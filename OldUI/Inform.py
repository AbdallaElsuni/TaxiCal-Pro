# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Inform.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QWidget)
import Icons.TaxiCal_Icons_rc

class Ui_Inform(object):
    def setupUi(self, Inform):
        if not Inform.objectName():
            Inform.setObjectName(u"Inform")
        Inform.setWindowModality(Qt.WindowModality.ApplicationModal)
        Inform.resize(434, 334)
        icon = QIcon()
        icon.addFile(u":/Main/Results.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Inform.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Inform)
        self.gridLayout.setObjectName(u"gridLayout")
        self.te_Inform = QTextEdit(Inform)
        self.te_Inform.setObjectName(u"te_Inform")
        self.te_Inform.setEnabled(True)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.te_Inform.setFont(font)
        self.te_Inform.setReadOnly(True)

        self.gridLayout.addWidget(self.te_Inform, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.pb_OK = QPushButton(Inform)
        self.pb_OK.setObjectName(u"pb_OK")
        self.pb_OK.setFont(font)
        self.pb_OK.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout.addWidget(self.pb_OK, 1, 2, 1, 1)

        self.pb_Copy = QPushButton(Inform)
        self.pb_Copy.setObjectName(u"pb_Copy")
        self.pb_Copy.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/Copy.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Copy.setIcon(icon1)
        self.pb_Copy.setIconSize(QSize(27, 27))

        self.gridLayout.addWidget(self.pb_Copy, 1, 1, 1, 1)


        self.retranslateUi(Inform)

        QMetaObject.connectSlotsByName(Inform)
    # setupUi

    def retranslateUi(self, Inform):
        Inform.setWindowTitle(QCoreApplication.translate("Inform", u"Results", None))
        self.te_Inform.setHtml(QCoreApplication.translate("Inform", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Income                   : $NotCalculated</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Tax Deduction       : $NotCalculated</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Taxable Income     : $NotCalculated</p>\n"
"<p style=\" margin-top"
                        ":0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Federal Taxes         : $NotCalculated</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        including:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                         Federal Income Tax  : $NotCalculated</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                         Social Security Tax   : $NotCalculated</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                         Medicare Tax             : $NotCalculated</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /"
                        "></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Net Income      : $NotCalculated</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Effective Rate  : NotCalculated%</p></body></html>", None))
        self.pb_OK.setText(QCoreApplication.translate("Inform", u"OK", None))
        self.pb_Copy.setText("")
    # retranslateUi

