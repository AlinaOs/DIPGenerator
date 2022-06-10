import ast
from enum import Enum

import PySide6
from PySide6 import QtCore
from PySide6.QtCore import (QRect, QSize, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QCursor,
                           QFont, QIcon, QPalette, QPixmap, QResizeEvent, QMouseEvent)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                               QLayout, QMainWindow, QPushButton, QRadioButton,
                               QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
                               QStatusBar, QTextBrowser, QVBoxLayout, QWidget,
                               QLineEdit, QToolButton, QFileDialog, QButtonGroup,
                               QAbstractScrollArea, QGridLayout, QDialog, QDialogButtonBox)

from drh.err import DrhError
from rv.snippets import UiTextProvider


####################
# Design constants
####################

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
font12b.setWeight(QFont.Weight.DemiBold)

font14 = QFont()
font14.setFamilies(["Source Sans Pro"])
font14.setPointSize(14)

font16 = QFont()
font16.setFamilies(["Source Sans Pro"])
font16.setPointSize(16)

icon_DIP = QIcon()  # https://www.iconshock.com/freeicons/package-16
icon_DIP.addFile("svg/Package.svg", QSize(), QIcon.Normal, QIcon.Off)
icon_info = QIcon()
icon_info.addFile("svg/LWL_mehr_Infos.svg", QSize(), QIcon.Normal, QIcon.Off)
icon_check_url = "svg/Check.svg"
icon_check = QIcon()  # https://www.iconshock.com/freeicons/check-circle-fill-24
icon_check.addFile(icon_check_url, QSize(), QIcon.Normal, QIcon.Off)
icon_check_pm = None
icon_link_up = QIcon()
icon_link_up.addFile("svg/LWL_Link_up.svg", QSize(), QIcon.Normal, QIcon.Off)
icon_link_down = QIcon()
icon_link_down.addFile("svg/LWL_Link_down.svg", QSize(), QIcon.Normal, QIcon.Off)
icon_directory = QIcon()
icon_directory.addFile("svg/Directory.svg", QSize(), QIcon.Normal, QIcon.Off)
icon_file = QIcon()
icon_file.addFile("svg/LWL_Dokument.svg", QSize(), QIcon.Normal, QIcon.Off)
icon_problem_url = "svg/LWL_Fehler_melden.svg"
icon_problem = QIcon()
icon_problem.addFile(icon_problem_url, QSize(), QIcon.Normal, QIcon.Off)
icon_problem_red_url = "svg/LWL_Fehler_melden_rot.svg"
icon_problem_red = QIcon()
icon_problem_red.addFile(icon_problem_red_url, QSize(), QIcon.Normal, QIcon.Off)


#################
# Custom widgets
#################


class LabelButton(QPushButton):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.setFont(font12)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setAutoFillBackground(False)
        self._stsh = u"QPushButton{\n"\
                    "	background-color: " + white + ";\n"\
                    "   border-radius: 5px;\n"\
                    "	padding: 3px 10px;\n"\
                    "	font: " + lwl_middlegray +";\n"\
                    "}\n"\
                    "\n"\
                    "QPushButton:active{\n"\
                    "	background-color: " + lwl_lightgray + ";\n"\
                    "     border: 1px solid " + lwl_darkblue + "\n"\
                    "}\n"\
                    "\n"\
                    "QPushButton:active:hover{\n"\
                    "     border: 1px solid " + lwl_darkred + ";\n"\
                    "}\n"\
                    "\n"\
                    "QPushButton:checked{\n"\
                    "	background-color: " + lwl_darkred + ";\n"\
                    "	color: rgb(255, 255, 255);\n"\
                    "     border: none;\n"\
                    "}"
        self.setStyleSheet(self._stsh)
        self.setCheckable(True)
        self.setChecked(False)
        self._highlighted = False
        self._pseudoenabled = True

    def enable(self, enabled):
        self.setEnabled(enabled)
        if enabled:
            self._pseudoenabled = False
            self.setCursor(QCursor(Qt.PointingHandCursor))
        else:
            self._pseudoenabled = False
            self.setCursor(QCursor(Qt.ArrowCursor))

    def pseudoenable(self) -> None:
        self.enable(True)
        self._pseudoenabled = True

    def ispseudoenabled(self) -> bool:
        return self._pseudoenabled

    def setBoxHighlighting(self, highlight: bool) -> None:
        self._highlighted = highlight
        if highlight:
            self.setStyleSheet(self._stsh + "QPushButton:active{border: 2px solid " + lwl_darkred + ";}")
        else:
            self.setStyleSheet(self._stsh)


class MenuButton(QPushButton):
    def __init__(self, parent: QWidget, checked: bool):
        super().__init__(parent)
        self.setMinimumSize(QSize(0, 21))
        self.setMaximumSize(QSize(16777215, 21))
        self.setFont(font12)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setAutoFillBackground(False)
        self.setStyleSheet(u"QPushButton{\n"
                           "    background-color: " + lwl_darkblue + ";\n"
                           "    border: 1px solid " + lwl_darkblue + ";\n"
                           "    color: #ffffff;\n"
                           "}\n"
                           "\n"
                           "QPushButton:hover{\n"
                           "    background-color: " + lwl_darkred + "\n"
                           "}\n"
                           "\n"
                           "QPushButton:checked{\n"
                           "    background-color: " + lwl_darkred + ";\n"
                           "    border: 1px solid " + lwl_darkred + "\n"
                           "}")
        self.setCheckable(True)
        self.setChecked(checked)
        self.setFlat(False)


class DetailsButton(QPushButton):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.setMinimumSize(QSize(60, 18))
        self.setMaximumSize(QSize(80, 100))
        self.setFont(font12)
        self.setIcon(icon_link_down)
        self.setIconSize(QSize(16, 16))
        self.clicked.connect(self._toggleicon)
        self._on = False

    def _toggleicon(self) -> None:
        if self._on:
            self.setIcon(icon_link_down)
        else:
            self.setIcon(icon_link_up)
        self._on = not self._on


class ToolButton(QToolButton):
    def __init__(self,
                 parent: QWidget,
                 icon: QIcon = None,
                 iconsize: QSize = None,
                 min_: QSize = None,
                 max_: QSize = None):
        super().__init__(parent)
        if min_:
            self.setMinimumSize(min_)
        if max_:
            self.setMaximumSize(max_)
        self.radius = 5
        if icon:
            self.setIcon(icon)
            self.setIconSize(iconsize)
            self.radius = iconsize.width()/2
            self.setStyleSheet("QToolButton{border-radius: "+str(self.radius)+"px}")
            self.setCursor(QCursor(Qt.PointingHandCursor))
        self._highlighted = False
        self._pseudoenabled = False

    def enable(self, enabled: bool) -> None:
        self.setEnabled(enabled)
        if enabled:
            self._pseudoenabled = False
        else:
            self._pseudoenabled = False

    def pseudoenable(self) -> None:
        self.enable(True)
        self._pseudoenabled = True

    def ispseudoenabled(self) -> bool:
        return self._pseudoenabled

    def setBoxHighlighting(self, highlight: bool) -> None:
        self._highlighted = highlight
        if highlight:
            self.setStyleSheet(
                "QToolButton{"
                "border: 2px solid " + lwl_darkred + ";"
                "border-radius: "+str(self.radius)+"px;"
                "}")
        else:
            if self.icon():
                self.setStyleSheet(
                    "QToolButton{"
                    "border-radius: "+str(self.radius)+"px;"
                    "}")
            else:
                self.setStyleSheet("")


class OverviewRadioBtn(QRadioButton):

    def __init__(self, parent: QWidget):
        super().__init__(parent)
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
                           "QRadioButton::indicator:active:checked {\n"
                           "    width: 9px;\n"
                           "    height: 9px;\n"
                           "    border-radius: 6px;\n"
                           "    background-color: #ffffff;\n"
                           "    border: 3px solid " + lwl_darkred + ";\n"
                            "}\n"
                            "\n"
                            "QRadioButton::indicator:unchecked:active:hover {\n"
                            "    border: 1px solid " + lwl_darkred + ";\n"
                            "}\n"
                             "QRadioButton:inactive {\n"
                             "    font: " + lwl_middlegray + ";\n"
                             "}"
                           )
        self.setIconSize(QSize(12, 12))
        self.setChecked(False)

    def enable(self, enabled: bool, tooltip: str = ""):
        self.setEnabled(enabled)
        if enabled:
            self.setCursor(QCursor(Qt.PointingHandCursor))
            self.setToolTip("")
        else:
            self.setCursor(QCursor(Qt.ArrowCursor))
            self.setToolTip(tooltip)


class Line(QFrame):
    def __init__(self, parent: QWidget,
                 min_: QSize = QSize(0, 0),
                 max_: QSize = QSize(16777215, 16777215)):
        super().__init__(parent)
        self.setMinimumSize(min_)
        self.setMaximumSize(max_)
        self.setLineWidth(2)
        self.setFrameShape(QFrame.HLine)
        self.setStyleSheet("QFrame:inactive{border: 2px solid " + lwl_middlegray + ";}")


class OverviewTextBrowser(QTextBrowser):

    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.setMinimumSize(QSize(160, 20))
        self.setMaximumSize(QSize(250, 16777215))
        self.setFont(font12)
        self.setStyleSheet(u"QTextBrowser{border: none}")
        self.setFrameShape(QFrame.NoFrame)
        self.setFrameShadow(QFrame.Plain)


class InfoTextBrowser(QTextBrowser):
    def __init__(self, parent: QWidget, width: int):
        super().__init__(parent)
        self._fwidth = width
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

    def minimumSizeHint(self) -> QSize:
        doc = self.document().clone()
        doc.setTextWidth(self._fwidth)
        height = doc.size().height()
        height += self.frameWidth() * 2
        return QSize(self.viewport().width(), height)

    def sizeHint(self) -> QSize:
        return self.minimumSizeHint()

    def setfwidth(self, w: int) -> None:
        self._fwidth = w
        self.updateGeometry()


class ClickableLineEdit(QLineEdit):
    clicked = Signal()

    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.setClearButtonEnabled(True)
        self.setMinimumSize(QSize(50, 25))
        self.setFont(font12)
        self.textChanged.connect(self.update)

    def mousePressEvent(self, e: QMouseEvent):
        self.clicked.emit()


class FileSpinner:
    def __init__(self, parent: QWidget, type_: str):
        self._type = type_
        self._highlighted = False
        self.paths = None

        self.edit = ClickableLineEdit(parent)
        self.edit.textChanged.connect(self.update)
        if type_ == "o":
            self.edit.clicked.connect(self._getdirpath)
        else:
            self.edit.clicked.connect(self._getpath)

        self.btn = None
        if type_ != "o":
            self.btn = ToolButton(parent, icon_file, QSize(20, 20), QSize(30, 30), QSize(30, 30))
            self.btn.clicked.connect(self._getpath)

        self.btndir = None
        if type_ != "v":
            self.btndir = ToolButton(parent, icon_directory, QSize(20, 20), QSize(30, 30), QSize(30, 30))
            self.btndir.clicked.connect(self._getdirpath)

    def update(self, text: str)-> None:
        if text == "":
            self.paths = None
            if self._highlighted:
                self.edit.setStyleSheet("border: 2px solid " + lwl_darkred + ";")
        elif str.startswith(text, "[") and str.endswith(text, "]"):
            self.paths = ast.literal_eval(text)
            self.edit.setStyleSheet("")
        else:
            self.paths = text
            self.edit.setStyleSheet("")

    def _getdirpath(self) -> None:
        self._getpath("dir")

    def _getpath(self, filemode: str = None) -> None:
        dialog = QFileDialog()
        dialog.setViewMode(QFileDialog.Detail)
        if filemode == "dir":
            dialog.setFileMode(QFileDialog.Directory)
            dialog.setWindowIcon(icon_directory)
        elif self._type == "v":
            dialog.setFileMode(QFileDialog.ExistingFile)
            dialog.setNameFilter("XML files (*.xml)")
            dialog.setWindowIcon(icon_file)
        else:
            dialog.setFileMode(QFileDialog.ExistingFiles)
            dialog.setNameFilter("TAR files (*.tar)")
            dialog.setWindowIcon(icon_file)

        if dialog.exec_():
            if filemode == "dir" or self._type == "v":
                self.edit.setText(dialog.selectedFiles()[0])
                self.paths = dialog.selectedFiles()[0]
            else:
                if len(dialog.selectedFiles()) > 1:
                    self.edit.setText(str(dialog.selectedFiles()))
                else:
                    self.edit.setText(dialog.selectedFiles()[0])
                self.paths = dialog.selectedFiles()

    def setToolTip(self, text1: str, text2: str = None) -> None:
        if self.btn:
            self.btn.setToolTip(text1)
        else:
            self.btndir.setToolTip(text1)
        if text2 and self.btndir:
            self.btndir.setToolTip(text2)

    def setPlaceholderText(self, text: str) -> None:
        self.edit.setPlaceholderText(text)

    def addToLayout(self, layout: QLayout) -> None:
        layout.addWidget(self.edit)
        if self.btn:
            layout.addWidget(self.btn)
        if self.btndir:
            layout.addWidget(self.btndir)

    def setBoxHighlighting(self, highlight: bool) -> None:
        self._highlighted = highlight
        if highlight:
            self.edit.setStyleSheet("QLineEdit{border: 2px solid " + lwl_darkred + ";}")
        else:
            self.edit.setStyleSheet("")


class MsgType(Enum):
    SUCCESS = 0
    WARNING = 1
    ERROR = 2
    ANY = 3


class MsgTrigger(Enum):
    LOAD = 0
    REQUEST = 1
    GOBTN = 2


class MessageBox(QDialog):
    def __init__(self,
                 parent: QWidget,
                 type_: MsgType,
                 trigger: MsgTrigger,
                 texts: str,
                 details: list[str] | list[DrhError] = None):
        super().__init__(parent)
        self._type = type_
        self._trigger = trigger
        self._details = details
        self._utp = UiTextProvider(texts)

        self.resize(390, 405)
        self.setFont(font12)
        if self._type == MsgType.SUCCESS:
            self.setWindowIcon(icon_check)
            self.iconurl = icon_check_url
        elif self._type == MsgType.WARNING:
            self.setWindowIcon(icon_problem)
            self.iconurl = icon_problem_url
        elif self._type == MsgType.ERROR:
            self.setWindowIcon(icon_problem_red)
            self.iconurl = icon_problem_red_url
        else:
            self.setWindowIcon(icon_problem)
            self.iconurl = icon_problem_url
        self.setSizeGripEnabled(True)
        self.setModal(True)
        self.setWindowModality(Qt.ApplicationModal)

        self.title = QLabel(self)
        self.title.setFont(font12b)
        horizontalLayout_2 = QHBoxLayout()
        horizontalLayout_2.setSpacing(0)
        horizontalLayout_2.addItem(QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum))
        horizontalLayout_2.addWidget(self.title)

        self.icon = QLabel(self)
        self.icon.setMaximumSize(QSize(30, 30))
        self.icon.setPixmap(QPixmap(self.iconurl))
        self.icon.setScaledContents(True)
        self.info = QLabel(self)
        self.info.setWordWrap(True)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.addWidget(self.icon)
        self.horizontalLayout.addWidget(self.info)

        if self._details:
            self.detailsbtn = QPushButton(self)
            self.detailsbtn.setMinimumSize(QSize(80, 25))
            self.detailsbtn.setMaximumSize(QSize(100, 25))
            self.detailsbtn.clicked.connect(self._toggledetails)
            self.horizontalLayout_3 = QHBoxLayout()
            self.horizontalLayout_3.setSpacing(0)
            self.horizontalLayout_3.setContentsMargins(40, -1, -1, -1)
            self.horizontalLayout_3.addWidget(self.detailsbtn)
            self.horizontalLayout_3.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

            self.textBrowser = QTextBrowser(self)
            self.textBrowser.setAutoFillBackground(True)
            self.textBrowser.setStyleSheet(
                u"QTextBrowser{background-color: #f0f0f0; margin-left: 40px;}")
            self.textBrowser.setFrameShape(QFrame.NoFrame)
            self.textBrowser.setFrameShadow(QFrame.Sunken)
            self.textBrowser.setTextInteractionFlags(
                Qt.LinksAccessibleByKeyboard |
                Qt.LinksAccessibleByMouse |
                Qt.TextBrowserInteraction |
                Qt.TextSelectableByKeyboard |
                Qt.TextSelectableByMouse)
            self._detailed = False
            self.textBrowser.hide()

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        if self._trigger == MsgTrigger.GOBTN and self._type == MsgType.WARNING:
            self.buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            btn = self.buttonBox.button(QDialogButtonBox.Cancel)
            btn.setText("Abbrechen")
        else:
            self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        # layout dialog window
        verticalLayout = QVBoxLayout(self)
        verticalLayout.addLayout(horizontalLayout_2)
        verticalLayout.addLayout(self.horizontalLayout)
        verticalLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))
        if details:
            verticalLayout.addLayout(self.horizontalLayout_3)
        verticalLayout.addItem(QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Fixed))
        if details:
            verticalLayout.addWidget(self.textBrowser)
        verticalLayout.addItem(QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding))
        verticalLayout.addWidget(self.buttonBox)

        self._retranslateMb()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def _toggledetails(self) -> None:
        if self._detailed:
            self.textBrowser.hide()
            self.detailsbtn.setText(self._utp.s("details"))
            self._detailed = False
        else:
            self.textBrowser.show()
            self.detailsbtn.setText(self._utp.s("showless"))
            self._detailed = True

    def _retranslateMb(self) -> None:
        self.setWindowTitle(self._utp.sfl("msgWindows", self._type.value))
        self.title.setText(self._utp.sfnl("msgTitle", self._type.value, self._trigger.value))
        self.info.setText(self._utp.sfnl("msgInfo", self._type.value, self._trigger.value))

        if not self._details:
            return
        self.detailsbtn.setText(self._utp.s("msgdet"))
        if self._type == MsgType.SUCCESS:
            html = self._utp.constructSuccessBrowser(self._details)
        elif self._type == MsgType.WARNING or self._type == MsgType.ERROR:
            html = self._utp.constructErrorBrowser(self._details)
        else:
            html = self._utp.wraptext(str(self._details[0]))
        self.textBrowser.setHtml(html)


###################
# MainWindow class
###################


class RvMainWindow(QMainWindow):
    centralwidget: QWidget
    stackedWidget: QStackedWidget
    _pn: int
    profilesLabel: QLabel
    repsLabel: QLabel
    pScrollArea: QScrollArea
    rScrollArea: QScrollArea

    menuButtons: list[MenuButton]
    stepHeaders: list[QFrame]
    steps: list[QLabel]
    stepTitles: list[QLabel]
    stepInfos: list[ToolButton]

    aipFileSpinner: FileSpinner
    # vzeFileSpinner: FileSpinner # VZE
    spinnerGoBtn: ToolButton

    profiles: list[QLayout]
    profileHeaders: list[QLayout]
    profileTitles: list[LabelButton]
    profileRecoms: list[QLabel]
    profileDetails: list[DetailsButton]
    profileInfos: list[InfoTextBrowser]
    pScrollAreaContents: QWidget

    aips: list[QLayout]
    aipInfos: list[InfoTextBrowser]
    aipDetails: list[DetailsButton]
    aipTitles: [LabelButton]
    aipDescs: list[QLabel]
    aipFormats: list[QLabel]
    rScrollAreaContents: QWidget
    repLayoutV: QLayout

    outFileSpinner: FileSpinner
    goButton: ToolButton

    def __init__(self, pn: int, texts: str):
        super().__init__()
        self._utp = UiTextProvider(texts)
        self.centralwidget = None
        self.stackedWidget = None
        self._pn = pn
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
        # self.vzeFileSpinner = None # VZE
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
        self.outFileSpinner = None
        self.goButton = None

        self.setWindowIcon(icon_DIP)
        self._setupUi()

    def _setupUi(self) -> None:
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
        self.centralwidget.setStyleSheet(u"")

        menuLayout = QHBoxLayout()
        menuLayout.setSpacing(1)
        menuLayout.setContentsMargins(-1, -1, -1, 20)

        self.menuGroup.setParent(self.centralwidget)
        btnd = MenuButton(self.centralwidget, True)
        menuLayout.addWidget(btnd)
        self.menuButtons.append(btnd)
        self.menuGroup.addButton(btnd)
        self.menuGroup.setId(btnd, 0)
        for i in range(1, 4):
            btn = MenuButton(self.centralwidget, False)
            menuLayout.addWidget(btn)
            self.menuButtons.append(btn)
            self.menuGroup.addButton(btn)
            self.menuGroup.setId(btn, i)

        content = QWidget()
        scrollLayout = QGridLayout(content)
        scrollArea = QScrollArea(content)
        scrollArea.setFrameShape(QFrame.NoFrame)
        scrollArea.setFrameShadow(QFrame.Plain)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        scrollArea.setWidgetResizable(True)
        self.scrollAreaContents = QWidget()
        self.scrollAreaContents.setGeometry(QRect(0, 0, 501, 552))
        contentLayoutV = QVBoxLayout(self.scrollAreaContents)

        self.infoGroup.setParent(self.scrollAreaContents)
        # Create Step Header
        for i in range(1, 4):
            stepFrame = QFrame(self.scrollAreaContents)
            stepFrame.setMinimumSize(QSize(0, 20))
            stepFrame.setMaximumSize(QSize(16777215, 50))
            stepFrame.setStyleSheet(u".QFrame{\n"
                                    "    border: 1px solid " + lwl_darkblue + ";\n"
                                    "    border-radius: 5px;\n"
                                    "}")
            stepFrame.setFrameShape(QFrame.Box)
            stepFrame.setFrameShadow(QFrame.Plain)
            stepFrame.setLineWidth(2)

            step = QLabel(stepFrame)
            step.setMinimumSize(QSize(70, 0))
            step.setMaximumSize(QSize(100, 16777215))
            step.setFont(font14)
            step.setAutoFillBackground(False)
            step.setStyleSheet(u".QLabel{\n"
                               "    border-radius: 5px;\n"
                               "    background-color: " + lwl_darkblue + ";\n"
                               "    padding: 1px 10px;\n"
                               "    color: #ffffff;\n"
                               "}")
            step.setAlignment(Qt.AlignCenter)

            title = QLabel(stepFrame)
            title.setFont(font16)
            title.setToolTipDuration(-1)
            title.setStyleSheet(u".QLabel{\n"
                                "    color: " + lwl_darkblue + ";\n"
                                "    padding-top: 1px;\n"
                                "    padding-bottom: 1px;\n"
                                "}")

            info = ToolButton(stepFrame, icon_info, QSize(20, 20), QSize(20, 0), QSize(30, 16777215))

            # Layout step frame
            horizontalLayout = QHBoxLayout(stepFrame)
            horizontalLayout.setSpacing(0)
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
            self.infoGroup.setId(info, i - 1)

        # Create Step 1 (file spinner)
        self.spinnerGoBtn = ToolButton(self.scrollAreaContents, icon_check, QSize(20, 20), QSize(30, 30), QSize(30, 30))

        self.aipFileSpinner = FileSpinner(self.scrollAreaContents, "a")
        # self.vzeFileSpinner = FileSpinner(self.scrollAreaContents, "v") # VZE

        # Layout file spinners
        fileSpinnerLayoutH = QHBoxLayout()
        fileSpinnerLayoutH.setContentsMargins(10, 10, 10, 20)
        self.aipFileSpinner.addToLayout(fileSpinnerLayoutH)
        # fileSpinnerLayoutH.addItem(QSpacerItem(30, 30, QSizePolicy.Minimum, QSizePolicy.Minimum)) # VZE
        # self.vzeFileSpinner.addToLayout(fileSpinnerLayoutH) # VZE
        fileSpinnerLayoutH.addItem(QSpacerItem(30, 30, QSizePolicy.Minimum, QSizePolicy.Expanding))
        fileSpinnerLayoutH.addWidget(self.spinnerGoBtn)
        fileSpinnerLayoutH.setStretch(0, 2)  # VZE: comment out
        fileSpinnerLayoutH.setStretch(3, 1)  # VZE: comment out

        # Create step 2 (profiles)
        self.profilesLabel = QLabel(self.scrollAreaContents)
        self.profilesLabel.setFont(font12)
        self.profilesLabel.setWordWrap(True)

        self.profileGroup.setParent(self.scrollAreaContents)
        self.profDetGroup.setParent(self.scrollAreaContents)

        # Create profiles
        for i in range(self._pn):
            pTitle = LabelButton(self.scrollAreaContents)
            pTitle.setMinimumSize(QSize(150, 18))
            pTitle.setMaximumSize(QSize(200, 100))

            pRecom = QLabel(self.scrollAreaContents)
            pRecom.setFont(font12)
            pRecom.setAlignment(Qt.AlignCenter)

            line1 = Line(self.scrollAreaContents, max_=QSize(60, 16777215))
            line2 = Line(self.scrollAreaContents)

            pDetail = DetailsButton(self.scrollAreaContents)

            # Layout Header
            pHeaderLayout = QHBoxLayout()
            pHeaderLayout.addWidget(pTitle)
            pHeaderLayout.addWidget(line1)
            pHeaderLayout.addWidget(pRecom)
            pHeaderLayout.addWidget(line2)
            pHeaderLayout.addWidget(pDetail)

            # Layout profile
            pLayout = QVBoxLayout()
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

        # Layout scroll area contents
        verticalLayout_9 = QVBoxLayout()
        verticalLayout_9.setSpacing(10)
        verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        verticalLayout_9.addLayout(self.profiles[0])
        verticalLayout_9.addLayout(self.profiles[1])
        verticalLayout_9.addLayout(self.profiles[2])
        verticalLayout_9.addLayout(self.profiles[3])

        # Layout step 2
        profilesLayout = QVBoxLayout()
        profilesLayout.setSpacing(10)
        profilesLayout.setContentsMargins(10, 10, 10, 20)
        profilesLayout.addWidget(self.profilesLabel)
        profilesLayout.addLayout(verticalLayout_9)

        # Create step 3 (representations)
        self.repsLabel = QLabel(self.scrollAreaContents)
        self.repsLabel.setFont(font12)
        self.repsLabel.setWordWrap(True)

        self.repLayoutV = QVBoxLayout()
        self.repLayoutV.setSpacing(0)
        self.repLayoutV.setContentsMargins(0, 0, 0, 0)
        self.repLayoutV.setSpacing(10)

        self.repsGroup.setParent(self.scrollAreaContents)
        self.repsDetGroup.setParent(self.scrollAreaContents)

        # Layout step 3
        repsLayout = QVBoxLayout()
        repsLayout.setSpacing(10)
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
        self.infopage = QTextBrowser(page)
        self.infopage.setFont(font12)
        self.infopage.setTextInteractionFlags(
            Qt.LinksAccessibleByKeyboard |
            Qt.LinksAccessibleByMouse |
            Qt.TextBrowserInteraction |
            Qt.TextSelectableByKeyboard |
            Qt.TextSelectableByMouse)
        self.infopage.setFrameShape(QFrame.NoFrame)
        vl = QVBoxLayout(page)
        vl.setSpacing(0)
        vl.setContentsMargins(0, 0, 0, 0)
        vl.addWidget(self.infopage)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setFont(font12)
        self.stackedWidget.addWidget(content)
        self.stackedWidget.addWidget(page)
        self.stackedWidget.setCurrentIndex(0)

        # Layout left side of the application
        leftLayout = QVBoxLayout()
        leftLayout.setSpacing(0)
        leftLayout.addLayout(menuLayout)
        leftLayout.addWidget(self.stackedWidget)

        # Create overview (right side of the application)
        overviewFrame = QFrame(self.centralwidget)
        overviewFrame.setMinimumSize(QSize(160, 0))
        overviewFrame.setMaximumSize(QSize(250, 16777215))
        overviewFrame.setStyleSheet(u"QFrame{\n"
                                    "    border-radius: 0;\n"
                                    "    border: 1px solid " + lwl_darkred + "\n"
                                    "}")
        overviewFrame.setFrameShape(QFrame.StyledPanel)
        overviewFrame.setFrameShadow(QFrame.Raised)

        # Title
        self.ovTitle = QWidget(overviewFrame)
        self.ovTitle.setMinimumSize(QSize(0, 20))
        self.label_3 = QLabel(self.ovTitle)
        self.label_3.setMinimumSize(QSize(130, 0))
        self.label_3.setMaximumSize(QSize(130, 16777215))
        self.label_3.setFont(font16)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u".QLabel{\n"
                                   "    border-radius: 5px;\n"
                                   "    border: none;\n"
                                   "    background-color: " + lwl_darkblue + ";\n"
                                   "    color: #ffffff\n"
                                   "}")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.horizontalLayout = QHBoxLayout(self.ovTitle)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.addWidget(self.label_3)

        # Text browser
        self.ieTextBrowser = OverviewTextBrowser(overviewFrame)
        self.profileTextBrowser = OverviewTextBrowser(overviewFrame)
        self.profileTextBrowser.setMaximumSize(QSize(16777215, 50))
        self.repTextBrowser = OverviewTextBrowser(overviewFrame)

        # Delivery box
        self.label = QLabel(overviewFrame)
        self.label.setFont(font12b)
        self.label.setStyleSheet(u"QLabel{border: none}")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setMargin(4)
        self.label.setIndent(1)

        self.btnViewer = OverviewRadioBtn(overviewFrame)
        self.btnDownload = OverviewRadioBtn(overviewFrame)
        self.btnBoth = OverviewRadioBtn(overviewFrame)

        self.overviewGroup.setParent(overviewFrame)
        self.overviewGroup.addButton(self.btnViewer)
        self.overviewGroup.setId(self.btnViewer, 0)
        self.overviewGroup.addButton(self.btnDownload)
        self.overviewGroup.setId(self.btnDownload, 1)
        self.overviewGroup.addButton(self.btnBoth)
        self.overviewGroup.setId(self.btnBoth, 2)

        deliveryButtonsLayout = QVBoxLayout()
        deliveryButtonsLayout.setSpacing(0)
        deliveryButtonsLayout.setContentsMargins(30, -1, -1, -1)
        deliveryButtonsLayout.addWidget(self.btnViewer)
        deliveryButtonsLayout.addWidget(self.btnDownload)
        deliveryButtonsLayout.addWidget(self.btnBoth)

        deliveryLayout = QVBoxLayout()
        deliveryLayout.addWidget(self.label)
        deliveryLayout.addLayout(deliveryButtonsLayout)

        # Output-Path
        self.outFileSpinner = FileSpinner(overviewFrame, "o")
        ofsLayoutH = QHBoxLayout()
        ofsLayoutH.setContentsMargins(10, 20, 10, 10)
        ofsLayoutH.setSpacing(4)
        self.outFileSpinner.addToLayout(ofsLayoutH)

        # Request button
        self.goButton = ToolButton(overviewFrame, min_=QSize(60, 0), max_=QSize(60, 16777215))
        self.goButton.setFont(font12b)

        self.ovButtonLayout = QHBoxLayout()
        self.ovButtonLayout.setContentsMargins(-1, -1, 20, -1)
        self.ovButtonLayout.addItem(QSpacerItem(94, 17, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.ovButtonLayout.addWidget(self.goButton)

        # Layout overview
        verticalLayout = QVBoxLayout(overviewFrame)
        verticalLayout.setSpacing(0)
        verticalLayout.addWidget(self.ovTitle)
        verticalLayout.addItem(QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed))
        verticalLayout.addWidget(self.ieTextBrowser)
        verticalLayout.addWidget(self.profileTextBrowser)
        verticalLayout.addWidget(self.repTextBrowser)
        verticalLayout.addLayout(deliveryLayout)
        verticalLayout.addLayout(ofsLayoutH)
        verticalLayout.addItem(QSpacerItem(17, 37, QSizePolicy.Minimum, QSizePolicy.Expanding))
        verticalLayout.addLayout(self.ovButtonLayout)
        verticalLayout.setStretch(2, 4)
        verticalLayout.setStretch(4, 1)

        # Layout central widget / window
        centralWidgetLayoutH = QHBoxLayout(self.centralwidget)
        centralWidgetLayoutH.setSpacing(0)
        centralWidgetLayoutH.setContentsMargins(0, 0, 0, 0)
        centralWidgetLayoutH.addLayout(leftLayout)
        centralWidgetLayoutH.addWidget(overviewFrame)

        self.setCentralWidget(self.centralwidget)
        statusbar = QStatusBar(self)
        statusbar.setEnabled(True)
        statusbar.setStyleSheet("QStatusBar{background-color: " + lwl_lightgray + "}")
        self.setStatusBar(statusbar)

        self._retranslateBaseUi()

    def _retranslateBaseUi(self):
        self.setWindowTitle(self._utp.s("windowTitle"))

        for i in range(4):
            self.menuButtons[i].setStatusTip(self._utp.sfl("menuStatuses", i))
            self.menuButtons[i].setText(self._utp.sfl("menuTitles", i))

        for i in range(3):
            self.stepTitles[i].setText(self._utp.sfl("stepTitles", i))
            self.steps[i].setText(self._utp.s("step") + " " + str(i + 1))
            self.stepInfos[i].setToolTip(self._utp.s("help"))

        self.aipFileSpinner.setPlaceholderText(self._utp.sfl("spinnerPh", 0))
        # self.vzeFileSpinner.setPlaceholderText(self._utp.sfl("spinnerPh", 1)) # VZE
        self.aipFileSpinner.setToolTip(
            self._utp.sfl("spinnerTooltip", 0),
            self._utp.sfl("spinnerTooltip", 1))
        # self.vzeFileSpinner.setToolTip(self._utp.sfl("spinnerTooltip", 2)) # VZE
        self.spinnerGoBtn.setToolTip(self._utp.sfl("spinnerTooltip", 3))
        self.spinnerGoBtn.setStatusTip(self._utp.sfl("spinnerTooltip", 3))

        self.repsLabel.setText(self._utp.s("repLabel"))

        self.label_3.setText(self._utp.s("choice"))
        self.ieTextBrowser.setHtml(self._utp.constructIeItb())
        self.profileTextBrowser.setHtml(self._utp.constructProfItb())
        self.repTextBrowser.setHtml(self._utp.constructOvRepItb())

        self.label.setText(self._utp.s("deliv"))
        self.btnViewer.setToolTip("")
        self.btnViewer.setText(self._utp.sfl("overviewBtns", 0))
        self.btnDownload.setToolTip("")
        self.btnDownload.setText(self._utp.sfl("overviewBtns", 1))
        self.btnBoth.setToolTip("")
        self.btnBoth.setText(self._utp.sfl("overviewBtns", 2))
        self.outFileSpinner.setPlaceholderText(self._utp.sfl("spinnerPh", 2))
        self.outFileSpinner.setToolTip(self._utp.sfl("spinnerTooltip", 1))
        self.goButton.setStatusTip(self._utp.s("goStatus"))
        self.goButton.setText(self._utp.s("go"))

    def createAIP(self, vl: QLayout, parent: QWidget, index_: int) -> None:
        aiptitle = LabelButton(parent)
        aiptitle.setMinimumSize(QSize(60, 17))
        aiptitle.setMaximumSize(QSize(70, 100))

        aipname = QLabel(parent)
        aipname.setFont(font12)
        aipname.setAlignment(Qt.AlignCenter)
        aipname.setStyleSheet("QLabel:inactive{font: "+lwl_middlegray+"}")

        aipformats = QLabel(parent)
        aipformats.setFont(font12)
        aipformats.setAlignment(Qt.AlignCenter)
        aipformats.setStyleSheet("QLabel:inactive{font: " + lwl_middlegray + "}")

        line1 = Line(parent, max_=QSize(30, 16777215))
        line2 = Line(parent)
        line3 = Line(parent, max_=QSize(30, 16777215))

        aipdetails = DetailsButton(parent)

        # Layout AIP-Header
        aipHeaderLayout = QHBoxLayout()
        aipHeaderLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        aipHeaderLayout.addWidget(aiptitle)
        aipHeaderLayout.addWidget(line1)
        aipHeaderLayout.addWidget(aipname)
        aipHeaderLayout.addWidget(line2)
        aipHeaderLayout.addWidget(aipformats)
        aipHeaderLayout.addWidget(line3)
        aipHeaderLayout.addWidget(aipdetails)
        aipHeaderLayout.setSpacing(10)

        # Layout AIP
        aipLayout = QVBoxLayout()
        aipLayout.setSpacing(10)
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

    def closeAips(self) -> None:
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

    def setAIPenabled(self, enabled: bool, aiplayout: QLayout, label: str = None) -> None:
        header = aiplayout.children()[0]
        if enabled:
            for i in range(header.count()):
                header.itemAt(i).widget().setEnabled(True)
        else:
            for i in range(header.count()):
                header.itemAt(i).widget().setEnabled(False)
        if label:
            self.repsLabel.setText(label)
        else:
            self.repsLabel.setText(self._utp.s("repLabel"))

    def createitb(self, parent: QWidget, layout: QLayout, type_: str, index_: int, infotexts: dict) -> None:
        info = InfoTextBrowser(parent, self.calcheaderwidth())
        if type_ == "a":
            info.setHtml(self._utp.constructRepItb(infotexts["date"], infotexts["files"]))
            self.aipInfos[index_] = info
        elif type_ == "p":
            info.setHtml(self._utp.constructProfileItb(infotexts))
            self.profileInfos[index_] = info
        layout.addWidget(info)

    def calcheaderwidth(self) -> int:
        pheader = self.profiles[0].children()[0]
        w = (pheader.count() - 1) * 10
        for i in reversed(range(pheader.count())):
            w += pheader.itemAt(i).widget().width()
        return w

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        allinfos = []
        allinfos.extend(self.profileInfos)
        allinfos.extend(self.aipInfos)
        for info in allinfos:
            if info:
                info.setfwidth(self.calcheaderwidth())

    def retranslateAips(self, formats: list) -> None:
        for i in range(len(self.aips)):
            self.aipTitles[i].setText(self._utp.s("AIP") + " " + str(i))
            if i == 0:
                self.aipDescs[i].setText(self._utp.s("root"))
            else:
                self.aipDescs[i].setText(self._utp.s("rep"))
            self.aipFormats[i].setText(", ".join(formats[i]))
            self.aipDetails[i].setText(self._utp.s("details"))

    def retranslateProfiles(self, nos: list[str], titles: list[str], recoms: list[str]) -> None:
        self.profilesLabel.setText(self._utp.s("profLabel"))

        for i in range(self._pn):
            self.profileTitles[i].setText(self._utp.s("profile") + " " + str(nos[i]) + " - " + titles[i])
            self.profileRecoms[i].setText(recoms[i])
            self.profileDetails[i].setText(self._utp.s("details"))

    def setInfoPage(self, info: dict) -> None:
        self.infopage.setHtml(self._utp.constructItb(info))
        self.stackedWidget.setCurrentIndex(1)

    def updateOvVzeTb(self,
                      signature: str,
                      title: str,
                      aiptype: str,
                      filetype: str,
                      runtime: str,
                      contains: str) -> None:
        if aiptype == "FILE_COLLECTION":
            aiptype = self._utp.s("typecollection")
        elif aiptype == "EAkte":
            aiptype = self._utp.s("typeefile")
        if filetype:
            type_ = filetype + " (" + aiptype + ")"
        else:
            type_ = aiptype

        if not signature:
            signature = "?"

        infos = [
            signature,
            title,
            type_,
            runtime,
            contains
        ]
        self.ieTextBrowser.setHtml(self._utp.constructIeItb(infos))

    def updateOvProTb(self, no: int, title: str) -> None:
        self.profileTextBrowser.setHtml(self._utp.constructProfItb(no, title))

    def updateOvRepTb(self, nos: list[int], aip: bool = False) -> None:
        self.repTextBrowser.setHtml(self._utp.constructOvRepItb(nos, aip))
