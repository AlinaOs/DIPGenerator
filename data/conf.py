

class DIPRequest:

    def __init__(self, conf, userchoices, aips):
        self.conf = conf
        self.aips = aips  # Todo
        self.output = userchoices["outputPath"]
        self.delivery = userchoices["deliveryType"]