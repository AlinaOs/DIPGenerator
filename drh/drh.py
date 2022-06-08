import os.path
import gc
import json
import tarfile
import tempfile
import traceback
from abc import ABC, abstractmethod

from saxonc import PySaxonProcessor

from drh.err import *
from drh.ip import AIP, DIP, ViewDIP


class DIPRequestHandler:
    def __init__(self, confdir, conf, vconfdir, vconf):
        self._confdir = confdir
        self._conf = self._loadconf(confdir, conf)
        self.vconf = self._loadconf(vconfdir, vconf)
        self._descs = self._loadpdescs()
        self._info = self._loadinfo()
        self._tempdir = tempfile.TemporaryDirectory()
        self._aips = {}
        self._proc = PySaxonProcessor(license=False)
        self._proc.set_cwd(os.getcwd())
        self._xsltproc = self._proc.new_xslt30_processor()

    def _loadconf(self, dir_, conf):
        with open(os.path.join(dir_, conf), "r") as confile:
            jsonconf = json.load(confile)
        return jsonconf

    def _loadpdescs(self):
        descs = {}
        for profile in self._conf["profileConfigs"]:
            path = self._conf["profileConfigs"][profile]["desc"]
            with open(os.path.join(self._confdir, path), "r", encoding="UTF-8") as desc:
                jsondesc = json.load(desc)
                descs.update({profile: jsondesc})
        return descs

    def _loadinfo(self):
        path = self._conf["info"]
        with open(os.path.join(self._confdir, path), "r", encoding="utf-8") as info:
            jsoninfo = json.load(info)
        return jsoninfo

    def startrequest(self, uchoices):
        resp = DrhResponse()
        aips, errors = self._parseaip(uchoices["chosenAips"], mode="req")
        if errors is not None and len(errors) > 0:
            resp.newerror(errors)
            return resp
        resp.newsuccess(ip="AIP", type_="parse", detail="Request AIPs")

        if uchoices["profileNo"] == 0:
            path = os.path.join(uchoices["outputPath"], aips[0].getieid())
            if os.path.exists(path):
                resp.newerror(PathExistsError(path))
                return resp
            os.mkdir(path)
            xsdpath = os.path.join(self._confdir, self._conf["profileConfigs"]["profile0"]["xsd"])
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

        pconf = dict(self._conf["profileConfigs"]["profile" + str(uchoices["profileNo"])])
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
            vdip = ViewDIP(dip, self.vconf, self._tempdir, self._xsltproc)
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

    def getinfo(self, prop):
        return self._info[prop]

    def getprofileinfo(self, p=None):
        if p is not None:
            return self._descs["profile" + str(p)]["fullDesc"]
        else:
            info = {
                "nos": [self._descs["profile" + str(i)]["no"] for i in range(4)],
                "names": [self._descs["profile" + str(i)]["shortName"] for i in range(4)],
                "recoms": [self._descs["profile" + str(i)]["recommendation"] for i in range(4)]
            }
            return info

    def getdefaultprofile(self):
        return self._conf["profileConfigs"][self._conf["standardProfile"]]["profileMetadata"]["profileNumber"]

    def getdefaultdelivery(self, no):
        return self._conf["profileConfigs"]["profile" + str(no)]["defaultDelivery"]

    def getdefaultaips(self, no):
        return self._conf["profileConfigs"]["profile" + str(no)]["defaultAIP"]

    def deliverychoice(self, no):
        return self._conf["profileConfigs"]["profile" + str(no)]["deliveryChoice"]

    def getdeliverymessage(self, no):
        return self._descs["profile"+str(no)]["deliveryInfo"]

    def getaipmessage(self, no):
        return self._descs["profile"+str(no)]["repInfo"]

    def aipchoice(self, no):
        return self._conf["profileConfigs"]["profile" + str(no)]["AIPChoice"]

    def getaipinfo(self, paths, vze=None):
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

    def _parseaip(self, paths, vze=None, mode="info"):
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

    def prepare_exit(self):
        self._tempdir.cleanup()
        self._proc.release()


class AbstractDrhResponse(ABC):

    def __init__(self):
        self._responses = []
        self._errors = []
        self._success = None

    def newerror(self, errors):
        if not isinstance(errors, list):
            self._errors = [errors]
        else:
            self._errors.extend(errors)

    def getfullresponse(self):
        return {
            "success": self._success,
            "errors": self._errors
        }

    def printresponse(self):
        print("Success:")
        print(self._success)
        print("Errors:")
        print(self._errors)


class InfoResponse(AbstractDrhResponse):
    def __init__(self):
        super().__init__()
        self._responses = []
        self._errors = []

    def setinfo(self, infodict):
        self._success = infodict

    def getinfo(self):
        return self._success

    def geterrors(self):
        return self._errors


class DrhResponse(AbstractDrhResponse):
    def __init__(self):
        super().__init__()
        self._responses = []
        self._errors = []
        self._success = []

    def newsuccess(self, ip, type_, detail=None):
        suc = {
            "IP": ip,
            "type": type_
        }
        if detail:
            suc.update({"detail": detail})
        self._success.append(suc)
