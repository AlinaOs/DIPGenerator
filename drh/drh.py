import json
from data.conf import DIPRequest
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
        self.aips = []

        # print(self.descs["profile0"])
        # print(self.info["general"])
        # print(self.conf["issuedBy"])

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
        with open(self.confPath+path, "r") as info:
            jsoninfo = json.load(info)
        return jsoninfo

    def start_request(self):
        pass

    def send_response(self):
        pass

    def get_info(self, prop):
        return self.info[prop]

    def get_aipinfo(self, paths):
        pass

    def parse_aip(self, paths):
        pass

    def send_errormsg(self):
        pass

    def prepare_exit(self):
        pass


