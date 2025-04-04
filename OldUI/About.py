# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'About.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QSpacerItem, QToolButton, QWidget)
import Icons.TaxiCal_Icons_rc

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.setWindowModality(Qt.WindowModality.ApplicationModal)
        About.resize(372, 318)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        About.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Buttons/About.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        About.setWindowIcon(icon)
        self.gridLayout = QGridLayout(About)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(About)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_Blank3 = QLabel(self.groupBox)
        self.lb_Blank3.setObjectName(u"lb_Blank3")

        self.gridLayout_2.addWidget(self.lb_Blank3, 6, 0, 1, 1)

        self.lb_JasonCodesQt = QLabel(self.groupBox)
        self.lb_JasonCodesQt.setObjectName(u"lb_JasonCodesQt")

        self.gridLayout_2.addWidget(self.lb_JasonCodesQt, 5, 1, 1, 1)

        self.lb_Blank1 = QLabel(self.groupBox)
        self.lb_Blank1.setObjectName(u"lb_Blank1")

        self.gridLayout_2.addWidget(self.lb_Blank1, 3, 0, 1, 1)

        self.tb_MyGmail = QToolButton(self.groupBox)
        self.tb_MyGmail.setObjectName(u"tb_MyGmail")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/Gmail.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_MyGmail.setIcon(icon1)
        self.tb_MyGmail.setIconSize(QSize(26, 26))

        self.gridLayout_2.addWidget(self.tb_MyGmail, 1, 3, 1, 1)

        self.tb_Freepik = QToolButton(self.groupBox)
        self.tb_Freepik.setObjectName(u"tb_Freepik")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/Freepik.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_Freepik.setIcon(icon2)
        self.tb_Freepik.setIconSize(QSize(26, 26))

        self.gridLayout_2.addWidget(self.tb_Freepik, 7, 2, 1, 1)

        self.lb_ChatGPT = QLabel(self.groupBox)
        self.lb_ChatGPT.setObjectName(u"lb_ChatGPT")

        self.gridLayout_2.addWidget(self.lb_ChatGPT, 6, 1, 1, 1)

        self.lb_CodeWithMosh = QLabel(self.groupBox)
        self.lb_CodeWithMosh.setObjectName(u"lb_CodeWithMosh")

        self.gridLayout_2.addWidget(self.lb_CodeWithMosh, 3, 1, 1, 1)

        self.lb_VersionNumber = QLabel(self.groupBox)
        self.lb_VersionNumber.setObjectName(u"lb_VersionNumber")

        self.gridLayout_2.addWidget(self.lb_VersionNumber, 0, 1, 1, 1)

        self.tb_ChatGPT = QToolButton(self.groupBox)
        self.tb_ChatGPT.setObjectName(u"tb_ChatGPT")
        self.tb_ChatGPT.setEnabled(True)
        icon3 = QIcon()
        icon3.addFile(u":/Buttons/Chatgpt.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_ChatGPT.setIcon(icon3)
        self.tb_ChatGPT.setIconSize(QSize(26, 26))

        self.gridLayout_2.addWidget(self.tb_ChatGPT, 6, 2, 1, 1)

        self.lb_Version = QLabel(self.groupBox)
        self.lb_Version.setObjectName(u"lb_Version")

        self.gridLayout_2.addWidget(self.lb_Version, 0, 0, 1, 1)

        self.lb_Credits = QLabel(self.groupBox)
        self.lb_Credits.setObjectName(u"lb_Credits")

        self.gridLayout_2.addWidget(self.lb_Credits, 2, 0, 1, 1)

        self.lb_Freepik = QLabel(self.groupBox)
        self.lb_Freepik.setObjectName(u"lb_Freepik")

        self.gridLayout_2.addWidget(self.lb_Freepik, 7, 1, 1, 1)

        self.lb_Blank2 = QLabel(self.groupBox)
        self.lb_Blank2.setObjectName(u"lb_Blank2")

        self.gridLayout_2.addWidget(self.lb_Blank2, 5, 0, 1, 1)

        self.tb_MyYouTube = QToolButton(self.groupBox)
        self.tb_MyYouTube.setObjectName(u"tb_MyYouTube")
        icon4 = QIcon()
        icon4.addFile(u":/Buttons/YouTube.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_MyYouTube.setIcon(icon4)
        self.tb_MyYouTube.setIconSize(QSize(26, 26))

        self.gridLayout_2.addWidget(self.tb_MyYouTube, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 9, 0, 1, 5)

        self.tb_Mosh_YouTube = QToolButton(self.groupBox)
        self.tb_Mosh_YouTube.setObjectName(u"tb_Mosh_YouTube")
        self.tb_Mosh_YouTube.setIcon(icon4)
        self.tb_Mosh_YouTube.setIconSize(QSize(26, 26))

        self.gridLayout_2.addWidget(self.tb_Mosh_YouTube, 3, 2, 1, 1)

        self.tb_MoshWebsite = QToolButton(self.groupBox)
        self.tb_MoshWebsite.setObjectName(u"tb_MoshWebsite")
        icon5 = QIcon()
        icon5.addFile(u":/Buttons/MoshWebsite.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_MoshWebsite.setIcon(icon5)
        self.tb_MoshWebsite.setIconSize(QSize(26, 26))

        self.gridLayout_2.addWidget(self.tb_MoshWebsite, 3, 3, 1, 1)

        self.lb_Developer = QLabel(self.groupBox)
        self.lb_Developer.setObjectName(u"lb_Developer")

        self.gridLayout_2.addWidget(self.lb_Developer, 1, 0, 1, 1)

        self.tb_JasonYouTube = QToolButton(self.groupBox)
        self.tb_JasonYouTube.setObjectName(u"tb_JasonYouTube")
        self.tb_JasonYouTube.setIcon(icon4)
        self.tb_JasonYouTube.setIconSize(QSize(26, 26))

        self.gridLayout_2.addWidget(self.tb_JasonYouTube, 5, 2, 1, 1)

        self.lb_Blank4 = QLabel(self.groupBox)
        self.lb_Blank4.setObjectName(u"lb_Blank4")

        self.gridLayout_2.addWidget(self.lb_Blank4, 7, 0, 1, 1)

        self.lb_DeveloperName = QLabel(self.groupBox)
        self.lb_DeveloperName.setObjectName(u"lb_DeveloperName")

        self.gridLayout_2.addWidget(self.lb_DeveloperName, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 4, 8, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"About", None))
        self.groupBox.setTitle(QCoreApplication.translate("About", u"TaxiCal", None))
        self.lb_Blank3.setText("")
        self.lb_JasonCodesQt.setText(QCoreApplication.translate("About", u"Jason Codes Qt", None))
        self.lb_Blank1.setText("")
        self.tb_MyGmail.setText("")
        self.tb_Freepik.setText("")
        self.lb_ChatGPT.setText(QCoreApplication.translate("About", u"ChatGPT", None))
        self.lb_CodeWithMosh.setText(QCoreApplication.translate("About", u"Code With Mosh", None))
        self.lb_VersionNumber.setText(QCoreApplication.translate("About", u"3.3", None))
        self.tb_ChatGPT.setText("")
        self.lb_Version.setText(QCoreApplication.translate("About", u"Version:", None))
        self.lb_Credits.setText(QCoreApplication.translate("About", u"Credits:-", None))
        self.lb_Freepik.setText(QCoreApplication.translate("About", u"Freepik", None))
        self.lb_Blank2.setText("")
        self.tb_MyYouTube.setText("")
        self.tb_Mosh_YouTube.setText("")
        self.tb_MoshWebsite.setText("")
        self.lb_Developer.setText(QCoreApplication.translate("About", u"Developer:", None))
        self.tb_JasonYouTube.setText("")
        self.lb_Blank4.setText("")
        self.lb_DeveloperName.setText(QCoreApplication.translate("About", u"Abdalla Elsoni", None))
    # retranslateUi

