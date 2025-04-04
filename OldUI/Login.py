# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
import Icons.TaxiCal_Icons_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.setWindowModality(Qt.WindowModality.ApplicationModal)
        Login.resize(388, 206)
        icon = QIcon()
        icon.addFile(u":/Main/Account.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Login.setWindowIcon(icon)
        self.formLayout = QFormLayout(Login)
        self.formLayout.setObjectName(u"formLayout")
        self.groupBox = QGroupBox(Login)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.formLayout_2 = QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lb_Client_ID = QLabel(self.groupBox)
        self.lb_Client_ID.setObjectName(u"lb_Client_ID")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lb_Client_ID)

        self.le_Client_ID = QLineEdit(self.groupBox)
        self.le_Client_ID.setObjectName(u"le_Client_ID")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.le_Client_ID)

        self.lb_Client_Passcode = QLabel(self.groupBox)
        self.lb_Client_Passcode.setObjectName(u"lb_Client_Passcode")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lb_Client_Passcode)

        self.le_Passcode = QLineEdit(self.groupBox)
        self.le_Passcode.setObjectName(u"le_Passcode")
        self.le_Passcode.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.le_Passcode)

        self.lb_Messege = QLabel(self.groupBox)
        self.lb_Messege.setObjectName(u"lb_Messege")

        self.formLayout_2.setWidget(2, QFormLayout.SpanningRole, self.lb_Messege)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.groupBox)

        self.pb_Login = QPushButton(Login)
        self.pb_Login.setObjectName(u"pb_Login")
        self.pb_Login.setEnabled(False)
        self.pb_Login.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/Login_Cropped.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Login.setIcon(icon1)
        self.pb_Login.setIconSize(QSize(25, 25))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pb_Login)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.groupBox.setTitle(QCoreApplication.translate("Login", u"Credentials", None))
        self.lb_Client_ID.setText(QCoreApplication.translate("Login", u"Client ID", None))
        self.le_Client_ID.setPlaceholderText(QCoreApplication.translate("Login", u"   XXXX-XXXX-XXXX-XXXX", None))
        self.lb_Client_Passcode.setText(QCoreApplication.translate("Login", u"Passcode", None))
        self.le_Passcode.setPlaceholderText(QCoreApplication.translate("Login", u"                *********", None))
        self.lb_Messege.setText("")
        self.pb_Login.setText(QCoreApplication.translate("Login", u"Login", None))
    # retranslateUi

