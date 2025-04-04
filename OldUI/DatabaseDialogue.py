# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DatabaseDialogue.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_DatabaseQuestion(object):
    def setupUi(self, DatabaseQuestion):
        if not DatabaseQuestion.objectName():
            DatabaseQuestion.setObjectName(u"DatabaseQuestion")
        DatabaseQuestion.setWindowModality(Qt.WindowModality.ApplicationModal)
        DatabaseQuestion.resize(407, 130)
        self.gridLayout = QGridLayout(DatabaseQuestion)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_Cancel = QPushButton(DatabaseQuestion)
        self.pb_Cancel.setObjectName(u"pb_Cancel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.pb_Cancel.setFont(font)

        self.gridLayout.addWidget(self.pb_Cancel, 1, 1, 1, 1)

        self.pb_OK = QPushButton(DatabaseQuestion)
        self.pb_OK.setObjectName(u"pb_OK")
        self.pb_OK.setFont(font)
        self.pb_OK.setAutoDefault(False)

        self.gridLayout.addWidget(self.pb_OK, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.lb_DatabaseQuestion = QLabel(DatabaseQuestion)
        self.lb_DatabaseQuestion.setObjectName(u"lb_DatabaseQuestion")
        self.lb_DatabaseQuestion.setFont(font)

        self.gridLayout.addWidget(self.lb_DatabaseQuestion, 0, 0, 1, 3)

        QWidget.setTabOrder(self.pb_OK, self.pb_Cancel)

        self.retranslateUi(DatabaseQuestion)

        self.pb_OK.setDefault(True)


        QMetaObject.connectSlotsByName(DatabaseQuestion)
    # setupUi

    def retranslateUi(self, DatabaseQuestion):
        DatabaseQuestion.setWindowTitle(QCoreApplication.translate("DatabaseQuestion", u"Database?", None))
        self.pb_Cancel.setText(QCoreApplication.translate("DatabaseQuestion", u"Cancel", None))
        self.pb_OK.setText(QCoreApplication.translate("DatabaseQuestion", u"OK", None))
        self.lb_DatabaseQuestion.setText(QCoreApplication.translate("DatabaseQuestion", u"Do you want to be added to database?", None))
    # retranslateUi

