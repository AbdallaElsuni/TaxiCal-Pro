# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Database.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
import Icons.TaxiCal_Icons_rc

class Ui_NewRegistry(object):
    def setupUi(self, NewRegistry):
        if not NewRegistry.objectName():
            NewRegistry.setObjectName(u"NewRegistry")
        NewRegistry.setWindowModality(Qt.WindowModality.ApplicationModal)
        NewRegistry.resize(400, 214)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        NewRegistry.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/Database2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        NewRegistry.setWindowIcon(icon)
        self.gridLayout = QGridLayout(NewRegistry)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.lb_Messege = QLabel(NewRegistry)
        self.lb_Messege.setObjectName(u"lb_Messege")
        self.lb_Messege.setFont(font)
        self.lb_Messege.setStyleSheet(u"color:red;")

        self.gridLayout.addWidget(self.lb_Messege, 2, 0, 1, 3)

        self.gb_Credentials = QGroupBox(NewRegistry)
        self.gb_Credentials.setObjectName(u"gb_Credentials")
        self.gridLayout_2 = QGridLayout(self.gb_Credentials)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_Passcode = QLabel(self.gb_Credentials)
        self.lb_Passcode.setObjectName(u"lb_Passcode")
        self.lb_Passcode.setFont(font)

        self.gridLayout_2.addWidget(self.lb_Passcode, 1, 0, 1, 1)

        self.le_Passcode = QLineEdit(self.gb_Credentials)
        self.le_Passcode.setObjectName(u"le_Passcode")

        self.gridLayout_2.addWidget(self.le_Passcode, 1, 1, 1, 1)

        self.lb_ID = QLabel(self.gb_Credentials)
        self.lb_ID.setObjectName(u"lb_ID")
        self.lb_ID.setFont(font)

        self.gridLayout_2.addWidget(self.lb_ID, 0, 0, 1, 1)

        self.pb_Generate = QPushButton(self.gb_Credentials)
        self.pb_Generate.setObjectName(u"pb_Generate")
        self.pb_Generate.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/Generate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Generate.setIcon(icon1)
        self.pb_Generate.setIconSize(QSize(26, 26))

        self.gridLayout_2.addWidget(self.pb_Generate, 1, 2, 1, 1)

        self.le_ID = QLineEdit(self.gb_Credentials)
        self.le_ID.setObjectName(u"le_ID")
        self.le_ID.setEnabled(False)
        self.le_ID.setFont(font)
        self.le_ID.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_2.addWidget(self.le_ID, 0, 1, 1, 2)


        self.gridLayout.addWidget(self.gb_Credentials, 0, 0, 1, 4)

        self.pb_Register = QPushButton(NewRegistry)
        self.pb_Register.setObjectName(u"pb_Register")
        self.pb_Register.setEnabled(False)
        self.pb_Register.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/Register.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Register.setIcon(icon2)
        self.pb_Register.setIconSize(QSize(26, 26))

        self.gridLayout.addWidget(self.pb_Register, 3, 2, 1, 1)

        self.pb_Copy = QPushButton(NewRegistry)
        self.pb_Copy.setObjectName(u"pb_Copy")
        icon3 = QIcon()
        icon3.addFile(u":/Buttons/Copy.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Copy.setIcon(icon3)
        self.pb_Copy.setIconSize(QSize(26, 26))

        self.gridLayout.addWidget(self.pb_Copy, 3, 1, 1, 1)


        self.retranslateUi(NewRegistry)

        QMetaObject.connectSlotsByName(NewRegistry)
    # setupUi

    def retranslateUi(self, NewRegistry):
        NewRegistry.setWindowTitle(QCoreApplication.translate("NewRegistry", u"Database", None))
        self.lb_Messege.setText("")
        self.gb_Credentials.setTitle(QCoreApplication.translate("NewRegistry", u"Credentials", None))
        self.lb_Passcode.setText(QCoreApplication.translate("NewRegistry", u"Passcode", None))
        self.lb_ID.setText(QCoreApplication.translate("NewRegistry", u"ID", None))
        self.pb_Generate.setText("")
        self.pb_Register.setText(QCoreApplication.translate("NewRegistry", u" Register ", None))
        self.pb_Copy.setText("")
    # retranslateUi

