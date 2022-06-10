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

    def __init__(self):
        self._responses = []
        self._errors = []
        self._success = None

    def newerror(self, errors: DrhError | list[DrhError]) -> None:
        if not isinstance(errors, list):
            self._errors = [errors]
        else:
            self._errors.extend(errors)

    def getfullresponse(self) -> dict:
        return {
            "success": self._success,
            "errors": self._errors
        }

    def printresponse(self) -> None:
        print("Success:")
        print(self._success)
        print("Errors:")
        print(self._errors)


class InfoResponse(AbstractDrhResponse):
    def __init__(self):
        super().__init__()
        self._errors = []

    def setinfo(self, infodict: dict) -> None:
        self._success = infodict

    def getinfo(self) -> dict:
        return self._success

    def geterrors(self) -> list[DrhError]:
        return self._errors


class DrhResponse(AbstractDrhResponse):
    def __init__(self):
        super().__init__()
        self._responses = []
        self._errors = []
        self._success = []

    def newsuccess(self, ip: str, type_: str, detail: str = None) -> None:
        suc = {
            "IP": ip,
            "type": type_
        }
        if detail:
            suc.update({"detail": detail})
        self._success.append(suc)


class DIPRequestHandler:
    def __init__(self, confdir: str, conf: str, vconfdir: str, vconf: str):
        self._confdir = confdir
        self._conf = self._loadconf(confdir, conf)
        self._vconf = self._loadconf(vconfdir, vconf)
        self._descs = self._loadpdescs()
        self._info = self._loadinfo()
        self._tempdir = tempfile.TemporaryDirectory()
        self._aips = {}
        self._proc = PySaxonProcessor(license=False)
        self._proc.set_cwd(os.getcwd())
        self._xsltproc = self._proc.new_xslt30_processor()

    def _loadconf(self, dir_: str, conf: str) -> dict:
        with open(os.path.join(dir_, conf), "r") as confile:
            jsonconf = json.load(confile)
        return jsonconf

    def _loadpdescs(self) -> list[dict]:
        descs = []
        for profile in self._conf["profileConfigs"]:
            path = profile["desc"]
            with open(os.path.join(self._confdir, path), "r", encoding="UTF-8") as desc:
                jsondesc = json.load(desc)
                descs.append(jsondesc)
        return descs

    def _loadinfo(self) -> dict:
        path = self._conf["info"]
        with open(os.path.join(self._confdir, path), "r", encoding="utf-8") as info:
            jsoninfo = json.load(info)
        return jsoninfo

    def startrequest(self, uchoices: dict) -> DrhResponse:
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
            xsdpath = os.path.join(self._confdir, self._conf["profileConfigs"][3]["xsd"])
            for a in aips:
                errs = a.save(path)
                if errs is not None:
                    resp.newerror(SavingError("AIP", errs))
                    return resp
                errs = a.savexsd(path, xsdpath)
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
        return self._info[prop]

    def getprofileinfo(self, p: int = None) -> dict:
        if p is not None:
            return self._descs[p]["fullDesc"]
        else:
            info = {
                "nos": [self._descs[i]["no"] for i in range(4)],
                "names": [self._descs[i]["shortName"] for i in range(4)],
                "recoms": [self._descs[i]["recommendation"] for i in range(4)]
            }
            return info

    def getdefaultprofile(self) -> int:
        return self._conf["standardProfile"]

    def getdefaultdelivery(self, no: int) -> str:
        return self._conf["profileConfigs"][no]["defaultDelivery"]

    def deliverychoice(self, no: int) -> bool:
        return self._conf["profileConfigs"][no]["deliveryChoice"]

    def getdeliverymessage(self, no: int) -> str:
        return self._descs[no]["deliveryInfo"]

    def getdefaultaips(self, no: int) -> str:
        return self._conf["profileConfigs"][no]["defaultAIP"]

    def aipchoice(self, no: int) -> bool:
        return self._conf["profileConfigs"][no]["AIPChoice"]

    def getaipmessage(self, no: int) -> str:
        return self._descs[no]["repInfo"]

    def getaipinfo(self, paths: str | list, vze: str = None) -> InfoResponse:
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
                ieid = aip.getie()
            if not ieid == aip.getie():
                errors.append(IEError("AIP-ID: " + aip.getid() + ", IE-ID: " + aip.getie(), fatal=True))
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
                errors.append(IEUncompleteError("Missing Parents: " + str(missingparents)))

        # Set the correct index for each AIP of this IE
        aips = sorted(aips)
        for i in range(len(aips)):
            aips[i].setindex(i)
            self._aips.update({aipids[i]: aips[i]})

        return aips, errors

    def prepare_exit(self) -> None:
        self._tempdir.cleanup()
        self._proc.release()
