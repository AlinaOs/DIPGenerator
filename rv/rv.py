import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from drh.drh import DIPRequestHandler
from rv.gui import RvMainWindow


class RequestViewer:
    def __init__(self, drh: DIPRequestHandler):
        self.drh = drh
        self.aips = []
        self.vze = None
        self.chosenaips = []
        self.delivery = "viewer"
        self.profile = 1
        self.output = None

        self.app = QApplication(sys.argv)
        self.window = RvMainWindow()

        for i in range(2):
            self.window.createAIP(self.window.repLayoutV, self.window.rScrollAreaContents, i)
        self.window.aipTitles[0].setChecked(True)
        self.window.retranslateUi()

        self.mbtns = self.window.menuGroup
        self.ibtns = self.window.infoGroup
        self.pbtns = self.window.profileGroup
        self.pdbtns = self.window.profDetGroup
        self.rbtns = self.window.repsGroup
        self.rdbtns = self.window.repsDetGroup
        self.obtns = self.window.overviewGroup

        self.setclickhandlers()
        self.window.show()
        self.app.exec()

    def setclickhandlers(self):
        self.mbtns.buttonClicked.connect(self.navigate)
        self.ibtns.buttonClicked.connect(self.navigate)
        self.window.spinnerGoBtn.clicked.connect(self.getaipinfo)
        self.window.aipFileSpinner.edit.returnPressed.connect(self.getaipinfo)
        self.window.vzeFileSpinner.edit.returnPressed.connect(self.getaipinfo)

        self.pbtns.buttonClicked.connect(self.setprofile)
        self.pdbtns.buttonToggled.connect(self.toggleitb_p)
        self.rbtns.buttonClicked.connect(self.addaip)
        self.rdbtns.buttonToggled.connect(self.toggleitb_r)

        self.obtns.buttonClicked.connect(self.setdelivery)
        self.window.goButton.clicked.connect(self.startrequest)

    def navigate(self, btn):
        if self.mbtns.id(btn) == 0:
            self.window.stackedWidget.setCurrentIndex(0)
        else:
            self.window.stackedWidget.setCurrentIndex(1)
            # Todo: Get Info Texts from DRH and show them

    def getaipinfo(self):
        aips = self.window.aipFileSpinner.paths
        if aips is None:
            print("Error! Aips is None!")
            return
        vze = self.window.vzeFileSpinner.paths
        print(aips)
        if vze:
            print(vze)
        # Todo: Get info from DRH and update AIPs/overview

    def setprofile(self, btn):
        self.profile = self.pbtns.id(btn)
        # Todo: Update overview

    def addaip(self, btn):
        self.chosenaips.append(self.rbtns.id(btn))
        # Todo: Update overview

    def setdelivery(self, btn):
        id_ = self.obtns.id(btn)
        if id == 0:
            self.delivery = "viewer"
        elif id == 1:
            self.delivery = "download"
        elif id == 2:
            self.delivery = "both"

    def toggleitb_p(self, btn, checked):
        id_ = self.pdbtns.id(btn)
        if checked:
            self.window.createitb(
                self.window.pScrollAreaContents,
                self.window.profiles[id_],
                "p",
                id_
            )
            # Todo: Get Info Texts from DRH and show them
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
                id_
            )
            # Todo: Get Info Texts from DRH and show them
        else:
            tb = self.window.aipInfos[id_]
            self.window.aipInfos[id_] = None
            tb.close()

    def startrequest(self):
        print("Requested!")
        # Todo: Start DIP Request and manage waiting time
        self.window.goButton.setChecked(False)
