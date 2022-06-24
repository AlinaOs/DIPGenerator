import sys
from PySide6.QtWidgets import QApplication, QAbstractButton
from drh.drh import DIPRequestHandler
from drh.err import NoPathError
from rv.gui import RvMainWindow, MessageBox, MsgTrigger, MsgType


class RequestViewer:
    """Main class for the initialization and management of the Request Viewer application."""

    _aips: list[dict]
    # _vze: str # VZE
    _chosenaips: list[int]
    _delivery: str
    _profile: int
    _output: str

    def __init__(self, drh: DIPRequestHandler, texts: str):
        """Initialize and return a new Request Viewer object."""

        self._drh = drh
        self.texts = texts
        self._aips = []
        # self._vze = None # VZE
        self._chosenaips = []
        self._delivery = None
        self._profile = None
        self._output = None
        self._pinfo = self._drh.getprofileinfo()

        # User choice markers: Has the user already chosen a profile, an aip, a delivery?
        # If not, default settings shall be used, when the user changes a profile.
        # If he has already chosen himself, those choices shall not be overruled!
        self._aipuc = False
        self._profuc = False
        self._delivuc = False

        # User guidance markers: They hold the current status of the program, e.g.
        # has the user successfully provided all the needed user choices at least once?
        self._aippathneeded = True
        self._aipconfirmneeded = True
        self._outputneeded = True
        self._goneeded = True
        self.firstoverallsuccess = False

        self.app = QApplication(sys.argv)
        self.window = RvMainWindow(len(self._pinfo["nos"]), texts)
        self.window.retranslateProfiles(self._pinfo["nos"], self._pinfo["names"], self._pinfo["recoms"])

        # Button groups for the handling of clicks on buttons.
        self.mbtns = self.window.menuGroup
        self.ibtns = self.window.infoGroup
        self.pbtns = self.window.profileGroup
        self.pdbtns = self.window.profDetGroup
        self.rbtns = self.window.repsGroup
        self.rdbtns = self.window.repsDetGroup
        self.obtns = self.window.overviewGroup

        self._setclickhandlers()
        self.window.aipFileSpinner.setBoxHighlighting(True)
        self.window.goButton.pseudoenable()
        self._setdefaultprofile()
        self.window.show()
        self.app.exec()

    def _setclickhandlers(self):
        """Set the input handlers for the viewer's components."""

        self.mbtns.buttonClicked.connect(self._navigate)
        self.ibtns.buttonClicked.connect(self._navigateinfo)
        self.window.spinnerGoBtn.clicked.connect(self._loadaips)
        self.window.aipFileSpinner.edit.returnPressed.connect(self._loadaips)
        # self.window.vzeFileSpinner.edit.returnPressed.connect(self.loadaips) # VZE
        self.window.aipFileSpinner.edit.textChanged.connect(self._managespinnergobtn)

        self.pbtns.buttonClicked.connect(self._setprofile)
        self.pdbtns.buttonClicked.connect(self._toggleitb_p)
        self.rbtns.buttonToggled.connect(self._toggleaip)
        self.rdbtns.buttonClicked.connect(self._toggleitb_r)

        self.obtns.buttonClicked.connect(self._setdelivery)
        self.window.outFileSpinner.edit.textChanged.connect(self._manageoutput)
        self.window.goButton.clicked.connect(self._checkrequest)

    ###############################
    # Navigation and user guidance
    ###############################

    def _updateguidance(self):
        """Update the box highlighting to guide the user."""

        if self._aippathneeded:
            self.window.aipFileSpinner.setBoxHighlighting(True)
            self.window.spinnerGoBtn.setBoxHighlighting(False)
            self.window.outFileSpinner.setBoxHighlighting(False)
            self.window.goButton.pseudoenable()
            self.window.goButton.setBoxHighlighting(False)
        elif self._aipconfirmneeded:
            self.window.aipFileSpinner.setBoxHighlighting(False)
            self.window.spinnerGoBtn.setBoxHighlighting(True)
            self.window.outFileSpinner.setBoxHighlighting(False)
            self.window.goButton.setBoxHighlighting(False)
        elif self._outputneeded:
            self.window.aipFileSpinner.setBoxHighlighting(False)
            self.window.spinnerGoBtn.setBoxHighlighting(False)
            self.window.outFileSpinner.setBoxHighlighting(True)
            self.window.goButton.pseudoenable()
            self.window.goButton.setBoxHighlighting(False)
        elif self._goneeded:
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

    def _navigateinfo(self, btn: QAbstractButton):
        """Navigate the infopages."""

        id_ = self.ibtns.id(btn)
        if id_-1 < 0:
            id_ = 3
        self.mbtns.button(id_).click()

    def _navigate(self, btn: QAbstractButton):
        """Navigate the main menu (infopages and request dialog)."""

        id_ = self.mbtns.id(btn)
        if id_ == 1:
            self.window.setInfoPage(self._drh.getinfo("profiles"))
        elif id_ == 2:
            self.window.setInfoPage(self._drh.getinfo("representations"))
        elif id_ == 3:
            self.window.setInfoPage(self._drh.getinfo("general"))
        else:
            self.window.stackedWidget.setCurrentIndex(0)

    def _managespinnergobtn(self, text: str):
        """Update the internal status on change of the input path(s)."""

        if text == "" and not self.firstoverallsuccess:
            if not self._aips:
                self._aippathneeded = True
            self._aipconfirmneeded = True
        else:
            self._aippathneeded = False
            self._aipconfirmneeded = True
        self._updateguidance()

    def _manageoutput(self, text: str):
        """Update the internal status on change of the output path."""

        if text == "":
            self._outputneeded = True
        else:
            self._outputneeded = False
        self._updateguidance()

    def _toggleaip(self, btn: QAbstractButton, checked: bool):
        """Choose or unchoose an AIP."""

        self._aipuc = True
        if checked:
            self._chosenaips.append(self.rbtns.id(btn))
            self._chosenaips = sorted(self._chosenaips)
            self.window.updateOvRepTb(self._chosenaips, True)
        else:
            self._chosenaips.remove(self.rbtns.id(btn))
            self.window.updateOvRepTb(self._chosenaips, True)

    def _toggleitb_p(self, btn: QAbstractButton):
        """Show or hide an info text browser for a profile."""

        id_ = self.pdbtns.id(btn)
        if not self.window.profileInfos[id_]:
            pinfo = self._drh.getprofileinfo(id_)
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

    def _toggleitb_r(self, btn: QAbstractButton):
        """Show or hide an info text browser for an AIP."""

        id_ = self.rdbtns.id(btn)
        if not self.window.aipInfos[id_]:
            self.window.createitb(
                self.window.rScrollAreaContents,
                self.window.aips[id_],
                "a",
                id_,
                self._aips[id_]
            )
        else:
            tb = self.window.aipInfos[id_]
            self.window.aipInfos[id_] = None
            tb.close()

    ######################
    # Set default choices
    ######################

    def _setdefaultprofile(self):
        """Set the default profile."""

        no = self._drh.getdefaultprofile()
        profuc = self._profuc
        self.window.profileTitles[no].click()
        self._profuc = profuc

    def _setdefaultaips(self):
        """Set the default AIPs for the current profile."""

        default = self._drh.getdefaultaips(self._profile)
        aipuc = self._aipuc
        if default == "all":
            for a in self.window.aipTitles:
                a.setChecked(True)
        elif default == "frame":
            self.window.aipTitles[0].setChecked(True)
            if len(self.window.aipTitles) > 1:
                self.window.aipTitles[-1].setChecked(True)
                for i in range(1, len(self.window.aipTitles) - 1):
                    self.window.aipTitles[i].setChecked(False)
                    if not self._drh.aipchoice(self._profile):
                        self.window.setAIPenabled(False, self.window.aips[i], self._drh.getaipmessage(self._profile))
        else:  # latest
            self.window.aipTitles[-1].setChecked(True)
            if len(self.window.aipTitles) > 1:
                for i in range(len(self.window.aipTitles) - 1):
                    self.window.aipTitles[i].setChecked(False)
                    if not self._drh.aipchoice(self._profile):
                        self.window.setAIPenabled(False, self.window.aips[i], self._drh.getaipmessage(self._profile))

        self._aipuc = aipuc

    ###################
    # Set user choices
    ###################

    def _loadaips(self):
        """Load and show the AIPs chosen in the aipFileSpinner's FileDialog."""

        aips = self.window.aipFileSpinner.paths
        if aips is None:
            err = NoPathError("")
            msg = MessageBox(self.window, MsgType.ERROR, MsgTrigger.LOAD, self.texts, [err])
            msg.show()
            return

        # Remove all present AIPs
        self._aips = []
        self.window.closeAips()

        # Set new AIPs
        # vze = self.window.vzeFileSpinner.paths # VZE
        resp = self._drh.getaipinfo(aips, vze=None)
        info = resp.getinfo()
        errs = resp.geterrors()
        if info is not None:
            self._aips = info["aipinfo"]
            self._aipconfirmneeded = False
            self._updateguidance()
            if errs:
                msg = MessageBox(self.window, MsgType.WARNING, MsgTrigger.LOAD, self.texts, errs)
                msg.show()
        else:
            msg = MessageBox(self.window, MsgType.ERROR, MsgTrigger.LOAD, self.texts, errs)
            msg.show()
            return

        aipformats = []
        for i in range(len(self._aips)):
            self.window.createAIP(self.window.repLayoutV, self.window.scrollAreaContents, i)
            aipformats.append(list(self._aips[i]["formats"]))
        self.window.retranslateAips(aipformats)
        self._aipuc = False
        self._setdefaultaips()

        # Update overview with VZE info
        self.window.updateOvVzeTb(
            info["vzeinfo"]["signature"],
            info["vzeinfo"]["title"],
            info["vzeinfo"]["aiptype"],
            info["vzeinfo"]["type"],
            info["vzeinfo"]["runtime"],
            info["vzeinfo"]["contains"]
        )

    def _setprofile(self, btn: QAbstractButton):
        """Choose a profile and update the internal status."""

        self._profuc = True
        self._profile = self.pbtns.id(btn)
        self.window.updateOvProTb(self._pinfo["nos"][self._profile], self._pinfo["names"][self._profile])
        self._enablealldeliv()

        if not self._delivery or not self._drh.deliverychoice(self._profile) or not self._delivuc:
            deliv = self._drh.getdefaultdelivery(self._profile)
            delivuc = self._delivuc
            if deliv == "viewer":
                self.window.btnViewer.click()
                if not self._drh.deliverychoice(self._profile):
                    self.window.btnDownload.enable(False, self._drh.getdeliverymessage(self._profile))
                    self.window.btnBoth.enable(False, self._drh.getdeliverymessage(self._profile))
                else:
                    self._enablealldeliv()
            elif deliv == "both":
                self.window.btnBoth.click()
                if not self._drh.deliverychoice(self._profile):
                    self.window.btnViewer.enable(False, self._drh.getdeliverymessage(self._profile))
                    self.window.btnDownload.enable(False, self._drh.getdeliverymessage(self._profile))
                else:
                    self._enablealldeliv()
            else:
                self.window.btnDownload.click()
                if not self._drh.deliverychoice(self._profile):
                    self.window.btnViewer.enable(False, self._drh.getdeliverymessage(self._profile))
                    self.window.btnBoth.enable(False, self._drh.getdeliverymessage(self._profile))
                else:
                    self._enablealldeliv()
            self._delivuc = delivuc

        for a in self.window.aips:
            self.window.setAIPenabled(True, a)
        if self._aips and (not self._drh.aipchoice(self._profile) or not self._aipuc):
            self._setdefaultaips()

    def _setdelivery(self, btn: QAbstractButton):
        """Choose a delivery type and update the internal status."""

        self._delivuc = True
        id_ = self.obtns.id(btn)
        if id_ == 0:
            self._delivery = "viewer"
        elif id_ == 1:
            self._delivery = "download"
        elif id_ == 2:
            self._delivery = "both"

    def _enablealldeliv(self):
        """Set all delivery options to enabled."""

        self.window.btnViewer.enable(True)
        self.window.btnDownload.enable(True)
        self.window.btnBoth.enable(True)

    ################
    # Start request
    ################

    def _checkrequest(self):
        """Check, whether all conditions for a successfull request are given.

        If not, show a message.
        """

        if self.window.goButton.ispseudoenabled():
            msg = MessageBox(self.window, MsgType.ERROR, MsgTrigger.GOBTN, self.texts,)
            msg.show()
            return
        elif self._aipconfirmneeded:
            msg = MessageBox(self.window, MsgType.WARNING, MsgTrigger.GOBTN, self.texts,)
            msg.open()
            msg.finished.connect(self._checkcancel)
        else:
            self._startrequest()

    def _checkcancel(self, req: bool):
        """Start or cancel a request.

        :param req: Indicates, whether the request should be started or not.
        """

        if req:
            self._startrequest()
        else:
            return

    def _startrequest(self):
        """Start a request and handle the response."""

        # Create a user choice dictionary.
        uc = {
            "vzePath": None,  # self.window.vzeFileSpinner.paths, # VZE
            "profileNo": self._profile,
            "deliveryType": self._delivery,
            "outputPath": self.window.outFileSpinner.paths,
            "chosenAips": [self._aips[i]["path"] for i in self._chosenaips]
        }
        resp = self._drh.startrequest(uc).getfullresponse()

        # Handle the response.
        if not resp["errors"]:
            output = [resp["success"][-1]["detail"]]
            if self._delivery == "both":
                output.append(resp["success"][-2]["detail"])
            msg = MessageBox(self.window, MsgType.SUCCESS, MsgTrigger.REQUEST, self.texts, details=output)
            msg.show()
        else:
            msg = MessageBox(self.window, MsgType.ERROR, MsgTrigger.REQUEST, self.texts, details=resp["errors"])
            msg.show()
        self.window.goButton.setChecked(False)
        self._goneeded = False
        self._updateguidance()
