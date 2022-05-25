# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Basic.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 570)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftLayout = QVBoxLayout()
        self.leftLayout.setSpacing(0)
        self.leftLayout.setObjectName(u"leftLayout")
        self.menuLayout = QHBoxLayout()
        self.menuLayout.setSpacing(1)
        self.menuLayout.setObjectName(u"menuLayout")
        self.menuLayout.setContentsMargins(-1, -1, -1, 20)
        self.btnDIP = QPushButton(self.centralwidget)
        self.btnDIP.setObjectName(u"btnDIP")
        self.btnDIP.setMinimumSize(QSize(0, 21))
        self.btnDIP.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamilies([u"Source Sans Pro"])
        font.setPointSize(12)
        self.btnDIP.setFont(font)
        self.btnDIP.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDIP.setContextMenuPolicy(Qt.NoContextMenu)
        self.btnDIP.setAutoFillBackground(False)
        self.btnDIP.setStyleSheet(u"QPushButton{\n"
"    background-color: rgb(0, 50, 95);\n"
"    border: 1px solid rgb(0, 50, 95);\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(155, 24, 42)\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: rgb(155, 24, 42);\n"
"    border: 1px solid rgb(155, 24, 42)\n"
"}")
        self.btnDIP.setCheckable(True)
        self.btnDIP.setChecked(True)
        self.btnDIP.setAutoDefault(False)
        self.btnDIP.setFlat(False)

        self.menuLayout.addWidget(self.btnDIP)

        self.btnHelp1 = QPushButton(self.centralwidget)
        self.btnHelp1.setObjectName(u"btnHelp1")
        self.btnHelp1.setMinimumSize(QSize(0, 21))
        self.btnHelp1.setMaximumSize(QSize(16777215, 21))
        self.btnHelp1.setFont(font)
        self.btnHelp1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnHelp1.setAutoFillBackground(False)
        self.btnHelp1.setStyleSheet(u"QPushButton{\n"
"    background-color: rgb(0, 50, 95);\n"
"    border: 1px solid rgb(0, 50, 95);\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(155, 24, 42)\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: rgb(155, 24, 42);\n"
"    border: 1px solid rgb(155, 24, 42)\n"
"}")
        self.btnHelp1.setIconSize(QSize(12, 12))
        self.btnHelp1.setCheckable(True)
        self.btnHelp1.setChecked(False)
        self.btnHelp1.setFlat(False)

        self.menuLayout.addWidget(self.btnHelp1)

        self.btnHelp2 = QPushButton(self.centralwidget)
        self.btnHelp2.setObjectName(u"btnHelp2")
        self.btnHelp2.setMinimumSize(QSize(0, 21))
        self.btnHelp2.setMaximumSize(QSize(16777215, 21))
        self.btnHelp2.setFont(font)
        self.btnHelp2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnHelp2.setAutoFillBackground(False)
        self.btnHelp2.setStyleSheet(u"QPushButton{\n"
"    background-color: rgb(0, 50, 95);\n"
"    border: 1px solid rgb(0, 50, 95);\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(155, 24, 42)\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: rgb(155, 24, 42);\n"
"    border: 1px solid rgb(155, 24, 42)\n"
"}")
        self.btnHelp2.setCheckable(True)
        self.btnHelp2.setFlat(False)

        self.menuLayout.addWidget(self.btnHelp2)

        self.btnHelp3 = QPushButton(self.centralwidget)
        self.btnHelp3.setObjectName(u"btnHelp3")
        self.btnHelp3.setMinimumSize(QSize(0, 21))
        self.btnHelp3.setMaximumSize(QSize(16777215, 21))
        self.btnHelp3.setFont(font)
        self.btnHelp3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnHelp3.setAutoFillBackground(False)
        self.btnHelp3.setStyleSheet(u"QPushButton{\n"
"    background-color: rgb(0, 50, 95);\n"
"    border: 1px solid rgb(0, 50, 95);\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(155, 24, 42)\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: rgb(155, 24, 42);\n"
"    border: 1px solid rgb(155, 24, 42)\n"
"}")
        self.btnHelp3.setCheckable(True)
        self.btnHelp3.setFlat(False)

        self.menuLayout.addWidget(self.btnHelp3)


        self.leftLayout.addLayout(self.menuLayout)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font)
        self.content = QWidget()
        self.content.setObjectName(u"content")
        self.verticalLayout_8 = QVBoxLayout(self.content)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.step1Frame = QFrame(self.content)
        self.step1Frame.setObjectName(u"step1Frame")
        self.step1Frame.setMinimumSize(QSize(0, 20))
        self.step1Frame.setMaximumSize(QSize(16777215, 50))
        palette1 = QPalette()
        brush5 = QBrush(QColor(0, 50, 95, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush5)
        brush6 = QBrush(QColor(0, 75, 143, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush6)
        brush7 = QBrush(QColor(0, 62, 119, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush7)
        brush8 = QBrush(QColor(0, 25, 47, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush8)
        brush9 = QBrush(QColor(0, 33, 63, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush9)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.step1Frame.setPalette(palette1)
        self.step1Frame.setStyleSheet(u".QFrame{\n"
"    border: 1px solid #00325f;\n"
"    border-radius: 5px;\n"
"}")
        self.step1Frame.setFrameShape(QFrame.Box)
        self.step1Frame.setFrameShadow(QFrame.Plain)
        self.step1Frame.setLineWidth(2)
        self.horizontalLayout_12 = QHBoxLayout(self.step1Frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.step1step = QLabel(self.step1Frame)
        self.step1step.setObjectName(u"step1step")
        self.step1step.setMinimumSize(QSize(70, 0))
        self.step1step.setMaximumSize(QSize(100, 16777215))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.step1step.setPalette(palette2)
        font1 = QFont()
        font1.setFamilies([u"Source Sans Pro"])
        font1.setPointSize(14)
        self.step1step.setFont(font1)
        self.step1step.setAutoFillBackground(False)
        self.step1step.setStyleSheet(u".QLabel{\n"
"    border-radius: 5px;\n"
"    background-color: #00325f;\n"
"    padding: 1px 10px;\n"
"}")
        self.step1step.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.step1step)

        self.horizontalSpacer = QSpacerItem(50, 15, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.step1title = QLabel(self.step1Frame)
        self.step1title.setObjectName(u"step1title")
        font2 = QFont()
        font2.setFamilies([u"Source Sans Pro"])
        font2.setPointSize(16)
        self.step1title.setFont(font2)
        self.step1title.setToolTipDuration(-1)
        self.step1title.setStyleSheet(u".QLabel{\n"
"    color: #00325f;\n"
"    padding-top: 1px;\n"
"    padding-bottom: 1px;\n"
"}")

        self.horizontalLayout_12.addWidget(self.step1title)

        self.horizontalSpacer_2 = QSpacerItem(50, 15, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.step1info = QPushButton(self.step1Frame)
        self.step1info.setObjectName(u"step1info")
        self.step1info.setMinimumSize(QSize(20, 0))
        self.step1info.setMaximumSize(QSize(30, 16777215))
        self.step1info.setCursor(QCursor(Qt.PointingHandCursor))
        self.step1info.setStyleSheet(u"QPushButton{\n"
"    padding-right: 5px\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../../Users/Alina/Documents/LWL/Code-Basis/Piktogramme_svg/SVG/LWL_mehr_Infos.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.step1info.setIcon(icon)
        self.step1info.setFlat(True)

        self.horizontalLayout_12.addWidget(self.step1info)


        self.verticalLayout_8.addWidget(self.step1Frame)

        self.fileSpinnerWidget = QHBoxLayout()
        self.fileSpinnerWidget.setObjectName(u"fileSpinnerWidget")
        self.fileSpinnerWidget.setContentsMargins(10, 10, 10, 20)
        self.aipFileSpinner = QSpinBox(self.content)
        self.aipFileSpinner.setObjectName(u"aipFileSpinner")

        self.fileSpinnerWidget.addWidget(self.aipFileSpinner)

        self.horizontalSpacer_15 = QSpacerItem(98, 17, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.fileSpinnerWidget.addItem(self.horizontalSpacer_15)

        self.vzeFileSpinner = QSpinBox(self.content)
        self.vzeFileSpinner.setObjectName(u"vzeFileSpinner")

        self.fileSpinnerWidget.addWidget(self.vzeFileSpinner)


        self.verticalLayout_8.addLayout(self.fileSpinnerWidget)

        self.step2Frame = QFrame(self.content)
        self.step2Frame.setObjectName(u"step2Frame")
        self.step2Frame.setMinimumSize(QSize(0, 20))
        self.step2Frame.setMaximumSize(QSize(16777215, 50))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush8)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush9)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.step2Frame.setPalette(palette3)
        self.step2Frame.setStyleSheet(u".QFrame{\n"
"    border: 1px solid #00325f;\n"
"    border-radius: 5px;\n"
"}")
        self.step2Frame.setFrameShape(QFrame.Box)
        self.step2Frame.setFrameShadow(QFrame.Plain)
        self.step2Frame.setLineWidth(2)
        self.horizontalLayout_11 = QHBoxLayout(self.step2Frame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.step2step = QLabel(self.step2Frame)
        self.step2step.setObjectName(u"step2step")
        self.step2step.setMinimumSize(QSize(70, 0))
        self.step2step.setMaximumSize(QSize(100, 16777215))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.step2step.setPalette(palette4)
        self.step2step.setFont(font1)
        self.step2step.setAutoFillBackground(False)
        self.step2step.setStyleSheet(u".QLabel{\n"
"    border-radius: 5px;\n"
"    background-color: #00325f;\n"
"    padding: 1px 10px;\n"
"}")
        self.step2step.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.step2step)

        self.horizontalSpacer_3 = QSpacerItem(50, 15, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)

        self.step2title = QLabel(self.step2Frame)
        self.step2title.setObjectName(u"step2title")
        self.step2title.setFont(font2)
        self.step2title.setToolTipDuration(-1)
        self.step2title.setStyleSheet(u".QLabel{\n"
"    color: #00325f;\n"
"    padding-top: 1px;\n"
"    padding-bottom: 1px;\n"
"}")

        self.horizontalLayout_11.addWidget(self.step2title)

        self.horizontalSpacer_4 = QSpacerItem(50, 15, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.step2info = QPushButton(self.step2Frame)
        self.step2info.setObjectName(u"step2info")
        self.step2info.setMinimumSize(QSize(20, 0))
        self.step2info.setMaximumSize(QSize(30, 16777215))
        self.step2info.setCursor(QCursor(Qt.PointingHandCursor))
        self.step2info.setStyleSheet(u"QPushButton{\n"
"    padding-right: 5px\n"
"}")
        self.step2info.setIcon(icon)
        self.step2info.setFlat(True)

        self.horizontalLayout_11.addWidget(self.step2info)


        self.verticalLayout_8.addWidget(self.step2Frame)

        self.profilesLayout = QVBoxLayout()
        self.profilesLayout.setSpacing(10)
        self.profilesLayout.setObjectName(u"profilesLayout")
        self.profilesLayout.setContentsMargins(10, 10, 10, 20)
        self.profilesLabel = QLabel(self.content)
        self.profilesLabel.setObjectName(u"profilesLabel")
        self.profilesLabel.setFont(font)
        self.profilesLabel.setWordWrap(True)

        self.profilesLayout.addWidget(self.profilesLabel)

        self.scrollArea = QScrollArea(self.content)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -4, 497, 174))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.p0Layout = QVBoxLayout()
        self.p0Layout.setObjectName(u"p0Layout")
        self.p0HeaderLayout = QHBoxLayout()
        self.p0HeaderLayout.setObjectName(u"p0HeaderLayout")
        self.p0title = QPushButton(self.scrollAreaWidgetContents)
        self.p0title.setObjectName(u"p0title")
        self.p0title.setMinimumSize(QSize(120, 18))
        self.p0title.setMaximumSize(QSize(180, 100))
        font3 = QFont()
        font3.setFamilies([u"Source Sans Pro"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.p0title.setFont(font3)
        self.p0title.setCursor(QCursor(Qt.PointingHandCursor))
        self.p0title.setAutoFillBackground(False)
        self.p0title.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(180, 178, 178);\n"
"     border-radius: 5px;\n"
"	padding: 3px 10px\n"
"}\n"
"\n"
"QPushButton:active{\n"
"	background-color: #e7e7e8;\n"
"     border: 1px solid rgb(0, 50, 95)\n"
"}\n"
"\n"
"QPushButton:active:hover{\n"
"     border: 1px solid rgb(155, 24, 42);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(155, 24, 42);\n"
"	color: rgb(255, 255, 255);\n"
"     border: none;\n"
"}")
        self.p0title.setCheckable(True)
        self.p0title.setChecked(False)

        self.p0HeaderLayout.addWidget(self.p0title)

        self.line_8 = QFrame(self.scrollAreaWidgetContents)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setMaximumSize(QSize(60, 16777215))
        self.line_8.setBaseSize(QSize(0, 0))
        font4 = QFont()
        font4.setPointSize(12)
        self.line_8.setFont(font4)
        self.line_8.setAutoFillBackground(True)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.line_8.setLineWidth(2)
        self.line_8.setMidLineWidth(0)
        self.line_8.setFrameShape(QFrame.HLine)

        self.p0HeaderLayout.addWidget(self.line_8)

        self.p0recom = QLabel(self.scrollAreaWidgetContents)
        self.p0recom.setObjectName(u"p0recom")
        self.p0recom.setFont(font)
        self.p0recom.setAlignment(Qt.AlignCenter)

        self.p0HeaderLayout.addWidget(self.p0recom)

        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFont(font4)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QFrame.HLine)

        self.p0HeaderLayout.addWidget(self.line_6)

        self.p0details = QPushButton(self.scrollAreaWidgetContents)
        self.p0details.setObjectName(u"p0details")
        self.p0details.setMinimumSize(QSize(60, 15))
        self.p0details.setMaximumSize(QSize(80, 100))
        self.p0details.setFont(font3)
        self.p0details.setCursor(QCursor(Qt.PointingHandCursor))
        self.p0details.setLayoutDirection(Qt.LeftToRight)
        self.p0details.setAutoFillBackground(False)
        self.p0details.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(180, 178, 178);\n"
"     border-radius: 5px;\n"
"     padding: 1px 3px\n"
"}\n"
"\n"
"QPushButton:active{\n"
"	background-color: #e7e7e8;\n"
"     border: 1px solid rgb(0, 50, 95)\n"
"}\n"
"\n"
"QPushButton:active:hover{\n"
"     border: 1px solid rgb(155, 24, 42);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../../Users/Alina/Documents/LWL/Code-Basis/Piktogramme_svg/SVG/LWL_Link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.p0details.setIcon(icon1)
        self.p0details.setIconSize(QSize(11, 11))
        self.p0details.setCheckable(True)
        self.p0details.setChecked(False)

        self.p0HeaderLayout.addWidget(self.p0details)


        self.p0Layout.addLayout(self.p0HeaderLayout)

        self.p0Info = QTextBrowser(self.scrollAreaWidgetContents)
        self.p0Info.setObjectName(u"p0Info")
        self.p0Info.setMaximumSize(QSize(16777215, 80))
        self.p0Info.setFont(font)
        self.p0Info.setStyleSheet(u"")
        self.p0Info.setFrameShape(QFrame.NoFrame)
        self.p0Info.setFrameShadow(QFrame.Plain)
        self.p0Info.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.p0Info.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.p0Layout.addWidget(self.p0Info)

        self.p0Layout.setStretch(1, 1)

        self.verticalLayout_9.addLayout(self.p0Layout)

        self.p1Layout = QVBoxLayout()
        self.p1Layout.setObjectName(u"p1Layout")
        self.p1HeaderLayout = QHBoxLayout()
        self.p1HeaderLayout.setObjectName(u"p1HeaderLayout")
        self.p1_title = QPushButton(self.scrollAreaWidgetContents)
        self.p1_title.setObjectName(u"p1_title")
        self.p1_title.setMinimumSize(QSize(120, 18))
        self.p1_title.setMaximumSize(QSize(180, 100))
        self.p1_title.setFont(font3)
        self.p1_title.setCursor(QCursor(Qt.PointingHandCursor))
        self.p1_title.setAutoFillBackground(False)
        self.p1_title.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(180, 178, 178);\n"
"     border-radius: 5px;\n"
"	padding: 3px 10px\n"
"}\n"
"\n"
"QPushButton:active{\n"
"	background-color: #e7e7e8;\n"
"     border: 1px solid rgb(0, 50, 95)\n"
"}\n"
"\n"
"QPushButton:active:hover{\n"
"     border: 1px solid rgb(155, 24, 42);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(155, 24, 42);\n"
"	color: rgb(255, 255, 255);\n"
"     border: none;\n"
"}")
        self.p1_title.setCheckable(True)
        self.p1_title.setChecked(True)

        self.p1HeaderLayout.addWidget(self.p1_title)

        self.line_7 = QFrame(self.scrollAreaWidgetContents)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMaximumSize(QSize(60, 16777215))
        self.line_7.setFont(font4)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_7.setLineWidth(2)
        self.line_7.setFrameShape(QFrame.HLine)

        self.p1HeaderLayout.addWidget(self.line_7)

        self.p1recom = QLabel(self.scrollAreaWidgetContents)
        self.p1recom.setObjectName(u"p1recom")
        self.p1recom.setMinimumSize(QSize(0, 0))
        self.p1recom.setFont(font)
        self.p1recom.setAlignment(Qt.AlignCenter)

        self.p1HeaderLayout.addWidget(self.p1recom)

        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFont(font4)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QFrame.HLine)

        self.p1HeaderLayout.addWidget(self.line_5)

        self.p1details = QPushButton(self.scrollAreaWidgetContents)
        self.p1details.setObjectName(u"p1details")
        self.p1details.setMinimumSize(QSize(60, 18))
        self.p1details.setMaximumSize(QSize(80, 100))
        self.p1details.setFont(font3)
        self.p1details.setCursor(QCursor(Qt.PointingHandCursor))
        self.p1details.setAutoFillBackground(False)
        self.p1details.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(180, 178, 178);\n"
"     border-radius: 5px;\n"
"     padding: 1px 3px\n"
"}\n"
"\n"
"QPushButton:active{\n"
"	background-color: #e7e7e8;\n"
"     border: 1px solid rgb(0, 50, 95)\n"
"}\n"
"\n"
"QPushButton:active:hover{\n"
"     border: 1px solid rgb(155, 24, 42);\n"
"}")
        self.p1details.setIcon(icon1)
        self.p1details.setIconSize(QSize(11, 11))
        self.p1details.setCheckable(True)
        self.p1details.setChecked(False)

        self.p1HeaderLayout.addWidget(self.p1details)


        self.p1Layout.addLayout(self.p1HeaderLayout)


        self.verticalLayout_9.addLayout(self.p1Layout)

        self.p2Layout = QVBoxLayout()
        self.p2Layout.setObjectName(u"p2Layout")
        self.p2HeaderLayout = QHBoxLayout()
        self.p2HeaderLayout.setObjectName(u"p2HeaderLayout")
        self.p2title = QPushButton(self.scrollAreaWidgetContents)
        self.p2title.setObjectName(u"p2title")
        self.p2title.setMinimumSize(QSize(160, 18))
        self.p2title.setMaximumSize(QSize(200, 100))
        self.p2title.setFont(font3)
        self.p2title.setCursor(QCursor(Qt.PointingHandCursor))
        self.p2title.setAutoFillBackground(False)
        self.p2title.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(180, 178, 178);\n"
"     border-radius: 5px;\n"
"	padding: 3px 10px\n"
"}\n"
"\n"
"QPushButton:active{\n"
"	background-color: #e7e7e8;\n"
"     border: 1px solid rgb(0, 50, 95)\n"
"}\n"
"\n"
"QPushButton:active:hover{\n"
"     border: 1px solid rgb(155, 24, 42);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(155, 24, 42);\n"
"	color: rgb(255, 255, 255);\n"
"     border: none;\n"
"}")
        self.p2title.setCheckable(True)
        self.p2title.setChecked(False)

        self.p2HeaderLayout.addWidget(self.p2title)

        self.line_9 = QFrame(self.scrollAreaWidgetContents)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setMaximumSize(QSize(30, 16777215))
        self.line_9.setFont(font4)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.line_9.setLineWidth(2)
        self.line_9.setFrameShape(QFrame.HLine)

        self.p2HeaderLayout.addWidget(self.line_9)

        self.p2recom = QLabel(self.scrollAreaWidgetContents)
        self.p2recom.setObjectName(u"p2recom")
        self.p2recom.setFont(font)
        self.p2recom.setAlignment(Qt.AlignCenter)

        self.p2HeaderLayout.addWidget(self.p2recom)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFont(font4)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QFrame.HLine)

        self.p2HeaderLayout.addWidget(self.line_4)

        self.p2details = QPushButton(self.scrollAreaWidgetContents)
        self.p2details.setObjectName(u"p2details")
        self.p2details.setMinimumSize(QSize(60, 18))
        self.p2details.setMaximumSize(QSize(80, 100))
        self.p2details.setFont(font3)
        self.p2details.setCursor(QCursor(Qt.PointingHandCursor))
        self.p2details.setAutoFillBackground(False)
        self.p2details.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(180, 178, 178);\n"
"     border-radius: 5px;\n"
"     padding: 1px 3px\n"
"}\n"
"\n"
"QPushButton:active{\n"
"	background-color: #e7e7e8;\n"
"     border: 1px solid rgb(0, 50, 95)\n"
"}\n"
"\n"
"QPushButton:active:hover{\n"
"     border: 1px solid rgb(155, 24, 42);\n"
"}")
        self.p2details.setIcon(icon1)
        self.p2details.setIconSize(QSize(11, 11))
        self.p2details.setCheckable(True)
        self.p2details.setChecked(False)

        self.p2HeaderLayout.addWidget(self.p2details)


        self.p2Layout.addLayout(self.p2HeaderLayout)


        self.verticalLayout_9.addLayout(self.p2Layout)

        self.p3Layout = QVBoxLayout()
        self.p3Layout.setObjectName(u"p3Layout")
        self.p3HeaderLayout = QHBoxLayout()
        self.p3HeaderLayout.setObjectName(u"p3HeaderLayout")
        self.p3title = QPushButton(self.scrollAreaWidgetContents)
        self.p3title.setObjectName(u"p3title")
        self.p3title.setMinimumSize(QSize(120, 18))
        self.p3title.setMaximumSize(QSize(180, 100))
        self.p3title.setFont(font3)
        self.p3title.setCursor(QCursor(Qt.PointingHandCursor))
        self.p3title.setAutoFillBackground(False)
        self.p3title.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(180, 178, 178);\n"
"     border-radius: 5px;\n"
"	padding: 3px 10px\n"
"}\n"
"\n"
"QPushButton:active{\n"
"	background-color: #e7e7e8;\n"
"     border: 1px solid rgb(0, 50, 95)\n"
"}\n"
"\n"
"QPushButton:active:hover{\n"
"     border: 1px solid rgb(155, 24, 42);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(155, 24, 42);\n"
"	color: rgb(255, 255, 255);\n"
"     border: none;\n"
"}")
        self.p3title.setCheckable(True)
        self.p3title.setChecked(False)

        self.p3HeaderLayout.addWidget(self.p3title)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(60, 16777215))
        self.line_2.setFont(font4)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.HLine)

        self.p3HeaderLayout.addWidget(self.line_2)

        self.p3recom = QLabel(self.scrollAreaWidgetContents)
        self.p3recom.setObjectName(u"p3recom")
        self.p3recom.setFont(font)
        self.p3recom.setAlignment(Qt.AlignCenter)

        self.p3HeaderLayout.addWidget(self.p3recom)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFont(font4)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QFrame.HLine)

        self.p3HeaderLayout.addWidget(self.line_3)

        self.p3details = QPushButton(self.scrollAreaWidgetContents)
        self.p3details.setObjectName(u"p3details")
        self.p3details.setMinimumSize(QSize(60, 18))
        self.p3details.setMaximumSize(QSize(80, 100))
        self.p3details.setFont(font3)
        self.p3details.setCursor(QCursor(Qt.PointingHandCursor))
        self.p3details.setAutoFillBackground(False)
        self.p3details.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(180, 178, 178);\n"
"     border-radius: 5px;\n"
"     padding: 1px 3px\n"
"}\n"
"\n"
"QPushButton:active{\n"
"	background-color: #e7e7e8;\n"
"     border: 1px solid rgb(0, 50, 95)\n"
"}\n"
"\n"
"QPushButton:active:hover{\n"
"     border: 1px solid rgb(155, 24, 42);\n"
"}")
        self.p3details.setIcon(icon1)
        self.p3details.setIconSize(QSize(11, 11))
        self.p3details.setCheckable(True)
        self.p3details.setChecked(False)

        self.p3HeaderLayout.addWidget(self.p3details)


        self.p3Layout.addLayout(self.p3HeaderLayout)


        self.verticalLayout_9.addLayout(self.p3Layout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.profilesLayout.addWidget(self.scrollArea)


        self.verticalLayout_8.addLayout(self.profilesLayout)

        self.step3Frame = QFrame(self.content)
        self.step3Frame.setObjectName(u"step3Frame")
        self.step3Frame.setEnabled(True)
        self.step3Frame.setMinimumSize(QSize(0, 20))
        self.step3Frame.setMaximumSize(QSize(16777215, 50))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush7)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush8)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush9)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.step3Frame.setPalette(palette5)
        self.step3Frame.setStyleSheet(u".QFrame{\n"
"    border: 1px solid #00325f;\n"
"    border-radius: 5px;\n"
"}")
        self.step3Frame.setFrameShape(QFrame.Box)
        self.step3Frame.setFrameShadow(QFrame.Plain)
        self.step3Frame.setLineWidth(2)
        self.horizontalLayout_10 = QHBoxLayout(self.step3Frame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.step3step = QLabel(self.step3Frame)
        self.step3step.setObjectName(u"step3step")
        self.step3step.setMinimumSize(QSize(70, 0))
        self.step3step.setMaximumSize(QSize(100, 16777215))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.step3step.setPalette(palette6)
        self.step3step.setFont(font1)
        self.step3step.setAutoFillBackground(False)
        self.step3step.setStyleSheet(u".QLabel{\n"
"    border-radius: 5px;\n"
"    background-color: #00325f;\n"
"    padding: 1px 10px;\n"
"}")
        self.step3step.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.step3step)

        self.horizontalSpacer_5 = QSpacerItem(50, 15, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.step3title = QLabel(self.step3Frame)
        self.step3title.setObjectName(u"step3title")
        self.step3title.setFont(font2)
        self.step3title.setToolTipDuration(-1)
        self.step3title.setStyleSheet(u".QLabel{\n"
"    color: #00325f;\n"
"    padding-top: 1px;\n"
"    padding-bottom: 1px;\n"
"}")

        self.horizontalLayout_10.addWidget(self.step3title)

        self.horizontalSpacer_6 = QSpacerItem(50, 15, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.step3info = QPushButton(self.step3Frame)
        self.step3info.setObjectName(u"step3info")
        self.step3info.setMinimumSize(QSize(20, 0))
        self.step3info.setMaximumSize(QSize(30, 16777215))
        self.step3info.setCursor(QCursor(Qt.PointingHandCursor))
        self.step3info.setStyleSheet(u"QPushButton{\n"
"    padding-right: 5px\n"
"}")
        self.step3info.setIcon(icon)
        self.step3info.setFlat(True)

        self.horizontalLayout_10.addWidget(self.step3info)


        self.verticalLayout_8.addWidget(self.step3Frame)

        self.repsLayout = QVBoxLayout()
        self.repsLayout.setSpacing(10)
        self.repsLayout.setObjectName(u"repsLayout")
        self.repsLayout.setContentsMargins(10, 10, 10, 10)
        self.repsLabel = QLabel(self.content)
        self.repsLabel.setObjectName(u"repsLabel")
        self.repsLabel.setFont(font)
        self.repsLabel.setWordWrap(True)

        self.repsLayout.addWidget(self.repsLabel)

        self.repsScrollArea = QScrollArea(self.content)
        self.repsScrollArea.setObjectName(u"repsScrollArea")
        self.repsScrollArea.setFrameShape(QFrame.NoFrame)
        self.repsScrollArea.setFrameShadow(QFrame.Plain)
        self.repsScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.repsScrollArea.setWidgetResizable(True)
        self.repsScrollAreaContents = QWidget()
        self.repsScrollAreaContents.setObjectName(u"repsScrollAreaContents")
        self.repsScrollAreaContents.setGeometry(QRect(0, 0, 510, 135))
        self.verticalLayout_2 = QVBoxLayout(self.repsScrollAreaContents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.aipLayout = QVBoxLayout()
        self.aipLayout.setObjectName(u"aipLayout")
        self.aipHeaderLayout = QHBoxLayout()
        self.aipHeaderLayout.setObjectName(u"aipHeaderLayout")
        self.aipHeaderLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.aip1title = QPushButton(self.repsScrollAreaContents)
        self.aip1title.setObjectName(u"aip1title")
        self.aip1title.setMinimumSize(QSize(60, 17))
        self.aip1title.setMaximumSize(QSize(70, 100))
        self.aip1title.setFont(font3)
        self.aip1title.setCursor(QCursor(Qt.PointingHandCursor))
        self.aip1title.setAutoFillBackground(False)
        self.aip1title.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(180, 178, 178);\n"
"     border-radius: 5px;\n"
"	padding: 3px 10px\n"
"}\n"
"\n"
"QPushButton:active{\n"
"	background-color: #e7e7e8;\n"
"     border: 1px solid rgb(0, 50, 95)\n"
"}\n"
"\n"
"QPushButton:active:hover{\n"
"     border: 1px solid rgb(155, 24, 42);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(155, 24, 42);\n"
"	color: rgb(255, 255, 255);\n"
"     border: none;\n"
"}")
        self.aip1title.setCheckable(True)
        self.aip1title.setChecked(False)

        self.aipHeaderLayout.addWidget(self.aip1title)

        self.line_10 = QFrame(self.repsScrollAreaContents)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setMaximumSize(QSize(30, 16777215))
        self.line_10.setFrameShadow(QFrame.Sunken)
        self.line_10.setLineWidth(2)
        self.line_10.setFrameShape(QFrame.HLine)

        self.aipHeaderLayout.addWidget(self.line_10)

        self.aip1name = QLabel(self.repsScrollAreaContents)
        self.aip1name.setObjectName(u"aip1name")
        self.aip1name.setFont(font)
        self.aip1name.setAlignment(Qt.AlignCenter)

        self.aipHeaderLayout.addWidget(self.aip1name)

        self.line_16 = QFrame(self.repsScrollAreaContents)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShadow(QFrame.Sunken)
        self.line_16.setLineWidth(2)
        self.line_16.setFrameShape(QFrame.HLine)

        self.aipHeaderLayout.addWidget(self.line_16)

        self.aip1recom = QLabel(self.repsScrollAreaContents)
        self.aip1recom.setObjectName(u"aip1recom")
        self.aip1recom.setFont(font)
        self.aip1recom.setAlignment(Qt.AlignCenter)

        self.aipHeaderLayout.addWidget(self.aip1recom)

        self.line_11 = QFrame(self.repsScrollAreaContents)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setMinimumSize(QSize(0, 0))
        self.line_11.setMaximumSize(QSize(30, 16777215))
        self.line_11.setFrameShadow(QFrame.Sunken)
        self.line_11.setLineWidth(2)
        self.line_11.setFrameShape(QFrame.HLine)

        self.aipHeaderLayout.addWidget(self.line_11)

        self.aip1details = QPushButton(self.repsScrollAreaContents)
        self.aip1details.setObjectName(u"aip1details")
        self.aip1details.setMinimumSize(QSize(60, 18))
        self.aip1details.setMaximumSize(QSize(80, 100))
        self.aip1details.setFont(font3)
        self.aip1details.setCursor(QCursor(Qt.PointingHandCursor))
        self.aip1details.setAutoFillBackground(False)
        self.aip1details.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(180, 178, 178);\n"
"     border-radius: 5px;\n"
"     padding: 1px 3px\n"
"}\n"
"\n"
"QPushButton:active{\n"
"	background-color: #e7e7e8;\n"
"     border: 1px solid rgb(0, 50, 95)\n"
"}\n"
"\n"
"QPushButton:active:hover{\n"
"     border: 1px solid rgb(155, 24, 42);\n"
"}")
        self.aip1details.setIcon(icon1)
        self.aip1details.setIconSize(QSize(11, 11))
        self.aip1details.setCheckable(True)
        self.aip1details.setChecked(False)

        self.aipHeaderLayout.addWidget(self.aip1details)


        self.aipLayout.addLayout(self.aipHeaderLayout)

        self.aipInfo = QTextBrowser(self.repsScrollAreaContents)
        self.aipInfo.setObjectName(u"aipInfo")
        self.aipInfo.setMaximumSize(QSize(16777215, 80))
        self.aipInfo.setFont(font)
        self.aipInfo.setStyleSheet(u"")
        self.aipInfo.setFrameShape(QFrame.NoFrame)
        self.aipInfo.setFrameShadow(QFrame.Plain)
        self.aipInfo.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.aipInfo.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.aipLayout.addWidget(self.aipInfo)

        self.aipLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.aipLayout)

        self.repsScrollArea.setWidget(self.repsScrollAreaContents)

        self.repsLayout.addWidget(self.repsScrollArea)


        self.verticalLayout_8.addLayout(self.repsLayout)

        self.verticalSpacer = QSpacerItem(17, 34, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.content)
        self.info1 = QWidget()
        self.info1.setObjectName(u"info1")
        self.verticalLayout_6 = QVBoxLayout(self.info1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.info1)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(u"")
        self.textBrowser.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_6.addWidget(self.textBrowser)

        self.stackedWidget.addWidget(self.info1)
        self.info2 = QWidget()
        self.info2.setObjectName(u"info2")
        self.verticalLayout_5 = QVBoxLayout(self.info2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_4 = QTextBrowser(self.info2)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setStyleSheet(u"")
        self.textBrowser_4.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_5.addWidget(self.textBrowser_4)

        self.stackedWidget.addWidget(self.info2)
        self.info3 = QWidget()
        self.info3.setObjectName(u"info3")
        self.verticalLayout_7 = QVBoxLayout(self.info3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_5 = QTextBrowser(self.info3)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setStyleSheet(u"")
        self.textBrowser_5.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_7.addWidget(self.textBrowser_5)

        self.stackedWidget.addWidget(self.info3)

        self.leftLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addLayout(self.leftLayout)

        self.overviewFrame = QFrame(self.centralwidget)
        self.overviewFrame.setObjectName(u"overviewFrame")
        self.overviewFrame.setMinimumSize(QSize(160, 0))
        self.overviewFrame.setMaximumSize(QSize(250, 16777215))
        self.overviewFrame.setStyleSheet(u"QFrame{\n"
"    border-radius: 0;\n"
"    border: 1px solid rgb(155, 24, 42)\n"
"}")
        self.overviewFrame.setFrameShape(QFrame.StyledPanel)
        self.overviewFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.overviewFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ovTitle = QWidget(self.overviewFrame)
        self.ovTitle.setObjectName(u"ovTitle")
        self.ovTitle.setMinimumSize(QSize(0, 20))
        self.horizontalLayout = QHBoxLayout(self.ovTitle)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.ovTitle)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(130, 0))
        self.label_3.setMaximumSize(QSize(130, 16777215))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush7)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush8)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush9)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette7.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush9)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.label_3.setPalette(palette7)
        font5 = QFont()
        font5.setFamilies([u"Source Sans Pro"])
        font5.setPointSize(16)
        font5.setBold(False)
        self.label_3.setFont(font5)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u".QLabel{\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"    background-color: #00325f\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.ovTitle)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.ieTextBrowser = QTextBrowser(self.overviewFrame)
        self.ieTextBrowser.setObjectName(u"ieTextBrowser")
        self.ieTextBrowser.setMinimumSize(QSize(160, 20))
        self.ieTextBrowser.setMaximumSize(QSize(250, 16777215))
        self.ieTextBrowser.setFont(font3)
        self.ieTextBrowser.setStyleSheet(u"QTextBrowser{border: none}")
        self.ieTextBrowser.setFrameShape(QFrame.NoFrame)
        self.ieTextBrowser.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.ieTextBrowser)

        self.profileTextBrowser = QTextBrowser(self.overviewFrame)
        self.profileTextBrowser.setObjectName(u"profileTextBrowser")
        self.profileTextBrowser.setMaximumSize(QSize(16777215, 50))
        self.profileTextBrowser.setFont(font3)
        self.profileTextBrowser.setStyleSheet(u"QTextBrowser{border: none}")
        self.profileTextBrowser.setFrameShape(QFrame.NoFrame)
        self.profileTextBrowser.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.profileTextBrowser)

        self.repTextBrowser = QTextBrowser(self.overviewFrame)
        self.repTextBrowser.setObjectName(u"repTextBrowser")
        self.repTextBrowser.setFont(font3)
        self.repTextBrowser.setStyleSheet(u"QTextBrowser{border: none}")
        self.repTextBrowser.setFrameShape(QFrame.NoFrame)
        self.repTextBrowser.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.repTextBrowser)

        self.deliveryLayout = QVBoxLayout()
        self.deliveryLayout.setObjectName(u"deliveryLayout")
        self.label = QLabel(self.overviewFrame)
        self.label.setObjectName(u"label")
        font6 = QFont()
        font6.setFamilies([u"Source Sans Pro"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.label.setFont(font6)
        self.label.setStyleSheet(u"QLabel{border: none}")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setMargin(4)
        self.label.setIndent(1)

        self.deliveryLayout.addWidget(self.label)

        self.deliveryButtonsLayout = QVBoxLayout()
        self.deliveryButtonsLayout.setSpacing(0)
        self.deliveryButtonsLayout.setObjectName(u"deliveryButtonsLayout")
        self.deliveryButtonsLayout.setContentsMargins(30, -1, -1, -1)
        self.btnViewer = QRadioButton(self.overviewFrame)
        self.btnViewer.setObjectName(u"btnViewer")
        self.btnViewer.setMinimumSize(QSize(70, 20))
        self.btnViewer.setMaximumSize(QSize(16777215, 20))
        self.btnViewer.setFont(font3)
        self.btnViewer.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnViewer.setAcceptDrops(False)
        self.btnViewer.setToolTipDuration(0)
        self.btnViewer.setStyleSheet(u"QRadioButton{\n"
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
"    border: 3px solid #9b182a;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border: 1px solid #9b182a;\n"
"}")
        self.btnViewer.setIconSize(QSize(12, 12))
        self.btnViewer.setChecked(True)

        self.deliveryButtonsLayout.addWidget(self.btnViewer)

        self.btnDownload = QRadioButton(self.overviewFrame)
        self.btnDownload.setObjectName(u"btnDownload")
        self.btnDownload.setMinimumSize(QSize(70, 20))
        self.btnDownload.setMaximumSize(QSize(16777215, 20))
        self.btnDownload.setFont(font3)
        self.btnDownload.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDownload.setAcceptDrops(False)
        self.btnDownload.setToolTipDuration(0)
        self.btnDownload.setStyleSheet(u"QRadioButton{\n"
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
"    border: 3px solid #9b182a;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border: 1px solid #9b182a;\n"
"}")
        self.btnDownload.setIconSize(QSize(12, 12))
        self.btnDownload.setChecked(False)

        self.deliveryButtonsLayout.addWidget(self.btnDownload)

        self.btnBoth = QRadioButton(self.overviewFrame)
        self.btnBoth.setObjectName(u"btnBoth")
        self.btnBoth.setMinimumSize(QSize(70, 20))
        self.btnBoth.setMaximumSize(QSize(16777215, 20))
        self.btnBoth.setFont(font3)
        self.btnBoth.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnBoth.setAcceptDrops(False)
        self.btnBoth.setToolTipDuration(0)
        self.btnBoth.setStyleSheet(u"QRadioButton{\n"
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
"    border: 3px solid #9b182a;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border: 1px solid #9b182a;\n"
"}")
        self.btnBoth.setIconSize(QSize(12, 12))
        self.btnBoth.setChecked(False)

        self.deliveryButtonsLayout.addWidget(self.btnBoth)


        self.deliveryLayout.addLayout(self.deliveryButtonsLayout)


        self.verticalLayout.addLayout(self.deliveryLayout)

        self.verticalSpacer_3 = QSpacerItem(17, 37, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.ovButtonLayout = QHBoxLayout()
        self.ovButtonLayout.setObjectName(u"ovButtonLayout")
        self.ovButtonLayout.setContentsMargins(-1, -1, 20, -1)
        self.horizontalSpacer_7 = QSpacerItem(94, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ovButtonLayout.addItem(self.horizontalSpacer_7)

        self.goButton = QPushButton(self.overviewFrame)
        self.goButton.setObjectName(u"goButton")
        self.goButton.setMinimumSize(QSize(60, 0))
        self.goButton.setMaximumSize(QSize(60, 16777215))
        self.goButton.setFont(font6)
        self.goButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.goButton.setAutoFillBackground(False)
        self.goButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(180, 178, 178);\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:active{\n"
"	background-color: #e7e7e8;\n"
"     border: 1px solid #00325f\n"
"}\n"
"\n"
"QPushButton:active:hover{\n"
"     border: 1px solid rgb(155, 24, 42);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(155, 24, 42);\n"
"     border: 1px solid rgb(155, 24, 42);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.goButton.setCheckable(True)
        self.goButton.setChecked(False)

        self.ovButtonLayout.addWidget(self.goButton)


        self.verticalLayout.addLayout(self.ovButtonLayout)

        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(4, 1)

        self.horizontalLayout_2.addWidget(self.overviewFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Base, brush1)
        brush10 = QBrush(QColor(231, 231, 232, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        self.statusbar.setPalette(palette8)
        self.statusbar.setAutoFillBackground(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DIP Request Viewer", None))
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.centralwidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.btnDIP.setStatusTip(QCoreApplication.translate("MainWindow", u"DIP Anforderung", None))
#endif // QT_CONFIG(statustip)
        self.btnDIP.setText(QCoreApplication.translate("MainWindow", u"DIP-Generierung", None))
#if QT_CONFIG(statustip)
        self.btnHelp1.setStatusTip(QCoreApplication.translate("MainWindow", u"Hilfe: Was sind Profile?", None))
#endif // QT_CONFIG(statustip)
        self.btnHelp1.setText(QCoreApplication.translate("MainWindow", u"Was sind DIP-Profile?", None))
#if QT_CONFIG(statustip)
        self.btnHelp2.setStatusTip(QCoreApplication.translate("MainWindow", u"Hilfe: Was sind Repr\u00e4sentationen?", None))
#endif // QT_CONFIG(statustip)
        self.btnHelp2.setText(QCoreApplication.translate("MainWindow", u"Was sind Repr\u00e4sentationen?", None))
#if QT_CONFIG(statustip)
        self.btnHelp3.setStatusTip(QCoreApplication.translate("MainWindow", u"Hilfe: Programm-Info", None))
#endif // QT_CONFIG(statustip)
        self.btnHelp3.setText(QCoreApplication.translate("MainWindow", u"Programm-Info", None))
        self.step1step.setText(QCoreApplication.translate("MainWindow", u"Schritt 1", None))
        self.step1title.setText(QCoreApplication.translate("MainWindow", u"Archivale w\u00e4hlen", None))
#if QT_CONFIG(tooltip)
        self.step1info.setToolTip(QCoreApplication.translate("MainWindow", u"Hilfe", None))
#endif // QT_CONFIG(tooltip)
        self.step1info.setText("")
        self.step2step.setText(QCoreApplication.translate("MainWindow", u"Schritt 2", None))
        self.step2title.setText(QCoreApplication.translate("MainWindow", u"DIP-Profil w\u00e4hlen", None))
#if QT_CONFIG(tooltip)
        self.step2info.setToolTip(QCoreApplication.translate("MainWindow", u"Hilfe", None))
#endif // QT_CONFIG(tooltip)
        self.step2info.setText("")
        self.profilesLabel.setText(QCoreApplication.translate("MainWindow", u"W\u00e4hlen Sie hier, wie die technischen Daten des Archivales f\u00fcr Sie aufbereitet werden sollen!", None))
        self.p0title.setText(QCoreApplication.translate("MainWindow", u"Profil 0 - Rohdaten", u"p0 Titel"))
        self.p0recom.setText(QCoreApplication.translate("MainWindow", u"Empfohlen f\u00fcr...", None))
        self.p0details.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.p0Info.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Source Sans Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Dies ist ein Platzhaltertext - yeah.</p></body></html>", None))
        self.p1_title.setText(QCoreApplication.translate("MainWindow", u"Profil 1 - Standard", None))
        self.p1recom.setText(QCoreApplication.translate("MainWindow", u"Empfohlen f\u00fcr...", None))
        self.p1details.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.p2title.setText(QCoreApplication.translate("MainWindow", u"Profil 2 - Wissenschaftlich", None))
        self.p2recom.setText(QCoreApplication.translate("MainWindow", u"Empfohlen f\u00fcr...", None))
        self.p2details.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.p3title.setText(QCoreApplication.translate("MainWindow", u"Profil 3 - Technisch", None))
        self.p3recom.setText(QCoreApplication.translate("MainWindow", u"Empfohlen f\u00fcr...", None))
        self.p3details.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.step3step.setText(QCoreApplication.translate("MainWindow", u"Schritt 3", None))
        self.step3title.setText(QCoreApplication.translate("MainWindow", u"Repr\u00e4sentationen w\u00e4hlen", None))
#if QT_CONFIG(tooltip)
        self.step3info.setToolTip(QCoreApplication.translate("MainWindow", u"Hilfe", None))
#endif // QT_CONFIG(tooltip)
        self.step3info.setText("")
        self.repsLabel.setText(QCoreApplication.translate("MainWindow", u"W\u00e4hlen Sie hier, welche technischen Repr\u00e4sentationen des Archivales Sie sehen wollen!", None))
        self.aip1title.setText(QCoreApplication.translate("MainWindow", u"AIP 1", None))
        self.aip1name.setText(QCoreApplication.translate("MainWindow", u"Ursprung", None))
        self.aip1recom.setText(QCoreApplication.translate("MainWindow", u"Empfohlen f\u00fcr...", None))
        self.aip1details.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.aipInfo.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Source Sans Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Dies ist ein Platzhaltertext - yeah. Dies ist ein Platzhaltertext - yeah. Dies ist ein Platzhaltertext - yeah. Dies ist ein Platzhaltertext - yeah. Dies ist ein Platzhaltertext - yeah. Dies ist ein Platzhaltertext - yeah. Dies ist ein Platzhaltertext - yeah. Dies ist ein Platzhaltertext - yeah. </p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Source Sans Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:4px; margin-bottom:2px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Maintitle</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</p>\n"
"<p style=\" margin-top:8px; margin-bottom:2px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Subtitle</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-"
                        "indent:0px;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</p>\n"
"<p style=\" margin-top:0px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</p>\n"
"<p style=\" margin-top:0px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 1</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 2</li>\n"
"<li style=\" margin-top:0p"
                        "x; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 3</li></ol>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 1</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 2</li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 3</li></ul>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt"
                        "; font-weight:600;\">Test</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:600;\">Test2</span></p></td></tr>\n"
"<tr>\n"
"<td></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">Test4</span></p></td></tr></table></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:4px; margin-bottom:2px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Source Sans Pro'; font-size:16pt; font-weight:600;\">Maintitle</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Source Sans Pro'; font-size:12pt;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</span></p>\n"
"<p style=\" margin-top:8px; margin-bottom:2px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Source Sans Pro'; font-size:14pt;\">Su"
                        "btitle</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Source Sans Pro'; font-size:12pt;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Source Sans Pro'; font-size:12pt;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Source Sans Pro'; font-size:12pt;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-rig"
                        "ht: 0px; -qt-list-indent: 1;\"><li style=\" font-family:'Source Sans Pro'; font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 1</li>\n"
"<li style=\" font-family:'Source Sans Pro'; font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 2</li>\n"
"<li style=\" font-family:'Source Sans Pro'; font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 3</li></ol></body></html>", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Source Sans Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:4px; margin-bottom:2px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Maintitle</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</p>\n"
"<p style=\" margin-top:8px; margin-bottom:2px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Subtitle</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-"
                        "indent:0px;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</p>\n"
"<p style=\" margin-top:0px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</p>\n"
"<p style=\" margin-top:0px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 1</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 2</li>\n"
"<li style=\" margin-top:0p"
                        "x; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 3</li></ol></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ihre Auswahl", None))
        self.ieTextBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Source Sans Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Signatur:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Lorem Ipsum</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Titel:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Lorem Ipsum</p>\n"
"<p style=\" margin-top:0px; margin-bott"
                        "om:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Laufzeit:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Lorem Ipsum</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Enth\u00e4lt:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Lorem Ipsum</p></body></html>", None))
        self.profileTextBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Source Sans Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">DIP-Profil</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">0 (Rohdaten)</p></body></html>", None))
        self.repTextBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Source Sans Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Repr\u00e4sentationen</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">1 (Ursprung)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">2 (Repr\u00e4sentation)</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bereitstellung", None))
#if QT_CONFIG(tooltip)
        self.btnViewer.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btnViewer.setText(QCoreApplication.translate("MainWindow", u"Viewer", None))
#if QT_CONFIG(tooltip)
        self.btnDownload.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btnDownload.setText(QCoreApplication.translate("MainWindow", u"Download", None))
#if QT_CONFIG(tooltip)
        self.btnBoth.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btnBoth.setText(QCoreApplication.translate("MainWindow", u"Beides", None))
#if QT_CONFIG(statustip)
        self.goButton.setStatusTip(QCoreApplication.translate("MainWindow", u"DIP anfordern", None))
#endif // QT_CONFIG(statustip)
        self.goButton.setText(QCoreApplication.translate("MainWindow", u"Los", None))
    # retranslateUi

