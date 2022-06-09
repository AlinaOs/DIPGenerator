import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from drh.drh import DIPRequestHandler
from drh.err import DrhError, NoPathError
from rv.gui import RvMainWindow, MessageBox, MsgTrigger, MsgType


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

        # User guidance markers: They hold the current status of the program, e.g.
        # has the user successfully provided all the needed user choices at least once?
        self.aippathneeded = True
        self.aipconfirmneeded = True
        self.outputneeded = True
        self.goneeded = True
        self.firstoverallsuccess = False

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
        self.window.aipFileSpinner.setBoxHighlighting(True)
        self.window.goButton.pseudoenable()
        self.setdefaultprofile()
        self.window.show()
        self.app.exec()

    def updateguidance(self):
        if self.aippathneeded:
            self.window.aipFileSpinner.setBoxHighlighting(True)
            self.window.spinnerGoBtn.setBoxHighlighting(False)
            self.window.outFileSpinner.setBoxHighlighting(False)
            self.window.goButton.pseudoenable()
            self.window.goButton.setBoxHighlighting(False)
        elif self.aipconfirmneeded:
            self.window.aipFileSpinner.setBoxHighlighting(False)
            self.window.spinnerGoBtn.setBoxHighlighting(True)
            self.window.outFileSpinner.setBoxHighlighting(False)
            self.window.goButton.setBoxHighlighting(False)
        elif self.outputneeded:
            self.window.aipFileSpinner.setBoxHighlighting(False)
            self.window.spinnerGoBtn.setBoxHighlighting(False)
            self.window.outFileSpinner.setBoxHighlighting(True)
            self.window.goButton.pseudoenable()
            self.window.goButton.setBoxHighlighting(False)
        elif self.goneeded:
            self.window.aipFileSpinner.setBoxHighlighting(False)
            self.window.spinnerGoBtn.setBoxHighlighting(False)
            self.window.outFileSpinner.setBoxHighlighting(False)
            self.window.goButton.enable(True)
            self.window.goButton.setBoxHighlighting(True)
        else:
            self.window.aipFileSpinner.setBoxHighlighting(False)
            self.window.spinnerGoBtn.setBoxHighlighting(False)
            self.window.outFileSpinner.setBoxHighlighting(False)
            self.window.goButton.enable(True)
            self.window.goButton.setBoxHighlighting(False)

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
        self.window.aipFileSpinner.edit.textChanged.connect(self.managespinnergobtn)

        self.pbtns.buttonClicked.connect(self.setprofile)
        self.pdbtns.buttonClicked.connect(self.toggleitb_p)
        self.rbtns.buttonToggled.connect(self.toggleaip)
        self.rdbtns.buttonClicked.connect(self.toggleitb_r)

        self.obtns.buttonClicked.connect(self.setdelivery)
        self.window.outFileSpinner.edit.textChanged.connect(self.manageoutput)
        self.window.goButton.clicked.connect(self.checkrequest)

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
            err = NoPathError("")
            msg = MessageBox(self.window, MsgType.ERROR, MsgTrigger.LOAD, [err])
            msg.show()
            return

        # Remove all present AIPs
        self.aips = []
        self.window.closeAips()

        # Set new AIPs
        vze = self.window.vzeFileSpinner.paths
        resp = self.drh.getaipinfo(aips, vze)
        info = resp.getinfo()
        errs = resp.geterrors()
        if info is not None:
            self.aips = info["aipinfo"]
            self.aipconfirmneeded = False
            self.updateguidance()
            if errs:
                msg = MessageBox(self.window, MsgType.WARNING, MsgTrigger.LOAD, errs)
                msg.show()
        else:
            msg = MessageBox(self.window, MsgType.ERROR, MsgTrigger.LOAD, errs)
            msg.show()
            return

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
        self.enablealldeliv()

        if not self.delivery or not self.drh.deliverychoice(self.profile) or not self.delivuc:
            deliv = self.drh.getdefaultdelivery(self.profile)
            delivuc = self.delivuc
            if deliv == "viewer":
                self.window.btnViewer.click()
                if not self.drh.deliverychoice(self.profile):
                    self.window.btnDownload.enable(False, self.drh.getdeliverymessage(self.profile))
                    self.window.btnBoth.enable(False, self.drh.getdeliverymessage(self.profile))
                else:
                    self.enablealldeliv()
            elif deliv == "both":
                self.window.btnBoth.click()
                if not self.drh.deliverychoice(self.profile):
                    self.window.btnViewer.enable(False, self.drh.getdeliverymessage(self.profile))
                    self.window.btnDownload.enable(False, self.drh.getdeliverymessage(self.profile))
                else:
                    self.enablealldeliv()
            else:
                self.window.btnDownload.click()
                if not self.drh.deliverychoice(self.profile):
                    self.window.btnViewer.enable(False, self.drh.getdeliverymessage(self.profile))
                    self.window.btnBoth.enable(False, self.drh.getdeliverymessage(self.profile))
                else:
                    self.enablealldeliv()
            self.delivuc = delivuc

        for a in self.window.aips:
            self.window.setAIPenabled(True, a)
        if self.aips and (not self.drh.aipchoice(self.profile) or not self.aipuc):
            self.setdefaultaips()

    def enablealldeliv(self):
        self.window.btnViewer.enable(True)
        self.window.btnDownload.enable(True)
        self.window.btnBoth.enable(True)

    def managespinnergobtn(self, text):
        if text == "" and not self.firstoverallsuccess:
            if not self.aips:
                self.aippathneeded = True
            self.aipconfirmneeded = True
        else:
            self.aippathneeded = False
            self.aipconfirmneeded = True
        self.updateguidance()

    def manageoutput(self, text):
        if text == "":
            self.outputneeded = True
        else:
            self.outputneeded = False
        self.updateguidance()

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
                    if not self.drh.aipchoice(self.profile):
                        self.window.setAIPenabled(False, self.window.aips[i], self.drh.getaipmessage(self.profile))
        else:  # latest
            self.window.aipTitles[-1].setChecked(True)
            if len(self.window.aipTitles) > 1:
                for i in range(len(self.window.aipTitles) - 1):
                    self.window.aipTitles[i].setChecked(False)
                    if not self.drh.aipchoice(self.profile):
                        self.window.setAIPenabled(False, self.window.aips[i], self.drh.getaipmessage(self.profile))

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

    def toggleitb_p(self, btn):
        id_ = self.pdbtns.id(btn)
        if not self.window.profileInfos[id_]:
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

    def toggleitb_r(self, btn):
        id_ = self.rdbtns.id(btn)
        if not self.window.aipInfos[id_]:
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

    def checkrequest(self):
        if self.window.goButton.ispseudoenabled():
            msg = MessageBox(self.window, MsgType.ERROR, MsgTrigger.GOBTN)
            msg.show()
            return
        elif self.aipconfirmneeded:
            msg = MessageBox(self.window, MsgType.WARNING, MsgTrigger.GOBTN)
            msg.open()
            msg.finished.connect(self.checkcancel)
        else:
            self.startrequest()

    def checkcancel(self, req):
        if req:
            self.startrequest()
        else:
            return

    def startrequest(self):
        uc = {
            "vzePath": self.window.vzeFileSpinner.paths,
            "profileNo": self.profile,
            "deliveryType": self.delivery,
            "outputPath": self.window.outFileSpinner.paths,
            "chosenAips": [self.aips[i]["path"] for i in self.chosenaips]
        }
        resp = self.drh.startrequest(uc).getfullresponse()

        if not resp["errors"]:
            output = [resp["success"][-1]["detail"]]
            if self.delivery == "both":
                output.append(resp["success"][-2]["detail"])
            msg = MessageBox(self.window, MsgType.SUCCESS, MsgTrigger.REQUEST, details=output)
            msg.show()
        else:
            msg = MessageBox(self.window, MsgType.ERROR, MsgTrigger.REQUEST, details=resp["errors"])
            msg.show()
        self.window.goButton.setChecked(False)
        self.goneeded = False
        self.updateguidance()
