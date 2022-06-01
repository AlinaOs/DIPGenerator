# -*- coding: utf-8 -*-
import ast
import gc

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QLayout, QMainWindow, QPushButton, QRadioButton,
                               QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
                               QStackedWidget, QStatusBar, QTextBrowser, QVBoxLayout,
                               QWidget, QLineEdit, QToolButton, QStyle, QFileDialog, QButtonGroup, QAbstractScrollArea,
                               QGridLayout)
from rv import snippets
from rv.snippets import UiTextProvider

lwl_darkred = "#9b182a"  # RGB 155/24/42
lwl_darkblue = "#00325f"  # RGB 0/50/95
lwl_middlegray = "#b4b2b2"  # RGB 180/178/178
lwl_lightgray = "#e7e7e8"  # RGB 231/231/232
white = "#ffffff"

font12 = QFont()
font12.setFamilies(["Source Sans Pro"])
font12.setPointSize(12)

font12b = QFont()
font12b.setFamilies(["Source Sans Pro"])
font12b.setPointSize(12)
font12b.setBold(True)

font14 = QFont()
font14.setFamilies(["Source Sans Pro"])
font14.setPointSize(14)

font16 = QFont()
font16.setFamilies(["Source Sans Pro"])
font16.setPointSize(16)

icon_allpages = QIcon()
icon_allpages.addFile("svg/LWL_Alle_Seiten_sehen.svg", QSize(), QIcon.Normal, QIcon.Off)
icon_info = QIcon()
icon_info.addFile("svg/LWL_mehr_Infos.svg", QSize(), QIcon.Normal, QIcon.Off)
icon_check = QIcon() # https://www.iconshock.com/freeicons/check-circle-fill-24
icon_check.addFile("svg/Check.svg", QSize(), QIcon.Normal, QIcon.Off)
icon_link = QIcon()
icon_link.addFile("svg/LWL_Link.svg", QSize(), QIcon.Normal, QIcon.Off)
icon_directory = QIcon()
icon_directory.addFile("svg/Directory.svg", QSize(), QIcon.Normal, QIcon.Off)
icon_file = QIcon()
icon_file.addFile("svg/LWL_Dokument.svg", QSize(), QIcon.Normal, QIcon.Off)


class RvMainWindow(QMainWindow):
    def __init__(self, pn):
        super().__init__()
        self.utp = UiTextProvider()
        self.centralwidget = None
        self.stackedWidget = None
        self.pn = pn
        self.profilesLabel = None
        self.repsLabel = None
        self.pScrollArea = None
        self.rScrollArea = None

        self.menuButtons = []
        self.stepHeaders = []
        self.steps = []
        self.stepTitles = []
        self.stepInfos = []
        self.menuGroup = QButtonGroup()
        self.infoGroup = QButtonGroup()

        self.aipFileSpinner = None
        self.vzeFileSpinner = None
        self.spinnerGoBtn = None

        self.profiles = []
        self.profileHeaders = []
        self.profileTitles = []
        self.profileRecoms = []
        self.profileDetails = []
        self.profileInfos = []
        self.pScrollAreaContents = None
        self.profileGroup = QButtonGroup()
        self.profDetGroup = QButtonGroup()
        self.profDetGroup.setExclusive(False)

        self.aips = []
        self.aipInfos = []
        self.aipDetails = []
        self.aipTitles = []
        self.aipDescs = []
        self.aipFormats = []
        self.rScrollAreaContents = None
        self.repLayoutV = None
        self.repsGroup = QButtonGroup()
        self.repsGroup.setExclusive(False)
        self.repsDetGroup = QButtonGroup()
        self.repsDetGroup.setExclusive(False)

        self.overviewGroup = QButtonGroup()

        self.setupUi()

    def setupUi(self):
        self.setObjectName(u"MainWindow")
        self.resize(794, 570)
        palette = QPalette()
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        self.setPalette(palette)
        self.setCursor(QCursor(Qt.ArrowCursor))
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")

        menuLayout = QHBoxLayout()
        menuLayout.setSpacing(1)
        menuLayout.setObjectName(u"menuLayout")
        menuLayout.setContentsMargins(-1, -1, -1, 20)

        self.menuGroup.setParent(self.centralwidget)
        btnd = MenuButton(self.centralwidget, "btnDIP", True)
        menuLayout.addWidget(btnd)
        self.menuButtons.append(btnd)
        self.menuGroup.addButton(btnd)
        self.menuGroup.setId(btnd, 0)
        for i in range(1, 4):
            btn = MenuButton(self.centralwidget, "btnHelp" + str(i), False)
            menuLayout.addWidget(btn)
            self.menuButtons.append(btn)
            self.menuGroup.addButton(btn)
            self.menuGroup.setId(btn, i)

        content = QWidget()
        content.setObjectName(u"content")
        scrollLayout = QGridLayout(content)
        scrollLayout.setObjectName(u"scrollLayout")
        scrollArea = QScrollArea(content)
        scrollArea.setObjectName(u"scrollArea")
        scrollArea.setFrameShape(QFrame.NoFrame)
        scrollArea.setFrameShadow(QFrame.Plain)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        scrollArea.setWidgetResizable(True)
        self.scrollAreaContents = QWidget()
        self.scrollAreaContents.setObjectName(u"scrollAreaContents")
        self.scrollAreaContents.setGeometry(QRect(0, 0, 501, 552))
        contentLayoutV = QVBoxLayout(self.scrollAreaContents)
        contentLayoutV.setObjectName(u"contentLayoutV")

        self.infoGroup.setParent(self.scrollAreaContents)
        # Create Step Header
        for i in range(1, 4):
            stepFrame = QFrame(self.scrollAreaContents)
            stepFrame.setObjectName(u"step"+str(i)+"Frame")
            stepFrame.setMinimumSize(QSize(0, 20))
            stepFrame.setMaximumSize(QSize(16777215, 50))
            stepFrame.setStyleSheet(u".QFrame{\n"\
                                    "    border: 1px solid "+lwl_darkblue+";\n"\
                                    "    border-radius: 5px;\n"\
                                    "}")
            stepFrame.setFrameShape(QFrame.Box)
            stepFrame.setFrameShadow(QFrame.Plain)
            stepFrame.setLineWidth(2)

            step = QLabel(stepFrame)
            step.setObjectName(u"step"+str(i)+"step")
            step.setMinimumSize(QSize(70, 0))
            step.setMaximumSize(QSize(100, 16777215))
            step.setFont(font14)
            step.setAutoFillBackground(False)
            step.setStyleSheet(u".QLabel{\n"
                               "    border-radius: 5px;\n"\
                               "    background-color: "+lwl_darkblue+";\n"\
                               "    padding: 1px 10px;\n"\
                               "    color: #ffffff;\n"\
                               "}")
            step.setAlignment(Qt.AlignCenter)

            title = QLabel(stepFrame)
            title.setObjectName(u"step"+str(i)+"title")
            title.setFont(font16)
            title.setToolTipDuration(-1)
            title.setStyleSheet(u".QLabel{\n"\
                                "    color: "+lwl_darkblue+";\n"\
                                "    padding-top: 1px;\n"\
                                "    padding-bottom: 1px;\n"\
                                "}")

            info = QPushButton(stepFrame)
            info.setObjectName(u"step"+str(i)+"info")
            info.setMinimumSize(QSize(20, 0))
            info.setMaximumSize(QSize(30, 16777215))
            info.setCursor(QCursor(Qt.PointingHandCursor))
            info.setStyleSheet(u"QPushButton{\n"
                               "    padding-right: 5px\n"
                               "}")
            info.setIcon(icon_info)
            info.setFlat(True)

            # Layout step frame
            horizontalLayout = QHBoxLayout(stepFrame)
            horizontalLayout.setSpacing(0)
            horizontalLayout.setObjectName(u"horizontalLayout_12")
            horizontalLayout.setContentsMargins(0, 0, 0, 0)
            horizontalLayout.addWidget(step)
            horizontalLayout.addItem(QSpacerItem(50, 15, QSizePolicy.Fixed, QSizePolicy.Minimum))
            horizontalLayout.addWidget(title)
            horizontalLayout.addItem(QSpacerItem(50, 15, QSizePolicy.Fixed, QSizePolicy.Minimum))
            horizontalLayout.addWidget(info)

            self.steps.append(step)
            self.stepTitles.append(title)
            self.stepInfos.append(info)
            self.stepHeaders.append(stepFrame)

            self.infoGroup.addButton(info)
            self.infoGroup.setId(info, i-1)

        # Create Step 1 (file spinner)
        self.spinnerGoBtn = QToolButton(self.scrollAreaContents)
        self.spinnerGoBtn.setObjectName(u"fsgobtn")
        self.spinnerGoBtn.setMinimumSize(QSize(30, 30))
        self.spinnerGoBtn.setMaximumSize(QSize(30, 30))
        self.spinnerGoBtn.setIcon(icon_allpages)
        self.spinnerGoBtn.setIcon(icon_check)

        self.aipFileSpinner = FileSpinner(self.scrollAreaContents, "a")
        self.vzeFileSpinner = FileSpinner(self.scrollAreaContents, "v")

        # Layout file spinners
        fileSpinnerLayoutH = QHBoxLayout()
        fileSpinnerLayoutH.setObjectName(u"fileSpinnerWidget")
        fileSpinnerLayoutH.setContentsMargins(10, 10, 10, 20)
        self.aipFileSpinner.addToLayout(fileSpinnerLayoutH)
        fileSpinnerLayoutH.addItem(QSpacerItem(30, 30, QSizePolicy.Minimum, QSizePolicy.Minimum))
        self.vzeFileSpinner.addToLayout(fileSpinnerLayoutH)
        fileSpinnerLayoutH.addItem(QSpacerItem(30, 30, QSizePolicy.Minimum, QSizePolicy.Minimum))
        fileSpinnerLayoutH.addWidget(self.spinnerGoBtn)

        # Create step 2 (profiles)
        self.profilesLabel = QLabel(self.scrollAreaContents)
        self.profilesLabel.setObjectName(u"profilesLabel")
        self.profilesLabel.setFont(font12)
        self.profilesLabel.setWordWrap(True)

        self.profileGroup.setParent(self.scrollAreaContents)
        self.profDetGroup.setParent(self.scrollAreaContents)

        # Create profiles
        for i in range(self.pn):
            pTitle = LabelButton(self.scrollAreaContents)
            pTitle.setObjectName(u"ptitle")
            pTitle.setMinimumSize(QSize(120, 18))
            pTitle.setMaximumSize(QSize(200, 100))

            pRecom = QLabel(self.scrollAreaContents)
            pRecom.setObjectName(u"p"+str(i)+"recom")
            pRecom.setFont(font12)
            pRecom.setAlignment(Qt.AlignCenter)

            line1 = Line(self.scrollAreaContents, max_=QSize(60, 16777215))
            line2 = Line(self.scrollAreaContents)

            pDetail = DetailsButton(self.scrollAreaContents)
            pDetail.setObjectName(u"p"+str(i)+"details")

            # Layout Header
            pHeaderLayout = QHBoxLayout()
            pHeaderLayout.setObjectName(u"p0HeaderLayout")
            pHeaderLayout.addWidget(pTitle)
            pHeaderLayout.addWidget(line1)
            pHeaderLayout.addWidget(pRecom)
            pHeaderLayout.addWidget(line2)
            pHeaderLayout.addWidget(pDetail)

            # Layout profile
            pLayout = QVBoxLayout()
            pLayout.setObjectName(u"p"+str(i)+"Layout")
            pLayout.addLayout(pHeaderLayout)
            self.profileInfos.append(None)
            pLayout.setStretch(1, 1)

            self.profileTitles.append(pTitle)
            self.profileRecoms.append(pRecom)
            self.profileDetails.append(pDetail)
            self.profiles.append(pLayout)

            self.profileGroup.addButton(pTitle)
            self.profileGroup.setId(pTitle, i)
            self.profDetGroup.addButton(pDetail)
            self.profDetGroup.setId(pDetail, i)

        self.profileTitles[1].setChecked(True)

        # Layout scroll area contents
        verticalLayout_9 = QVBoxLayout()
        verticalLayout_9.setSpacing(10)
        verticalLayout_9.setObjectName(u"verticalLayout_9")
        verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        verticalLayout_9.addLayout(self.profiles[0])
        verticalLayout_9.addLayout(self.profiles[1])
        verticalLayout_9.addLayout(self.profiles[2])
        verticalLayout_9.addLayout(self.profiles[3])

        # Layout step 2
        profilesLayout = QVBoxLayout()
        profilesLayout.setSpacing(10)
        profilesLayout.setObjectName(u"profilesLayout")
        profilesLayout.setContentsMargins(10, 10, 10, 20)
        profilesLayout.addWidget(self.profilesLabel)
        profilesLayout.addLayout(verticalLayout_9)

        # Create step 3 (representations)
        self.repsLabel = QLabel(self.scrollAreaContents)
        self.repsLabel.setObjectName(u"repsLabel")
        self.repsLabel.setFont(font12)
        self.repsLabel.setWordWrap(True)

        self.repLayoutV = QVBoxLayout()
        self.repLayoutV.setSpacing(0)
        self.repLayoutV.setObjectName(u"repLayoutV")
        self.repLayoutV.setContentsMargins(0, 0, 0, 0)
        self.repLayoutV.setSpacing(10)

        self.repsGroup.setParent(self.scrollAreaContents)
        self.repsDetGroup.setParent(self.scrollAreaContents)

        # Layout step 3
        repsLayout = QVBoxLayout()
        repsLayout.setSpacing(10)
        repsLayout.setObjectName(u"repsLayout")
        repsLayout.setContentsMargins(10, 10, 10, 10)
        repsLayout.addWidget(self.repsLabel)
        repsLayout.addLayout(self.repLayoutV)

        # Layout all content items
        contentLayoutV.addWidget(self.stepHeaders[0])
        contentLayoutV.addLayout(fileSpinnerLayoutH)
        contentLayoutV.addWidget(self.stepHeaders[1])
        contentLayoutV.addLayout(profilesLayout)
        contentLayoutV.addWidget(self.stepHeaders[2])
        contentLayoutV.addLayout(repsLayout)
        contentLayoutV.addItem(QSpacerItem(17, 34, QSizePolicy.Minimum, QSizePolicy.Expanding))
        scrollArea.setWidget(self.scrollAreaContents)
        scrollLayout.addWidget(scrollArea, 0, 0, 1, 1)

        # Construct info page and stackedWidget
        page = QWidget()
        page.setObjectName("info")
        self.infopage = QTextBrowser(page)
        self.infopage.setObjectName("infoTextBrowser"+str(i+1))
        self.infopage.setFont(font12)
        self.infopage.setTextInteractionFlags(
            Qt.LinksAccessibleByKeyboard |
            Qt.LinksAccessibleByMouse |
            Qt.TextBrowserInteraction |
            Qt.TextSelectableByKeyboard |
            Qt.TextSelectableByMouse)
        vl = QVBoxLayout(page)
        vl.setSpacing(0)
        vl.setObjectName("verticalLayout_6")
        vl.setContentsMargins(0, 0, 0, 0)
        vl.addWidget(self.infopage)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font12)
        self.stackedWidget.addWidget(content)
        self.stackedWidget.addWidget(page)
        self.stackedWidget.setCurrentIndex(0)

        # Layout left side of the application
        leftLayout = QVBoxLayout()
        leftLayout.setSpacing(0)
        leftLayout.setObjectName(u"leftLayout")
        leftLayout.addLayout(menuLayout)
        leftLayout.addWidget(self.stackedWidget)

        # Create overview (right side of the application)
        overviewFrame = QFrame(self.centralwidget)
        overviewFrame.setObjectName(u"overviewFrame")
        overviewFrame.setMinimumSize(QSize(160, 0))
        overviewFrame.setMaximumSize(QSize(250, 16777215))
        overviewFrame.setStyleSheet(u"QFrame{\n"
                                        "    border-radius: 0;\n"
                                        "    border: 1px solid "+lwl_darkred+"\n"
                                        "}")
        overviewFrame.setFrameShape(QFrame.StyledPanel)
        overviewFrame.setFrameShadow(QFrame.Raised)
        
        # Title
        self.ovTitle = QWidget(overviewFrame)
        self.ovTitle.setObjectName(u"ovTitle")
        self.ovTitle.setMinimumSize(QSize(0, 20))
        self.label_3 = QLabel(self.ovTitle)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(130, 0))
        self.label_3.setMaximumSize(QSize(130, 16777215))
        self.label_3.setFont(font16)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u".QLabel{\n"
                                    "    border-radius: 5px;\n"
                                    "    border: none;\n"
                                    "    background-color: "+lwl_darkblue+";\n"
                                    "    color: #ffffff\n"
                                    "}")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.horizontalLayout = QHBoxLayout(self.ovTitle)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.addWidget(self.label_3)

        # Text browser
        self.ieTextBrowser = OverviewTextBrowser(overviewFrame, "ieTextBrowser")
        self.profileTextBrowser = OverviewTextBrowser(overviewFrame, "profileTextBrowser")
        self.profileTextBrowser.setMaximumSize(QSize(16777215, 50))
        self.repTextBrowser = OverviewTextBrowser(overviewFrame, "repTextBrowser")

        # Delivery box
        self.label = QLabel(overviewFrame)
        self.label.setObjectName(u"label")
        self.label.setFont(font12b)
        self.label.setStyleSheet(u"QLabel{border: none}")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setMargin(4)
        self.label.setIndent(1)

        self.btnViewer = OverviewRadioBtn(overviewFrame, "btnViewer")
        self.btnViewer.setChecked(True)
        self.btnDownload = OverviewRadioBtn(overviewFrame, "btnDownload")
        self.btnBoth = OverviewRadioBtn(overviewFrame, "btnBoth")

        self.overviewGroup.setParent(overviewFrame)
        self.overviewGroup.addButton(self.btnViewer)
        self.overviewGroup.setId(self.btnViewer, 0)
        self.overviewGroup.addButton(self.btnDownload)
        self.overviewGroup.setId(self.btnDownload, 1)
        self.overviewGroup.addButton(self.btnBoth)
        self.overviewGroup.setId(self.btnBoth, 2)

        deliveryButtonsLayout = QVBoxLayout()
        deliveryButtonsLayout.setSpacing(0)
        deliveryButtonsLayout.setObjectName(u"deliveryButtonsLayout")
        deliveryButtonsLayout.setContentsMargins(30, -1, -1, -1)
        deliveryButtonsLayout.addWidget(self.btnViewer)
        deliveryButtonsLayout.addWidget(self.btnDownload)
        deliveryButtonsLayout.addWidget(self.btnBoth)

        deliveryLayout = QVBoxLayout()
        deliveryLayout.setObjectName(u"deliveryLayout")
        deliveryLayout.addWidget(self.label)
        deliveryLayout.addLayout(deliveryButtonsLayout)

        # Request button
        self.goButton = LabelButton(overviewFrame)
        self.goButton.setObjectName(u"goButton")
        self.goButton.setMinimumSize(QSize(60, 0))
        self.goButton.setMaximumSize(QSize(60, 16777215))
        self.goButton.setFont(font12b)

        self.ovButtonLayout = QHBoxLayout()
        self.ovButtonLayout.setObjectName(u"ovButtonLayout")
        self.ovButtonLayout.setContentsMargins(-1, -1, 20, -1)
        self.ovButtonLayout.addItem(QSpacerItem(94, 17, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.ovButtonLayout.addWidget(self.goButton)

        # Layout overview
        verticalLayout = QVBoxLayout(overviewFrame)
        verticalLayout.setSpacing(0)
        verticalLayout.setObjectName(u"verticalLayout")
        verticalLayout.addWidget(self.ovTitle)
        verticalLayout.addItem(QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed))
        verticalLayout.addWidget(self.ieTextBrowser)
        verticalLayout.addWidget(self.profileTextBrowser)
        verticalLayout.addWidget(self.repTextBrowser)
        verticalLayout.addLayout(deliveryLayout)
        verticalLayout.addItem(QSpacerItem(17, 37, QSizePolicy.Minimum, QSizePolicy.Expanding))
        verticalLayout.addLayout(self.ovButtonLayout)
        verticalLayout.setStretch(2, 2)
        verticalLayout.setStretch(4, 1)

        # Layout central widget / window
        centralWidgetLayoutH = QHBoxLayout(self.centralwidget)
        centralWidgetLayoutH.setSpacing(0)
        centralWidgetLayoutH.setObjectName(u"centralWidgetLayoutH")
        centralWidgetLayoutH.setContentsMargins(0, 0, 0, 0)
        centralWidgetLayoutH.addLayout(leftLayout)
        centralWidgetLayoutH.addWidget(overviewFrame)

        self.setCentralWidget(self.centralwidget)
        statusbar = QStatusBar(self)
        statusbar.setObjectName(u"statusbar")
        statusbar.setEnabled(True)
        statusbar.setStyleSheet("QStatusBar{background-color: "+lwl_lightgray+"}")
        self.setStatusBar(statusbar)
    # setupUi

    def createAIP(self, vl, parent, index_):
        aiptitle = LabelButton(parent)
        aiptitle.setObjectName(u"aiptitle")
        aiptitle.setMinimumSize(QSize(60, 17))
        aiptitle.setMaximumSize(QSize(70, 100))

        aipname = QLabel(parent)
        aipname.setObjectName(u"aipname")
        aipname.setFont(font12)
        aipname.setAlignment(Qt.AlignCenter)

        aipformats = QLabel(parent)
        aipformats.setObjectName(u"aipformats")
        aipformats.setFont(font12)
        aipformats.setAlignment(Qt.AlignCenter)

        line1 = Line(parent, max_=QSize(30, 16777215))
        line2 = Line(parent)
        line3 = Line(parent, max_=QSize(30, 16777215))

        aipdetails = DetailsButton(parent)

        # Layout AIP-Header
        aipHeaderLayout = QHBoxLayout()
        aipHeaderLayout.setObjectName(u"aipHeaderLayout")
        aipHeaderLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        aipHeaderLayout.addWidget(aiptitle)
        aipHeaderLayout.addWidget(line1)
        aipHeaderLayout.addWidget(aipname)
        aipHeaderLayout.addWidget(line2)
        aipHeaderLayout.addWidget(aipformats)
        aipHeaderLayout.addWidget(line3)
        aipHeaderLayout.addWidget(aipdetails)
        aipHeaderLayout.setSpacing(10)

        #Layout AIP
        aipLayout = QVBoxLayout()
        aipLayout.setSpacing(10)
        aipLayout.setObjectName(u"aipLayout")
        aipLayout.addLayout(aipHeaderLayout)
        self.aipInfos.append(None)
        aipLayout.setStretch(1, 1)
        vl.addLayout(aipLayout)

        self.aipTitles.append(aiptitle)
        self.aipDescs.append(aipname)
        self.aipFormats.append(aipformats)
        self.aipDetails.append(aipdetails)
        self.aips.append(aipLayout)

        self.repsGroup.addButton(aiptitle)
        self.repsGroup.setId(aiptitle, index_)
        self.repsDetGroup.addButton(aipdetails)
        self.repsDetGroup.setId(aipdetails, index_)

    def closeAips(self):
        for i in range(len(self.aipInfos)):
            if not self.aipInfos[i]:
                continue
            tb = self.aipInfos[i]
            self.aipInfos[i] = None
            tb.close()

        for r in self.aips:
            header = r.children()[0]
            for i in reversed(range(header.count())):
                widget = header.itemAt(i).widget()
                widget.close()
            self.repLayoutV.removeItem(r)

        self.aips = []
        self.aipDetails = []
        self.aipDescs = []
        self.aipTitles = []
        self.aipFormats = []

    def createitb(self, parent, layout, type_, index_, infotexts):
        info = InfoTextBrowser(parent)
        if type_ == "a":
            info.setHtml(self.utp.constructRepItb(infotexts["date"], infotexts["files"]))
            self.aipInfos[index_] = info
        elif type_ == "p":
            info.setHtml(self.utp.constructProfileItb(infotexts))
            self.profileInfos[index_] = info
        layout.addWidget(info)

    def retranslateAips(self, formats):
        self.repsLabel.setText(QCoreApplication.translate("self", snippets.repLabel, None))

        for i in range(len(self.aips)):
            self.aipTitles[i].setText(QCoreApplication.translate("self", snippets.AIP + " " + str(i), None))
            if i == 0:
                self.aipDescs[i].setText(QCoreApplication.translate("self", snippets.root, None))
            else:
                self.aipDescs[i].setText(QCoreApplication.translate("self", snippets.rep, None))
            self.aipFormats[i].setText(QCoreApplication.translate("self", ", ".join(formats[i]), None))
            self.aipDetails[i].setText(QCoreApplication.translate("self", snippets.details, None))

    def retranslateProfiles(self, nos, titles, recoms, infos=None):
        self.profilesLabel.setText(QCoreApplication.translate("self", snippets.profLabel, None))

        for i in range(self.pn):
            self.profileTitles[i].setText(
                QCoreApplication.translate("self", snippets.profile + " " + str(nos[i]) + " - " + titles[i], None))
            self.profileRecoms[i].setText(QCoreApplication.translate("self", recoms[i], None))
            self.profileDetails[i].setText(QCoreApplication.translate("self", snippets.details, None))

    def setInfoPage(self, info):
        self.infopage.setHtml(self.utp.constructItb(info))
        self.stackedWidget.setCurrentIndex(1)

    def retranslateBaseUi(self):
        self.setWindowTitle(QCoreApplication.translate("self", snippets.windowTitle, None))

        for i in range(4):
            self.menuButtons[i].setStatusTip(QCoreApplication.translate("self", snippets.menuStatuses[i], None))
            self.menuButtons[i].setText(QCoreApplication.translate("self", snippets.menuTitles[i], None))

        for i in range(3):
            self.stepTitles[i].setText(QCoreApplication.translate("self", snippets.stepTitles[i], None))
            self.steps[i].setText(QCoreApplication.translate("self", snippets.step + " " + str(i+1), None))
            self.stepInfos[i].setToolTip(QCoreApplication.translate("self", snippets.help, None))

        self.infopage.setHtml(QCoreApplication.translate("self", snippets.infoTexts[0], None))

        self.aipFileSpinner.setPlaceholderText(QCoreApplication.translate("self", snippets.spinnerPh[0], None))
        self.vzeFileSpinner.setPlaceholderText(QCoreApplication.translate("self", snippets.spinnerPh[1], None))
        self.aipFileSpinner.setToolTip(
            QCoreApplication.translate("self", snippets.spinnerTooltip[0], None),
            QCoreApplication.translate("self", snippets.spinnerTooltip[1], None)
        )
        self.vzeFileSpinner.setToolTip(QCoreApplication.translate("self", snippets.spinnerTooltip[2], None))
        self.spinnerGoBtn.setToolTip(QCoreApplication.translate("self", snippets.spinnerTooltip[3], None))
        self.spinnerGoBtn.setStatusTip(QCoreApplication.translate("self", snippets.spinnerTooltip[3], None))

        self.label_3.setText(QCoreApplication.translate("self", snippets.choice, None))
        self.ieTextBrowser.setHtml(QCoreApplication.translate("self", snippets.overviewTexts[0], None))
        self.profileTextBrowser.setHtml(QCoreApplication.translate("self", snippets.overviewTexts[1], None))
        self.repTextBrowser.setHtml(QCoreApplication.translate("self", snippets.overviewTexts[2], None))

        self.label.setText(QCoreApplication.translate("self", snippets.deliv, None))
        self.btnViewer.setToolTip("")
        self.btnViewer.setText(QCoreApplication.translate("self", snippets.overviewBtns[0], None))
        self.btnDownload.setToolTip("")
        self.btnDownload.setText(QCoreApplication.translate("self", snippets.overviewBtns[1], None))
        self.btnBoth.setToolTip("")
        self.btnBoth.setText(QCoreApplication.translate("self", snippets.overviewBtns[2], None))
        self.goButton.setStatusTip(QCoreApplication.translate("self", snippets.goStatus, None))
        self.goButton.setText(QCoreApplication.translate("self", snippets.go, None))
    # retranslateUi


class MenuButton(QPushButton):
    def __init__(self, parent, objectName, checked):
        super().__init__(parent)
        self.setObjectName(objectName)
        self.setMinimumSize(QSize(0, 21))
        self.setMaximumSize(QSize(16777215, 21))
        self.setFont(font12)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setAutoFillBackground(False)
        self.setStyleSheet(u"QPushButton{\n" \
                        "    background-color: " + lwl_darkblue + ";\n" \
                        "    border: 1px solid " + lwl_darkblue + ";\n" \
                        "    color: #ffffff;\n" \
                        "}\n" \
                        "\n" \
                        "QPushButton:hover{\n" \
                        "    background-color: " + lwl_darkred + "\n" \
                        "}\n" \
                        "\n" \
                        "QPushButton:checked{\n" \
                        "    background-color: " + lwl_darkred + ";\n" \
                        "    border: 1px solid " + lwl_darkred + "\n" \
                        "}")
        self.setCheckable(True)
        self.setChecked(checked)
        self.setFlat(False)


class FileSpinner:
    def __init__(self, parent, type_):
        self.type_ = type_
        self.paths = None

        self.edit = QLineEdit(parent)
        self.edit.setObjectName(u"aipfs")
        self.edit.setClearButtonEnabled(True)
        self.edit.textChanged.connect(self.update)

        self.btn = QToolButton(parent)
        self.btn.setObjectName(u"fsbtn")
        self.btn.setMinimumSize(QSize(30, 30))
        self.btn.setMaximumSize(QSize(30, 30))
        self.btn.setIcon(icon_file)
        self.btn.clicked.connect(self.getpath)

        self.btndir = None
        if type_ == "a":
            self.btndir = QToolButton(parent)
            self.btndir.setObjectName(u"fsdbtn")
            self.btndir.setMinimumSize(QSize(30, 30))
            self.btndir.setMaximumSize(QSize(30, 30))
            self.btndir.setIcon(icon_directory)
            self.btndir.clicked.connect(self.getdirpath)

    def update(self, text):
        if text == "":
            self.paths = None
        elif str.startswith(text, "[") and str.endswith(text, "]"):
            self.paths = ast.literal_eval(text)
        else:
            self.paths = text

    def getdirpath(self):
        self.getpath("dir")

    def getpath(self, filemode=None):
        dialog = QFileDialog()
        dialog.setViewMode(QFileDialog.Detail)
        if filemode == "dir":
            dialog.setFileMode(QFileDialog.Directory)
        elif self.type_ == "v":
            dialog.setFileMode(QFileDialog.ExistingFile)
            dialog.setNameFilter("XML files (*.xml)")
        else:
            dialog.setFileMode(QFileDialog.ExistingFiles)

        if dialog.exec_():
            if filemode == "dir" or self.type_ == "v":
                self.paths = dialog.selectedFiles()[0]
                self.edit.setText(self.paths)
            else:
                self.paths = dialog.selectedFiles()
                if len(self.paths) > 1:
                    self.edit.setText(str(self.paths))
                else:
                    self.edit.setText(self.paths[0])

    def setToolTip(self, text1, text2=None):
        self.btn.setToolTip(text1)
        if text2 and self.btndir:
            self.btndir.setToolTip(text2)

    def setPlaceholderText(self, text):
        self.edit.setPlaceholderText(text)

    def addToLayout(self, layout):
        layout.addWidget(self.edit)
        layout.addWidget(self.btn)
        if self.btndir:
            layout.addWidget(self.btndir)


class OverviewTextBrowser(QTextBrowser):

    def __init__(self, parent, objectName):
        super().__init__(parent)
        self.setObjectName(objectName)
        self.setMinimumSize(QSize(160, 20))
        self.setMaximumSize(QSize(250, 16777215))
        self.setFont(font12)
        self.setStyleSheet(u"QTextBrowser{border: none}")
        self.setFrameShape(QFrame.NoFrame)
        self.setFrameShadow(QFrame.Plain)


class InfoTextBrowser(QTextBrowser):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName(u"Info")
        self.setFont(font12)
        self.setFrameShape(QFrame.NoFrame)
        self.setFrameShadow(QFrame.Plain)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTextInteractionFlags(
            Qt.LinksAccessibleByKeyboard |
            Qt.LinksAccessibleByMouse |
            Qt.TextBrowserInteraction |
            Qt.TextSelectableByKeyboard |
            Qt.TextSelectableByMouse)


class OverviewRadioBtn(QRadioButton):

    def __init__(self, parent, objectName):
        super().__init__(parent)
        self.setObjectName(objectName)
        self.setMinimumSize(QSize(70, 20))
        self.setMaximumSize(QSize(16777215, 20))
        self.setFont(font12)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet(u"QRadioButton{\n"
                                   "    margin-left: 3px\n"
                                   "}\n"
                                   "QRadioButton::indicator {\n"
                                   "    background-color: #ffffff;\n"
                                   "    width: 11px;\n"
                                   "    height: 11px;\n"
                                   "    border-radius: 6px;\n"
                                   "    border: 1px solid black;\n"
                                   "}\n"
                                   "\n"
                                   "QRadioButton::indicator:checked {\n"
                                   "    width: 9px;\n"
                                   "    height: 9px;\n"
                                   "    border-radius: 6px;\n"
                                   "    background-color: #ffffff;\n"
                                   "    border: 3px solid "+lwl_darkred+";\n"
                                   "}\n"
                                   "\n"
                                   "QRadioButton::indicator:unchecked:hover {\n"
                                   "    border: 1px solid "+lwl_darkred+";\n"
                                   "}")
        self.setIconSize(QSize(12, 12))
        self.setChecked(False)


class DetailsButton(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName(u"btndetails")
        self.setMinimumSize(QSize(60, 18))
        self.setMaximumSize(QSize(80, 100))
        self.setFont(font12)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setAutoFillBackground(False)
        self.setStyleSheet(u"QPushButton{\n"
                            "	background-color: " + lwl_middlegray + ";\n"
                            "     border-radius: 5px;\n"
                            "     padding: 1px 3px\n"
                            "}\n"
                            "\n"
                            "QPushButton:active{\n"
                            "	background-color: " + lwl_lightgray + ";\n"
                            "     border: 1px solid " + lwl_darkblue + "\n"
                            "}\n"
                            "\n"
                            "QPushButton:active:hover{\n"
                            "     border: 1px solid " + lwl_darkred + ";\n"
                            "}")
        self.setIcon(icon_link)
        self.setIconSize(QSize(11, 11))
        self.setCheckable(True)
        self.setChecked(False)


class LabelButton(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName(u"btnlabel")
        self.setFont(font12)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setAutoFillBackground(False)
        self.setStyleSheet(u"QPushButton{\n"
                            "	background-color: " + lwl_middlegray + ";\n"
                            "     border-radius: 5px;\n"
                            "	padding: 3px 10px\n"
                            "}\n"
                            "\n"
                            "QPushButton:active{\n"
                            "	background-color: " + lwl_lightgray + ";\n"
                            "     border: 1px solid " + lwl_darkblue + "\n"
                            "}\n"
                            "\n"
                            "QPushButton:active:hover{\n"
                            "     border: 1px solid " + lwl_darkred + ";\n"
                            "}\n"
                            "\n"
                            "QPushButton:checked{\n"
                            "	background-color: " + lwl_darkred + ";\n"
                            "	color: rgb(255, 255, 255);\n"
                            "     border: none;\n"
                            "}")
        self.setCheckable(True)
        self.setChecked(False)


class Line(QFrame):
    def __init__(self, parent, min_=QSize(0, 0), max_=QSize(16777215, 16777215)):
        super().__init__(parent)
        self.setObjectName(u"line_11")
        self.setMinimumSize(min_)
        self.setMaximumSize(max_)
        self.setLineWidth(2)
        self.setFrameShape(QFrame.HLine)
