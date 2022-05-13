

class DIPRequest:

    def __init__(self, conf, userchoices, aips):
        self.conf = conf
        self.aips = aips
        self.output = userchoices["outputPath"]
        self.delivery = userchoices["deliveryType"]
