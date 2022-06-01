import sys
from PySide6.QtWidgets import QApplication
from drh.drh import DIPRequestHandler
from rv.gui import RvMainWindow


class RequestViewer:
    def __init__(self, drh: DIPRequestHandler):
        self.drh = drh
        self.aips = []
        self.vze = None
        self.chosenaips = []
        self.delivery = None
        self.profile = None
        self.output = None
        self.pinfo = self.drh.getprofileinfo()

        # User choice markers: Has the user already chosen a profile, an aip, a delivery?
        # If not, default settings shall be used, when the user changes a profile.
        # If he has already chosen himself, those choices shall not be overruled!
        self.aipuc = False
        self.profuc = False
        self.delivuc = False

        self.app = QApplication(sys.argv)
        self.window = RvMainWindow(len(self.pinfo["nos"]))
        self.retranslateUi()

        self.mbtns = self.window.menuGroup
        self.ibtns = self.window.infoGroup
        self.pbtns = self.window.profileGroup
        self.pdbtns = self.window.profDetGroup
        self.rbtns = self.window.repsGroup
        self.rdbtns = self.window.repsDetGroup
        self.obtns = self.window.overviewGroup

        self.setclickhandlers()
        self.setdefaultprofile()
        self.window.show()
        self.app.exec()

    def setdefaultprofile(self):
        no = self.drh.getdefaultprofile()
        profuc = self.profuc
        self.window.profileTitles[no].click()
        self.profuc = profuc

    def retranslateUi(self):
        self.window.retranslateBaseUi()
        self.window.retranslateProfiles(self.pinfo["nos"], self.pinfo["names"], self.pinfo["recoms"])

    def setclickhandlers(self):
        self.mbtns.buttonClicked.connect(self.navigate)
        self.ibtns.buttonClicked.connect(self.navigateinfo)
        self.window.spinnerGoBtn.clicked.connect(self.getaipinfo)
        self.window.aipFileSpinner.edit.returnPressed.connect(self.getaipinfo)
        self.window.vzeFileSpinner.edit.returnPressed.connect(self.getaipinfo)

        self.pbtns.buttonClicked.connect(self.setprofile)
        self.pdbtns.buttonToggled.connect(self.toggleitb_p)
        self.rbtns.buttonToggled.connect(self.toggleaip)
        self.rdbtns.buttonToggled.connect(self.toggleitb_r)

        self.obtns.buttonClicked.connect(self.setdelivery)
        self.window.goButton.clicked.connect(self.startrequest)

    def navigateinfo(self, btn):
        id_ = self.ibtns.id(btn)
        if id_-1 < 0:
            id_ = 3
        self.mbtns.button(id_).click()

    def navigate(self, btn):
        id_ = self.mbtns.id(btn)
        if id_ == 1:
            self.window.setInfoPage(self.drh.getinfo("profiles"))
        elif id_ == 2:
            self.window.setInfoPage(self.drh.getinfo("representations"))
        elif id_ == 3:
            self.window.setInfoPage(self.drh.getinfo("general"))
        else:
            self.window.stackedWidget.setCurrentIndex(0)

    def getaipinfo(self):
        aips = self.window.aipFileSpinner.paths
        if aips is None:
            print("Error! Aips is None!")
            return

        # Remove all present AIPs
        self.aips = []
        self.window.closeAips()

        # Set new AIPs
        vze = self.window.vzeFileSpinner.paths
        info = self.drh.getaipinfo(aips, vze).getinfo()
        self.aips = info["aipinfo"]
        aipformats = []
        for i in range(len(self.aips)):
            self.window.createAIP(self.window.repLayoutV, self.window.scrollAreaContents, i)
            aipformats.append(list(self.aips[i]["formats"]))
        self.window.retranslateAips(aipformats)
        self.aipuc = False
        self.setdefaultaips()

        # Update overview with VZE info
        self.window.updateOvVzeTb(
            info["vzeinfo"]["signature"],
            info["vzeinfo"]["title"],
            info["vzeinfo"]["aiptype"],
            info["vzeinfo"]["type"],
            info["vzeinfo"]["runtime"],
            info["vzeinfo"]["contains"]
        )

    def setprofile(self, btn):
        self.profuc = True
        self.profile = self.pbtns.id(btn)
        self.window.updateOvProTb(self.pinfo["nos"][self.profile], self.pinfo["names"][self.profile])

        if not self.delivery or (not self.drh.deliverychoice(self.profile) or not self.delivuc):
            deliv = self.drh.getdefaultdelivery(self.profile)
            delivuc = self.delivuc
            if deliv == "viewer":
                self.window.btnViewer.click()
            elif deliv == "both":
                self.window.btnBoth.click()
            else:
                self.window.btnDownload.click()
            self.delivuc = delivuc

        if self.aips and (not self.drh.aipchoice(self.profile) or not self.aipuc):
            self.setdefaultaips()

    def setdefaultaips(self):
        default = self.drh.getdefaultaips(self.profile)
        aipuc = self.aipuc
        if default == "all":
            for a in self.window.aipTitles:
                a.setChecked(True)
        elif default == "frame":
            self.window.aipTitles[0].setChecked(True)
            if len(self.window.aipTitles) > 1:
                self.window.aipTitles[-1].setChecked(True)
                for i in range(1, len(self.window.aipTitles) - 1):
                    self.window.aipTitles[i].setChecked(False)
        else:  # latest
            self.window.aipTitles[-1].setChecked(True)
            if len(self.window.aipTitles) > 1:
                for i in range(len(self.window.aipTitles) - 1):
                    self.window.aipTitles[i].setChecked(False)
        self.aipuc = aipuc

    def toggleaip(self, btn, checked):
        self.aipuc = True
        if checked:
            self.chosenaips.append(self.rbtns.id(btn))
            self.chosenaips = sorted(self.chosenaips)
            self.window.updateOvRepTb(self.chosenaips, True)
        else:
            self.chosenaips.remove(self.rbtns.id(btn))
            self.window.updateOvRepTb(self.chosenaips, True)

    def setdelivery(self, btn):
        self.delivuc = True
        id_ = self.obtns.id(btn)
        if id_ == 0:
            self.delivery = "viewer"
        elif id_ == 1:
            self.delivery = "download"
        elif id_ == 2:
            self.delivery = "both"

    def toggleitb_p(self, btn, checked):
        id_ = self.pdbtns.id(btn)
        if checked:
            pinfo = self.drh.getprofileinfo(id_)
            infos = [
                pinfo["desc"],
                pinfo["suitability"],
                pinfo["ieLevel"],
                pinfo["itemLevel"],
                pinfo["archivalProcess"],
                pinfo["representations"],
                pinfo["other"]
            ]
            self.window.createitb(
                self.window.pScrollAreaContents,
                self.window.profiles[id_],
                "p",
                id_,
                infos
            )
        else:
            tb = self.window.profileInfos[id_]
            self.window.profileInfos[id_] = None
            tb.close()

    def toggleitb_r(self, btn, checked):
        id_ = self.rdbtns.id(btn)
        if checked:
            self.window.createitb(
                self.window.rScrollAreaContents,
                self.window.aips[id_],
                "a",
                id_,
                self.aips[id_]
            )
        else:
            tb = self.window.aipInfos[id_]
            self.window.aipInfos[id_] = None
            tb.close()

    def startrequest(self):
        uc = {
            "vzePath": self.window.vzeFileSpinner.paths,
            "profileNo": self.profile,
            "deliveryType": self.delivery,
            "outputPath": self.window.outFileSpinner.paths,
            "chosenAips": [self.aips[i]["path"] for i in self.chosenaips]
        }
        print("Requested!")
        # Todo: Show Response
        resp = self.drh.startrequest(uc)
        print(resp)
        self.window.goButton.setChecked(False)
