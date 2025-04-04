# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChangePasscode.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
import Icons.TaxiCal_Icons_rc

class Ui_ChangePasscode(object):
    def setupUi(self, ChangePasscode):
        if not ChangePasscode.objectName():
            ChangePasscode.setObjectName(u"ChangePasscode")
        ChangePasscode.setWindowModality(Qt.WindowModality.ApplicationModal)
        ChangePasscode.resize(400, 166)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        ChangePasscode.setFont(font)
        self.gridLayout = QGridLayout(ChangePasscode)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_Change = QPushButton(ChangePasscode)
        self.pb_Change.setObjectName(u"pb_Change")
        self.pb_Change.setEnabled(False)
        icon = QIcon()
        icon.addFile(u":/Buttons/Confirm2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Change.setIcon(icon)
        self.pb_Change.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pb_Change, 4, 2, 1, 1)

        self.le_OldPasscode = QLineEdit(ChangePasscode)
        self.le_OldPasscode.setObjectName(u"le_OldPasscode")
        self.le_OldPasscode.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.le_OldPasscode, 0, 1, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 3)

        self.lb_OldPasscode = QLabel(ChangePasscode)
        self.lb_OldPasscode.setObjectName(u"lb_OldPasscode")

        self.gridLayout.addWidget(self.lb_OldPasscode, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 0, 1, 1)

        self.le_NewPasscode = QLineEdit(ChangePasscode)
        self.le_NewPasscode.setObjectName(u"le_NewPasscode")
        self.le_NewPasscode.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.le_NewPasscode, 1, 1, 1, 2)

        self.lb_NewPasscode = QLabel(ChangePasscode)
        self.lb_NewPasscode.setObjectName(u"lb_NewPasscode")

        self.gridLayout.addWidget(self.lb_NewPasscode, 1, 0, 1, 1)

        self.pb_Cancel = QPushButton(ChangePasscode)
        self.pb_Cancel.setObjectName(u"pb_Cancel")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/Cross.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Cancel.setIcon(icon1)
        self.pb_Cancel.setIconSize(QSize(26, 26))

        self.gridLayout.addWidget(self.pb_Cancel, 4, 1, 1, 1)

        self.lb_Messege = QLabel(ChangePasscode)
        self.lb_Messege.setObjectName(u"lb_Messege")
        self.lb_Messege.setFont(font)
        self.lb_Messege.setStyleSheet(u"color:red;")

        self.gridLayout.addWidget(self.lb_Messege, 2, 0, 1, 3)


        self.retranslateUi(ChangePasscode)

        QMetaObject.connectSlotsByName(ChangePasscode)
    # setupUi

    def retranslateUi(self, ChangePasscode):
        ChangePasscode.setWindowTitle(QCoreApplication.translate("ChangePasscode", u"Change Passcode", None))
        self.pb_Change.setText(QCoreApplication.translate("ChangePasscode", u"Change", None))
        self.lb_OldPasscode.setText(QCoreApplication.translate("ChangePasscode", u"Old Passcode", None))
        self.lb_NewPasscode.setText(QCoreApplication.translate("ChangePasscode", u"New Passcode", None))
        self.pb_Cancel.setText(QCoreApplication.translate("ChangePasscode", u"Cancel", None))
        self.lb_Messege.setText("")
    # retranslateUi

