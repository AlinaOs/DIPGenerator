import gc
import os.path
import re
import json
import tarfile
import tempfile
from drh.ip import AIP, DIP, ViewDIP

# Todo: Delimiter
delim = "/"


class DIPRequestHandler:
    def __init__(self, confdir, conf, vconfdir, vconf):
        self._confdir = confdir
        self._conf = self._loadconf(confdir, conf)
        self.vconf = self._loadconf(vconfdir, vconf)
        self._descs = self._loadpdescs()
        self._info = self._loadinfo()
        self._tempdir = tempfile.TemporaryDirectory()
        self._aips = {}

    def _loadconf(self, dir_, conf):
        with open(dir_ + conf, "r") as confile:
            jsonconf = json.load(confile)
        return jsonconf

    def _loadpdescs(self):
        descs = {}
        for profile in self._conf["profileConfigs"]:
            path = self._conf["profileConfigs"][profile]["desc"]
            with open(self._confdir + path, "r") as desc:
                jsondesc = json.load(desc)
                descs.update({profile: jsondesc})
        return descs

    def _loadinfo(self):
        path = self._conf["info"]
        with open(self._confdir + path, "r", encoding="utf-8") as info:
            jsoninfo = json.load(info)
        return jsoninfo

    def startrequest(self, uchoices):
        suc = self._parseaip(uchoices["aipPaths"])
        if isinstance(suc, DrhError):
            return suc

        pconf = self._conf["profileConfigs"]["profile"+str(uchoices["profileNo"])]
        pconf.update({"xsl": self._confdir + pconf["xsl"]})
        pconf.update({"xsd": self._confdir + pconf["xsd"]})
        print(pconf)
        req = {
            "aips": [self._aips[x] for x in uchoices["chosenAips"]],
            "pconf": pconf,
            "vzePath": uchoices["vzePath"],
            "isil": self._conf["issuedBy"]
        }

        # Create DIP and, if user chose download as delivery type, save it
        dip = DIP(req, self._tempdir)
        if uchoices["deliveryType"] != "viewer":
            dip.save(uchoices["outputPath"])

        # If user chose Viewer as delivery type, create ViewDIP
        if uchoices["deliveryType"] != "download":
            vdip = ViewDIP(dip, self.vconf, self._tempdir)
            vdip.save(uchoices["outputPath"])

    def sendresponse(self):
        pass

    def getinfo(self, prop):
        return self._info[prop]

    def getaipinfo(self, paths, vze=None):
        aips = self._parseaip(paths, vze)
        aipinfo = []
        for a in aips:
            aip = {
                "n": str(a.getindex()),
                "date": a.getdate()[0:10],
                "formats": set(a.getformats())
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

        if vze is None:
            vzeinfo = a.getieinfo()
        else:
            pass

        return {
            "aipinfo": aipinfo,
            "vzeinfo": vzeinfo
        }

    def _parseaip(self, paths, vze=None):

        if not isinstance(paths, list):
            if os.path.isdir(paths):
                pathfiles = os.listdir(paths)
                p = paths
                paths = []
                for f in pathfiles:
                    paths.append(p+"\\"+f)
            else:
                return DrhError("FormatError", paths)

        ieid = None
        aips = []
        aipids = []
        for p in paths:

            # Check, if file exists
            if not os.path.exists(p):
                return DrhError("FormatError", p)

            # Check, if file is tar.
            if not tarfile.is_tarfile(p) or os.path.isdir(p):
                return DrhError("FormatError", p)

            aipid = re.split(delim, p)[-1][0:-4]
            if aipid not in self._aips and aipid not in aipids:
                # Try to create an AIP object.
                aip = AIP(p, self._tempdir)

                # Check, if tar is AIP.
                if not aip.isaip():
                    del aip
                    gc.collect()
                    return DrhError("AIPError", p)

                self._aips.update({aipid: aip})
            else:
                aip = self._aips[aipid]
            aips.append(aip)
            aipids.append(aipid)

            # Check, if all tars represent the same IE.
            if ieid is None:
                ieid = aip.getie()
            elif not ieid == aip.getie():
                return DrhError("IEError", "AIP-ID: "+aip.getid()+", IE-ID: "+aip.getie())

            # Todo: Check, if the tars and the VZE represent the same IE.

        # Todo: Check, if each parent AIP is also present?

        # Set the correct index for each AIP of this IE
        aips = sorted(aips)
        for i in range(len(aips)):
            aips[i].setindex(i)
            self._aips.update({aipids[i]: aips[i]})

        return aips

    def prepare_exit(self):
        self._tempdir.cleanup()


class DrhError:
    def __init__(self, etype, detail):
        self.etype = etype
        self.desc = self.assigndesc()
        self.detail = detail

    def assigndesc(self):
        if self.etype == "FormatError":
            return "The given path doesn't lead to a directory or at least one of the submitted paths / files in the"\
                   "given directory is a directory or not a TAR file!"
        if self.etype == "AIPError":
            return "At least one of the submitted files couldn't be read because it isn't a valid AIP!"
        if self.etype == "IEError":
            return "The submitted AIPs and VZE Info don't represent the same Intellectual Entity. At least one of the"\
                   "submitted files represents a different Entity than the others"

    def gettype(self):
        return self.etype

    def getdesc(self):
        return self.desc

    def getdetail(self):
        return self.detail


