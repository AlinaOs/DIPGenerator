import gc
import re
import json
import tarfile
import tempfile
import platform
from data.conf import DIPRequest
from data.ip import AIP
from drh.generators import DIPGenerator, ViewDIPGenerator


class DIPRequestHandler:
    def __init__(self, temp, conf, confName):
        self.temp = temp
        self.dgen = DIPGenerator()
        self.vdgen = ViewDIPGenerator()
        self.confPath = conf
        self.conf = self.__load_profile_conf__(confName)
        self.descs = self.__load_profile_descs__()
        self.info = self.__load_general_info__()
        self.tempdir = tempfile.TemporaryDirectory()
        self.aips = {}

        print(self.descs["profile0"])
        print(self.info["general"])
        print(self.conf["issuedBy"])

    def __load_profile_conf__(self, confName):
        with open(self.confPath+confName, "r") as confile:
            jsonconf = json.load(confile)
        return jsonconf

    def __load_profile_descs__(self):
        descs = {}
        for profile in self.conf["profileConfigs"]:
            path = self.conf["profileConfigs"][profile]["desc"]
            with open(self.confPath+path, "r") as desc:
                jsondesc = json.load(desc)
                descs.update({profile: jsondesc})
        return descs

    def __load_general_info__(self):
        path = self.conf["info"]
        with open(self.confPath+path, "r", encoding="utf-8") as info:
            jsoninfo = json.load(info)
        return jsoninfo

    def start_request(self):
        pass

    def send_response(self):
        pass

    def get_info(self, prop):
        return self.info[prop]

    def get_aipinfo(self, paths, vze=None):
        pass

    def parse_aip(self, paths, vze=None):
        # https://www.askpython.com/python-modules/tarfile-module
        delim = "/"
        # if platform.system() == "Windows":
        #     delim = "\\"

        # Todo: check if dir, then paths = all files

        ieid = None
        aips = []
        for p in paths:

            # Check, if file is tar.
            if not tarfile.is_tarfile(p):
                return DrhError("FormatError", p)

            aipid = re.split(delim, p)[-1][0:-4]
            aip = None
            if aipid not in aips:
                # Try to create an AIP object.
                aip = AIP(p, self.tempdir)

                # Check, if tar is AIP.
                if not aip.isaip():
                    del aip
                    gc.collect()
                    return DrhError("AIPError", p)
            else:
                aip = aips[aipid]
            aips.append(aip)

            # Check, if all tars represent the same IE.
            if ieid is None:
                ieid = aip.getie()
            elif not ieid == aip.getie():
                return DrhError("IEError", "AIP-ID: "+aip.getid()+", IE-ID: "+aip.getie())

            # Todo: Check, if the tars and the VZE represent the same IE.

        # Todo: Check, if each parent AIP is also present

        # Set the correct index for each AIP of this IE
        aips = sorted(aips)
        for i in range(len(aips)):
            aips[i].setindex(i)
            self.aips.update({aips[i].ipid: aips[i]})

        print(self.aips)

    def send_errormsg(self):
        pass

    def prepare_exit(self):
        self.tempdir.cleanup()


class DrhError:
    def __init__(self, etype, detail):
        self.etype = etype
        self.desc = self.assigndesc()
        self.detail = detail

    def assigndesc(self):
        if self.etype == "FormatError":
            return "At least one of the submitted files is not a TAR file."
        return ""

    def gettype(self):
        return self.etype

    def getdesc(self):
        return self.desc

    def getdetail(self):
        return self.detail


