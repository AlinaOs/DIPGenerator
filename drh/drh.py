import os.path
import gc
import json
import tarfile
import tempfile
from abc import ABC
from saxonpy import PySaxonProcessor
from drh.err import *
from drh.ip import AIP, DIP, ViewDIP


class AbstractDrhResponse(ABC):
    """The abstract base class for response objects returned by the DIP Request Handler"""

    def __init__(self):
        """Initialize and return a response object."""
        self._responses = []
        self._errors = []
        self._success = None

    def newerror(self, errors: DrhError | list[DrhError]):
        """Extend the object's list of errors with the given DrHError or list of DrhError.

        :param errors: The errors to be appended.
        :type errors: DrhError | list[DrhError]
        """
        if not isinstance(errors, list):
            self._errors = [errors]
        else:
            self._errors.extend(errors)

    def getfullresponse(self) -> dict:
        """Return the full response as dictionary.

        :return: A dictionary with the keys "success" and "errors", containing whatever is stored in these properties.
        """
        return {
            "success": self._success,
            "errors": self._errors
        }

    def printresponse(self):
        """Print the response object.

        This function can be used for debugging and logging.
        """
        print("Success:")
        print(self._success)
        print("Errors:")
        print(self._errors)


class InfoResponse(AbstractDrhResponse):
    """The representation of an informative response."""

    def __init__(self):
        super().__init__()
        self._errors = []

    def setinfo(self, infodict: dict):
        """Set the given dictionary of informations as the _success property of the response object."""
        self._success = infodict

    def getinfo(self) -> dict:
        """Return the informative dictionary stored as the _success property of the response object."""
        return self._success

    def geterrors(self) -> list[DrhError]:
        """Return the list of errors stored as the _errors property of the response object."""
        return self._errors


class DrhResponse(AbstractDrhResponse):
    """The representation of a response to a DIP request."""
    def __init__(self):
        super().__init__()
        self._responses = []
        self._errors = []
        self._success = []

    def newsuccess(self, ip: str, type_: str, detail: str = None):
        """Add a new item to the list of successes of the response object.

        :param ip: The ID of the affected Information Package.
        :param type_: The type of the affected Information Package (e.g., "DIP", "VDIP", or "AIP")
        :param detail: An optional more detailed message.
        """
        suc = {
            "IP": ip,
            "type": type_
        }
        if detail:
            suc.update({"detail": detail})
        self._success.append(suc)


class DIPRequestHandler:
    """The main class handling DIP info- or generation-requests."""

    def __init__(self, confdir: str, conf: str, vconfdir: str, vconf: str):
        """Initialize and return a DIPRequestHandler object.

        The params given to this constructor are used throughout the entire
        existence of the object to load, parse, generate and save Information Packages.

        :param confdir: The path to the directory containing the DIP configs.
        :param conf: The path to the main DIP config file (relative to the confdir).
        :param vconfdir: The path to the directory containing the ViewDIP configs.
        :param vconf: The path to the main ViewDIP config file (relative to the vconfdir).
        """

        self._confdir = confdir
        self._conf = self._loadconf(confdir, conf)
        self._vconf = self._loadconf(vconfdir, vconf)
        self._pn = len(self._conf["profileConfigs"])
        self._descs = self._loadpdescs()
        self._info = self._loadinfo()
        self._tempdir = tempfile.TemporaryDirectory()
        self._aips = {}
        self._proc = PySaxonProcessor(license=False)
        self._proc.set_cwd(os.getcwd())
        self._xsltproc = self._proc.new_xslt30_processor()

    def _loadconf(self, dir_: str, conf: str) -> dict:
        """Load and return the given json config file as dictionary.

        :param dir_: The path to the directory, to which the conf path is relative.
        :param conf: The path to the json config file, relative to the dir_ path.
        :return: The config file as dictionary.
        """

        with open(os.path.join(dir_, conf), "r") as confile:
            jsonconf = json.load(confile)
        return jsonconf

    def _loadpdescs(self) -> list[dict]:
        """Load and return the descriptions of all possible DIP profiles.

        The method uses the object's _conf property. It should therefore only be called
        *after* the config file has been loaded and assigned to the _conf property.

        :return: A list of dictionaries containing the profile descriptions.
        """

        descs = []
        for profile in self._conf["profileConfigs"]:
            path = profile["desc"]
            with open(os.path.join(self._confdir, path), "r", encoding="UTF-8") as desc:
                jsondesc = json.load(desc)
                descs.append(jsondesc)
        return descs

    def _loadinfo(self) -> dict:
        """Load and return the general infotexts.

        The method uses the object's _conf property. It should therefore only be called
        *after* the config file has been loaded and assigned to the _conf property.

        :return: A dictionary containing the infotexts.
        """

        path = self._conf["info"]
        with open(os.path.join(self._confdir, path), "r", encoding="utf-8") as info:
            jsoninfo = json.load(info)
        return jsoninfo

    def startrequest(self, uchoices: dict) -> DrhResponse:
        """Start and execute a request for a DIP generation.

        The dictionary containing the user's choices must have the following keys:
            * "chosenAips": The paths to the requested AIPs.
            * "profileNumber": The index of the DIP profile to be used.
            * "deliveryType": The chosen deliveryType ("viewer", "download", "both").
            * "outputPath": The path of a directory, to where the (View)DIP shall be saved.

        :param uchoices: A dictionary containing the user's choices.
        :return: A response object containing information about successful steps and errors, if any.
        """

        resp = DrhResponse()
        aips, errors = self._parseaip(uchoices["chosenAips"], mode="req")
        if errors is not None and len(errors) > 0:
            resp.newerror(errors)
            return resp
        resp.newsuccess(ip="AIP", type_="parse", detail="Request AIPs")

        if uchoices["profileNo"] == 3:
            path = os.path.join(uchoices["outputPath"], aips[0].getieid())
            if os.path.exists(path):
                resp.newerror(PathExistsError(path))
                return resp
            os.mkdir(path)
            for a in aips:
                errs = a.save(path)
                if errs is not None:
                    resp.newerror(SavingError("AIP", errs))
                    return resp
                errs = a.savexsd(path)
                if errs is not None:
                    resp.newerror(SavingError("AIP", errs))
                    return resp
            resp.newsuccess(detail=path, ip="AIP", type_="save")
            return resp

        pconf = dict(self._conf["profileConfigs"][uchoices["profileNo"]])
        pconf.update({"xsl": os.path.join(self._confdir, pconf["xsl"])})
        pconf.update({"xsd": os.path.join(self._confdir, pconf["xsd"])})
        pconf.update({"generatorName": self._conf["generatorName"]})
        pconf.update({"generatorVersion": self._conf["generatorVersion"]})
        pconf.update({"issuedBy": self._conf["issuedBy"]})
        req = {
            "aips": aips,
            "pconf": pconf,
            "vzePath": uchoices["vzePath"]
        }

        # Create DIP and, if user chose download as delivery type, save it
        dip = DIP(req, self._tempdir, self._xsltproc)
        if not dip.initsuccess():
            resp.newerror(ParsingError(dip.getid(), dip.gettb()))
            return resp
        resp.newsuccess(ip="DIP", type_="parse", detail=dip.getid())
        if uchoices["deliveryType"] != "viewer":
            errs = dip.save(uchoices["outputPath"])
            if errs is not None:
                resp.newerror(SavingError(dip.getid(), errs))
                return resp
            resp.newsuccess(detail=os.path.join(uchoices["outputPath"], dip.getid()), ip="DIP", type_="save")

        # If user chose Viewer as delivery type, create ViewDIP
        if uchoices["deliveryType"] != "download":
            vdip = ViewDIP(dip, self._vconf, self._tempdir, self._xsltproc)
            if not vdip.initsuccess():
                resp.newerror(ParsingError(vdip.getid(), vdip.gettb()))
                return resp
            resp.newsuccess(ip="VDIP", type_="parse", detail=vdip.getid())
            errs = vdip.save(uchoices["outputPath"])
            if errs is not None:
                resp.newerror(SavingError(vdip.getid(), errs))
                return resp
            resp.newsuccess(detail=os.path.join(uchoices["outputPath"], vdip.getid()), ip="VDIP", type_="save")

        return resp

    def getinfo(self, prop: str) -> dict:
        """Returns the infotext for the given key as dictionary.

        :param prop: A key contained at the top level of the .json file with the general infotexts.
        :return: A dictionary containing the infotexts for the given key.
        """

        return self._info[prop]

    def getprofileinfo(self, p: int = None) -> dict:
        """Returns the infotexts for profiles as dictionary.

        If the param p is specified, the method returns the full description of
        the requested profile. If no profile index is specified, it constructs and
        returns an overview dictionary with the following keys:
            * "nos": The numbers (not the index!) of all profiles as list of ints.
            * "names": The short names of all profiles as list of strings.
            * "recoms": The short recommendations  of all profiles as list of strings.

        :param p: The index of the requested profile (optional).
        :return: A dictionary containing the requested information.
        """

        if p is not None:
            return self._descs[p]["fullDesc"]
        else:
            info = {
                "nos": [self._descs[i]["no"] for i in range(self._pn)],
                "names": [self._descs[i]["shortName"] for i in range(self._pn)],
                "recoms": [self._descs[i]["recommendation"] for i in range(self._pn)]
            }
            return info

    def getdefaultprofile(self) -> int:
        """Return the index of the default profile."""
        return self._conf["standardProfile"]

    def getdefaultdelivery(self, no: int) -> str:
        """Return the default delivery choice for the profile with the given index."""
        return self._conf["profileConfigs"][no]["defaultDelivery"]

    def deliverychoice(self, no: int) -> bool:
        """Return, whether a user delivery choice is allowed for the profile with the given index."""
        return self._conf["profileConfigs"][no]["deliveryChoice"]

    def getdeliverymessage(self, no: int) -> str:
        """Return the message to be displayed with the delivery choice for the profile with the given index."""
        return self._descs[no]["deliveryInfo"]

    def getdefaultaips(self, no: int) -> str:
        """Return the default aip choice for the profile with the given index."""
        return self._conf["profileConfigs"][no]["defaultAIP"]

    def aipchoice(self, no: int) -> bool:
        """Return, whether a user aip choice is allowed for the profile with the given index."""
        return self._conf["profileConfigs"][no]["AIPChoice"]

    def getaipmessage(self, no: int) -> str:
        """Return the message to be displayed with the aip choice for the profile with the given index."""
        return self._descs[no]["repInfo"]

    def getaipinfo(self, paths: str | list, vze: str = None) -> InfoResponse:
        """Create and return an info dictionary about the given AIPs.

        The method currently uses the ieinfo of the parsed AIPs to transform it into a standardised info
        dictionary. When VZE support is integrated, the method should instead use the VZE-xml for that,
        if it is supplied. The info dictionary is returned via an InfoResponse object, which also contains
        any DrhErrors raised during the parsing of the given AIPs.

        This standardised info dictionary has the following structure:
            * "aipinfo": A dictionary containing technical information about the AIP and its files.

                * "n": The index of the AIP.
                * "date": The creation date of the AIP.
                * "formats": The formats contained in the AIP.
                * "path": The path to the AIP's .tar file.
                * "files" A list containing a dictionary for each file contained in the AIP.

                    * "name": The original name of the file.
                    * "format": The format of the current file.
                    * "size": The size (in kb) of the current file.
                    * "preslev": The preservation level of the current file.
            * "vzeinfo": A dictionary containing archival information about the Intellectual Entity/VZE.

                * "signature": The signature of the archival file, or "?" when unknown.
                * "title": The IE/VZE's title.
                * "contains": The IE/VZE's description.
                * "runtime": The IE/VZE's runtime (formatted like "YYYY-MM-DD - YYYY-MM-DD").
                * "aiptype": The AIP's type (e.g., file collection or e-file).
                * "type": The IE/VZE's type (e.g. "Sachakte").

        :param paths: A path to a dictionary (as string) containing AIPs or multiple paths (as list) to AIPs.
        :param vze: A path to a .xml file containing information about the corresponding VZE (optional).
        :return: A response object containing the info dictionary as its _success property - containing _errors if any.
        :rtype: InfoResponse
        """
        resp = InfoResponse()
        aips, errors = self._parseaip(paths, vze=vze)
        resp.newerror(errors)
        if any(e.isfatal() for e in errors) or not aips:
            return resp

        aipinfo = []
        for a in aips:
            aip = {
                "n": str(a.getindex()),
                "date": a.getdate()[0:10],
                "formats": set(a.getformats()),
                "path": a.getpath()
            }

            files = []
            formats = a.getformats()
            sizes = a.getsizes()
            filenames = a.getfilenames()
            preslevs = a.getpreslevels()

            for i in range(len(filenames)):
                files.append({
                    "name": filenames[i],
                    "format": formats[i],
                    "size": sizes[i],
                    "preslev": preslevs[i]
                })

            aip.update({"files": files})
            aipinfo.append(aip)

        vzeinfo = None
        if vze is None:
            vzeinfo = aips[0].getieinfo()
            vzeinfo.update({"signature": None})
        else:
            pass  # Todo VZE

        resp.setinfo({
            "aipinfo": aipinfo,
            "vzeinfo": vzeinfo
        })
        return resp

    def _parseaip(self, paths: list | str, vze: str = None, mode: str = "info") -> (list[AIP], list[DrhError]):
        """Parse the given AIPs to AIP objects.

        The function checks the given paths and files for validity and creates an internal representation of
        them as AIP objects. If there are any non fatal errors, the parsing will go on and the errors registered
        in the response object. If there are fatal errors, the parsing will stop.
        The parsing of the AIPs is necessary to get ieinfos etc. from them.

        :param paths: A path to a dictionary (as string) containing AIPs or multiple paths (as list) to AIPs.
        :param vze: A path to a .xml file containing information about the corresponding VZE (optional).
        :param mode: "info" for an info request or "req" for a generation request.
        :return: A tuple containing first the AIP objects as list and second any occurring DrhErrors as list.
        """

        errors = []
        ieid = None
        aips = []
        aipids = []

        if not isinstance(paths, list):
            if os.path.isdir(paths):
                pathfiles = os.listdir(paths)
                p = paths
                paths = []
                for f in pathfiles:
                    paths.append(os.path.join(p, f))
            else:
                errors.append(PathError(paths, fatal=True))
                return aips, errors

        for p in paths:

            # Check, if file exists
            if not os.path.exists(p):
                errors.append(PathError(p))
                continue

            # Check, if file is tar.
            if not tarfile.is_tarfile(p) or os.path.isdir(p):
                errors.append(FormatError(p))
                continue

            aipid = os.path.basename(p)
            aipid = aipid[0:-4]
            if aipid not in self._aips and aipid not in aipids:
                # Try to create an AIP object.
                aip = AIP(p, os.path.join(self._confdir, self._conf["AIPschema"]), self._tempdir)

                # Check, if tar is AIP.
                if not aip.initsuccess():
                    errors.append(ParsingError(p, aip.gettb()))
                    del aip
                    gc.collect()
                    continue

                self._aips.update({aipid: aip})
            else:
                aip = self._aips[aipid]
            aips.append(aip)
            aipids.append(aipid)

            # Check, if all tars represent the same IE.
            if ieid is None:
                ieid = aip.getieid()
            if not ieid == aip.getieid():
                errors.append(IEError("AIP-ID: " + aip.getid() + ", IE-ID: " + aip.getieid(), fatal=True))
                continue
            if vze is not None:
                # Todo: Check, if the tars and the VZE represent the same IE.
                return IEError("AIP-IE: " + aip.getid() + ", VZE-IE: " + "Todo", fatal=True)

        # Check, if each parent AIP is present
        if mode == "info":
            missingparents = 0
            for i in range(len(aips)):
                if aips[i].getparent() and aips[i].getparent() not in aipids:
                    missingparents += 1
            if missingparents > 0:
                errors.append(IEIncompleteError("Missing Parents: " + str(missingparents)))

        # Set the correct index for each AIP of this IE
        aips = sorted(aips)
        for i in range(len(aips)):
            aips[i].setindex(i)
            self._aips.update({aipids[i]: aips[i]})

        return aips, errors
