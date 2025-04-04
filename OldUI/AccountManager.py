# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AccountManager.ui'
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

class Ui_AccountManager(object):
    def setupUi(self, AccountManager):
        if not AccountManager.objectName():
            AccountManager.setObjectName(u"AccountManager")
        AccountManager.setWindowModality(Qt.WindowModality.ApplicationModal)
        AccountManager.resize(331, 184)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        AccountManager.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/Account.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        AccountManager.setWindowIcon(icon)
        self.gridLayout = QGridLayout(AccountManager)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.gb_AccountName = QGroupBox(AccountManager)
        self.gb_AccountName.setObjectName(u"gb_AccountName")
        self.gridLayout_2 = QGridLayout(self.gb_AccountName)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.gb_AccountName)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.tb_DeleteAccount = QToolButton(self.gb_AccountName)
        self.tb_DeleteAccount.setObjectName(u"tb_DeleteAccount")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/Delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_DeleteAccount.setIcon(icon1)
        self.tb_DeleteAccount.setIconSize(QSize(26, 26))

        self.gridLayout_2.addWidget(self.tb_DeleteAccount, 0, 1, 1, 1)

        self.label_2 = QLabel(self.gb_AccountName)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.tb_ChangeID = QToolButton(self.gb_AccountName)
        self.tb_ChangeID.setObjectName(u"tb_ChangeID")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/ChangeID.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_ChangeID.setIcon(icon2)
        self.tb_ChangeID.setIconSize(QSize(26, 26))

        self.gridLayout_2.addWidget(self.tb_ChangeID, 1, 1, 1, 1)

        self.label_3 = QLabel(self.gb_AccountName)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.tb_Change_Passcode = QToolButton(self.gb_AccountName)
        self.tb_Change_Passcode.setObjectName(u"tb_Change_Passcode")
        icon3 = QIcon()
        icon3.addFile(u":/Buttons/RedLock1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_Change_Passcode.setIcon(icon3)
        self.tb_Change_Passcode.setIconSize(QSize(26, 26))

        self.gridLayout_2.addWidget(self.tb_Change_Passcode, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.gb_AccountName, 0, 0, 1, 1)


        self.retranslateUi(AccountManager)

        QMetaObject.connectSlotsByName(AccountManager)
    # setupUi

    def retranslateUi(self, AccountManager):
        AccountManager.setWindowTitle(QCoreApplication.translate("AccountManager", u"Account Manager", None))
        self.gb_AccountName.setTitle(QCoreApplication.translate("AccountManager", u"Account", None))
        self.label.setText(QCoreApplication.translate("AccountManager", u"Delete Account", None))
        self.tb_DeleteAccount.setText("")
        self.label_2.setText(QCoreApplication.translate("AccountManager", u"Change ID", None))
        self.tb_ChangeID.setText("")
        self.label_3.setText(QCoreApplication.translate("AccountManager", u"Change Passcode", None))
        self.tb_Change_Passcode.setText("")
    # retranslateUi

