# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NotificationPanel.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

class Ui_Notifications(object):
    def setupUi(self, Notifications):
        if not Notifications.objectName():
            Notifications.setObjectName(u"Notifications")
        Notifications.setWindowModality(Qt.WindowModality.ApplicationModal)
        Notifications.resize(200, 422)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        Notifications.setFont(font)

        self.retranslateUi(Notifications)

        QMetaObject.connectSlotsByName(Notifications)
    # setupUi

    def retranslateUi(self, Notifications):
        Notifications.setWindowTitle(QCoreApplication.translate("Notifications", u"Notifications", None))
    # retranslateUi

