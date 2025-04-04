# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfirmDeletion.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
import Icons.TaxiCal_Icons_rc

class Ui_ConfirmDeletion(object):
    def setupUi(self, ConfirmDeletion):
        if not ConfirmDeletion.objectName():
            ConfirmDeletion.setObjectName(u"ConfirmDeletion")
        ConfirmDeletion.setWindowModality(Qt.WindowModality.ApplicationModal)
        ConfirmDeletion.resize(400, 154)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        ConfirmDeletion.setFont(font)
        self.gridLayout = QGridLayout(ConfirmDeletion)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_Inform = QLabel(ConfirmDeletion)
        self.lb_Inform.setObjectName(u"lb_Inform")

        self.gridLayout.addWidget(self.lb_Inform, 0, 0, 1, 3)

        self.pb_Confirm = QPushButton(ConfirmDeletion)
        self.pb_Confirm.setObjectName(u"pb_Confirm")
        self.pb_Confirm.setEnabled(False)
        icon = QIcon()
        icon.addFile(u":/Buttons/Confirm2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Confirm.setIcon(icon)
        self.pb_Confirm.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.pb_Confirm, 3, 2, 1, 1)

        self.pb_Cancel = QPushButton(ConfirmDeletion)
        self.pb_Cancel.setObjectName(u"pb_Cancel")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/Cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Cancel.setIcon(icon1)
        self.pb_Cancel.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.pb_Cancel, 3, 1, 1, 1)

        self.lb_Passcode = QLabel(ConfirmDeletion)
        self.lb_Passcode.setObjectName(u"lb_Passcode")

        self.gridLayout.addWidget(self.lb_Passcode, 1, 0, 1, 1)

        self.le_Passcode = QLineEdit(ConfirmDeletion)
        self.le_Passcode.setObjectName(u"le_Passcode")
        self.le_Passcode.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.le_Passcode, 1, 1, 1, 2)

        self.lb_Messege = QLabel(ConfirmDeletion)
        self.lb_Messege.setObjectName(u"lb_Messege")

        self.gridLayout.addWidget(self.lb_Messege, 2, 0, 1, 3)


        self.retranslateUi(ConfirmDeletion)

        QMetaObject.connectSlotsByName(ConfirmDeletion)
    # setupUi

    def retranslateUi(self, ConfirmDeletion):
        ConfirmDeletion.setWindowTitle(QCoreApplication.translate("ConfirmDeletion", u"Confirm Deletion", None))
        self.lb_Inform.setText(QCoreApplication.translate("ConfirmDeletion", u"Input Passcode to confirm deletion.", None))
        self.pb_Confirm.setText(QCoreApplication.translate("ConfirmDeletion", u"Confirm", None))
        self.pb_Cancel.setText(QCoreApplication.translate("ConfirmDeletion", u"Cancel", None))
        self.lb_Passcode.setText(QCoreApplication.translate("ConfirmDeletion", u"Passcode", None))
        self.lb_Messege.setText("")
    # retranslateUi

