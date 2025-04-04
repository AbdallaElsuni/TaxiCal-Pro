# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTabWidget,
    QTextBrowser, QToolButton, QWidget)
import Icons.TaxiCal_Icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 559)
        MainWindow.setMinimumSize(QSize(650, 559))
        MainWindow.setMaximumSize(QSize(7000, 7000))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/T.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.actionNew_Account = QAction(MainWindow)
        self.actionNew_Account.setObjectName(u"actionNew_Account")
        self.actionNew_Account.setCheckable(True)
        self.actionNew_Account.setChecked(True)
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/Plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionNew_Account.setIcon(icon1)
        font1 = QFont()
        font1.setBold(True)
        self.actionNew_Account.setFont(font1)
        self.actionAccount_1 = QAction(MainWindow)
        self.actionAccount_1.setObjectName(u"actionAccount_1")
        self.actionAccount_1.setCheckable(True)
        self.actionAccount_1.setEnabled(False)
        self.actionAccount_Manager = QAction(MainWindow)
        self.actionAccount_Manager.setObjectName(u"actionAccount_Manager")
        icon2 = QIcon()
        icon2.addFile(u":/Main/Account.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAccount_Manager.setIcon(icon2)
        self.actionAccount_Manager.setFont(font1)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon3 = QIcon()
        icon3.addFile(u":/Buttons/About.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAbout.setIcon(icon3)
        self.actionUpdate = QAction(MainWindow)
        self.actionUpdate.setObjectName(u"actionUpdate")
        icon4 = QIcon()
        icon4.addFile(u":/Buttons/DownloadUpdate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionUpdate.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.DisclaimerPage = QWidget()
        self.DisclaimerPage.setObjectName(u"DisclaimerPage")
        self.gridLayout_7 = QGridLayout(self.DisclaimerPage)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pb_DeclineAndExit = QPushButton(self.DisclaimerPage)
        self.pb_DeclineAndExit.setObjectName(u"pb_DeclineAndExit")

        self.gridLayout_7.addWidget(self.pb_DeclineAndExit, 1, 1, 1, 1)

        self.pb_AgreeAndContinue = QPushButton(self.DisclaimerPage)
        self.pb_AgreeAndContinue.setObjectName(u"pb_AgreeAndContinue")
        self.pb_AgreeAndContinue.setEnabled(False)

        self.gridLayout_7.addWidget(self.pb_AgreeAndContinue, 1, 2, 1, 1)

        self.tb_EULA = QTextBrowser(self.DisclaimerPage)
        self.tb_EULA.setObjectName(u"tb_EULA")

        self.gridLayout_7.addWidget(self.tb_EULA, 0, 0, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.DisclaimerPage)
        self.FirstPage = QWidget()
        self.FirstPage.setObjectName(u"FirstPage")
        self.gridLayout = QGridLayout(self.FirstPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_AccountQuestion = QLabel(self.FirstPage)
        self.lb_AccountQuestion.setObjectName(u"lb_AccountQuestion")

        self.gridLayout.addWidget(self.lb_AccountQuestion, 5, 0, 1, 1)

        self.groupBox = QGroupBox(self.FirstPage)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_10 = QGridLayout(self.groupBox)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.lb_BlankTotalFederalItemized = QLabel(self.groupBox)
        self.lb_BlankTotalFederalItemized.setObjectName(u"lb_BlankTotalFederalItemized")

        self.gridLayout_10.addWidget(self.lb_BlankTotalFederalItemized, 1, 0, 1, 1)

        self.cb_FederalDeductionType = QComboBox(self.groupBox)
        self.cb_FederalDeductionType.addItem("")
        self.cb_FederalDeductionType.addItem("")
        self.cb_FederalDeductionType.setObjectName(u"cb_FederalDeductionType")

        self.gridLayout_10.addWidget(self.cb_FederalDeductionType, 0, 1, 1, 3)

        self.tb_SmartFederalItemization = QToolButton(self.groupBox)
        self.tb_SmartFederalItemization.setObjectName(u"tb_SmartFederalItemization")
        self.tb_SmartFederalItemization.setEnabled(True)
        icon5 = QIcon()
        icon5.addFile(u":/Buttons/BlueSheildWithCheck.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_SmartFederalItemization.setIcon(icon5)
        self.tb_SmartFederalItemization.setIconSize(QSize(26, 26))

        self.gridLayout_10.addWidget(self.tb_SmartFederalItemization, 1, 3, 1, 1)

        self.le_TotalFederalItemization = QLineEdit(self.groupBox)
        self.le_TotalFederalItemization.setObjectName(u"le_TotalFederalItemization")
        self.le_TotalFederalItemization.setEnabled(False)

        self.gridLayout_10.addWidget(self.le_TotalFederalItemization, 1, 1, 1, 1)

        self.lb_FederalDeductionType = QLabel(self.groupBox)
        self.lb_FederalDeductionType.setObjectName(u"lb_FederalDeductionType")

        self.gridLayout_10.addWidget(self.lb_FederalDeductionType, 0, 0, 1, 1)

        self.tb_ManualFederalItemization = QToolButton(self.groupBox)
        self.tb_ManualFederalItemization.setObjectName(u"tb_ManualFederalItemization")
        self.tb_ManualFederalItemization.setEnabled(True)
        icon6 = QIcon()
        icon6.addFile(u":/Buttons/RedPencilSmaller.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_ManualFederalItemization.setIcon(icon6)
        self.tb_ManualFederalItemization.setIconSize(QSize(26, 26))

        self.gridLayout_10.addWidget(self.tb_ManualFederalItemization, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 2)

        self.gb_MaritalStatusAndIncome = QGroupBox(self.FirstPage)
        self.gb_MaritalStatusAndIncome.setObjectName(u"gb_MaritalStatusAndIncome")
        self.gridLayout_9 = QGridLayout(self.gb_MaritalStatusAndIncome)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.lb_MaritualStatus = QLabel(self.gb_MaritalStatusAndIncome)
        self.lb_MaritualStatus.setObjectName(u"lb_MaritualStatus")

        self.gridLayout_9.addWidget(self.lb_MaritualStatus, 0, 0, 1, 1)

        self.cb_Status = QComboBox(self.gb_MaritalStatusAndIncome)
        self.cb_Status.addItem("")
        self.cb_Status.addItem("")
        self.cb_Status.addItem("")
        self.cb_Status.addItem("")
        self.cb_Status.setObjectName(u"cb_Status")

        self.gridLayout_9.addWidget(self.cb_Status, 0, 1, 1, 1)

        self.lb_Income = QLabel(self.gb_MaritalStatusAndIncome)
        self.lb_Income.setObjectName(u"lb_Income")

        self.gridLayout_9.addWidget(self.lb_Income, 1, 0, 1, 1)

        self.le_Income = QLineEdit(self.gb_MaritalStatusAndIncome)
        self.le_Income.setObjectName(u"le_Income")

        self.gridLayout_9.addWidget(self.le_Income, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.gb_MaritalStatusAndIncome, 1, 0, 1, 2)

        self.gb_Name = QGroupBox(self.FirstPage)
        self.gb_Name.setObjectName(u"gb_Name")
        self.gridLayout_2 = QGridLayout(self.gb_Name)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.le_FirstName = QLineEdit(self.gb_Name)
        self.le_FirstName.setObjectName(u"le_FirstName")

        self.gridLayout_2.addWidget(self.le_FirstName, 0, 1, 1, 1)

        self.lb_FirstName = QLabel(self.gb_Name)
        self.lb_FirstName.setObjectName(u"lb_FirstName")

        self.gridLayout_2.addWidget(self.lb_FirstName, 0, 0, 1, 1)

        self.lb_LastName = QLabel(self.gb_Name)
        self.lb_LastName.setObjectName(u"lb_LastName")

        self.gridLayout_2.addWidget(self.lb_LastName, 0, 2, 1, 1)

        self.le_LastName = QLineEdit(self.gb_Name)
        self.le_LastName.setObjectName(u"le_LastName")

        self.gridLayout_2.addWidget(self.le_LastName, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.gb_Name, 0, 0, 1, 2)

        self.gb_NextAndExit = QGroupBox(self.FirstPage)
        self.gb_NextAndExit.setObjectName(u"gb_NextAndExit")
        self.gridLayout_4 = QGridLayout(self.gb_NextAndExit)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pb_Exit = QPushButton(self.gb_NextAndExit)
        self.pb_Exit.setObjectName(u"pb_Exit")
        icon7 = QIcon()
        icon7.addFile(u":/Buttons/Cross.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Exit.setIcon(icon7)

        self.gridLayout_4.addWidget(self.pb_Exit, 0, 0, 1, 1)

        self.pb_Next = QPushButton(self.gb_NextAndExit)
        self.pb_Next.setObjectName(u"pb_Next")
        self.pb_Next.setEnabled(False)
        self.pb_Next.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon8 = QIcon()
        icon8.addFile(u":/Buttons/Next.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Next.setIcon(icon8)
        self.pb_Next.setIconSize(QSize(26, 26))

        self.gridLayout_4.addWidget(self.pb_Next, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.gb_NextAndExit, 3, 0, 1, 2)

        self.pb_Login = QPushButton(self.FirstPage)
        self.pb_Login.setObjectName(u"pb_Login")
        icon9 = QIcon()
        icon9.addFile(u":/Buttons/Login.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Login.setIcon(icon9)
        self.pb_Login.setIconSize(QSize(27, 27))

        self.gridLayout.addWidget(self.pb_Login, 5, 1, 1, 1)

        self.lb_FederalMessege = QLabel(self.FirstPage)
        self.lb_FederalMessege.setObjectName(u"lb_FederalMessege")

        self.gridLayout.addWidget(self.lb_FederalMessege, 4, 0, 1, 2)

        self.stackedWidget.addWidget(self.FirstPage)
        self.SecondPage = QWidget()
        self.SecondPage.setObjectName(u"SecondPage")
        self.gridLayout_5 = QGridLayout(self.SecondPage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lb_DontSeeYourCityQuestion = QLabel(self.SecondPage)
        self.lb_DontSeeYourCityQuestion.setObjectName(u"lb_DontSeeYourCityQuestion")

        self.gridLayout_5.addWidget(self.lb_DontSeeYourCityQuestion, 1, 0, 1, 1)

        self.gb_StateAndCity = QGroupBox(self.SecondPage)
        self.gb_StateAndCity.setObjectName(u"gb_StateAndCity")
        self.formLayout = QFormLayout(self.gb_StateAndCity)
        self.formLayout.setObjectName(u"formLayout")
        self.lb_State = QLabel(self.gb_StateAndCity)
        self.lb_State.setObjectName(u"lb_State")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_State)

        self.cb_State = QComboBox(self.gb_StateAndCity)
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.addItem("")
        self.cb_State.setObjectName(u"cb_State")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cb_State)

        self.lb_City = QLabel(self.gb_StateAndCity)
        self.lb_City.setObjectName(u"lb_City")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lb_City)

        self.cb_City = QComboBox(self.gb_StateAndCity)
        self.cb_City.addItem("")
        self.cb_City.setObjectName(u"cb_City")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cb_City)


        self.gridLayout_5.addWidget(self.gb_StateAndCity, 0, 0, 1, 2)

        self.pb_AddCity = QPushButton(self.SecondPage)
        self.pb_AddCity.setObjectName(u"pb_AddCity")

        self.gridLayout_5.addWidget(self.pb_AddCity, 1, 1, 1, 1)

        self.lb_StateMessege = QLabel(self.SecondPage)
        self.lb_StateMessege.setObjectName(u"lb_StateMessege")

        self.gridLayout_5.addWidget(self.lb_StateMessege, 3, 0, 1, 2)

        self.gb_EmployementAndBenefits = QGroupBox(self.SecondPage)
        self.gb_EmployementAndBenefits.setObjectName(u"gb_EmployementAndBenefits")
        self.gridLayout_8 = QGridLayout(self.gb_EmployementAndBenefits)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.le_StateTotalItemization = QLineEdit(self.gb_EmployementAndBenefits)
        self.le_StateTotalItemization.setObjectName(u"le_StateTotalItemization")
        self.le_StateTotalItemization.setEnabled(False)

        self.gridLayout_8.addWidget(self.le_StateTotalItemization, 2, 1, 1, 1)

        self.lb_Employement = QLabel(self.gb_EmployementAndBenefits)
        self.lb_Employement.setObjectName(u"lb_Employement")

        self.gridLayout_8.addWidget(self.lb_Employement, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gb_EmployementAndBenefits)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_8.addWidget(self.label_2, 3, 0, 1, 1)

        self.lb_StateDeductionType = QLabel(self.gb_EmployementAndBenefits)
        self.lb_StateDeductionType.setObjectName(u"lb_StateDeductionType")

        self.gridLayout_8.addWidget(self.lb_StateDeductionType, 1, 0, 1, 1)

        self.cb_EmployementStatus = QComboBox(self.gb_EmployementAndBenefits)
        self.cb_EmployementStatus.addItem("")
        self.cb_EmployementStatus.addItem("")
        self.cb_EmployementStatus.addItem("")
        self.cb_EmployementStatus.setObjectName(u"cb_EmployementStatus")

        self.gridLayout_8.addWidget(self.cb_EmployementStatus, 0, 1, 1, 3)

        self.comboBox = QComboBox(self.gb_EmployementAndBenefits)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_8.addWidget(self.comboBox, 3, 1, 1, 3)

        self.tb_ManualStateItemization = QToolButton(self.gb_EmployementAndBenefits)
        self.tb_ManualStateItemization.setObjectName(u"tb_ManualStateItemization")
        self.tb_ManualStateItemization.setEnabled(False)
        self.tb_ManualStateItemization.setToolTipDuration(-1)
        self.tb_ManualStateItemization.setIcon(icon6)
        self.tb_ManualStateItemization.setIconSize(QSize(26, 26))

        self.gridLayout_8.addWidget(self.tb_ManualStateItemization, 2, 2, 1, 1)

        self.tb_SmartStateItemization = QToolButton(self.gb_EmployementAndBenefits)
        self.tb_SmartStateItemization.setObjectName(u"tb_SmartStateItemization")
        self.tb_SmartStateItemization.setEnabled(False)
        self.tb_SmartStateItemization.setToolTipDuration(-1)
        self.tb_SmartStateItemization.setIcon(icon5)
        self.tb_SmartStateItemization.setIconSize(QSize(26, 26))

        self.gridLayout_8.addWidget(self.tb_SmartStateItemization, 2, 3, 1, 1)

        self.lb_Blank = QLabel(self.gb_EmployementAndBenefits)
        self.lb_Blank.setObjectName(u"lb_Blank")

        self.gridLayout_8.addWidget(self.lb_Blank, 2, 0, 1, 1)

        self.cb_StateDeductionType = QComboBox(self.gb_EmployementAndBenefits)
        self.cb_StateDeductionType.addItem("")
        self.cb_StateDeductionType.addItem("")
        self.cb_StateDeductionType.setObjectName(u"cb_StateDeductionType")

        self.gridLayout_8.addWidget(self.cb_StateDeductionType, 1, 1, 1, 3)

        self.lb_Blank2 = QLabel(self.gb_EmployementAndBenefits)
        self.lb_Blank2.setObjectName(u"lb_Blank2")

        self.gridLayout_8.addWidget(self.lb_Blank2, 4, 0, 1, 1)

        self.le_CityTotalItemization = QLineEdit(self.gb_EmployementAndBenefits)
        self.le_CityTotalItemization.setObjectName(u"le_CityTotalItemization")
        self.le_CityTotalItemization.setEnabled(False)

        self.gridLayout_8.addWidget(self.le_CityTotalItemization, 4, 1, 1, 1)

        self.tb_ManualCityItemization = QToolButton(self.gb_EmployementAndBenefits)
        self.tb_ManualCityItemization.setObjectName(u"tb_ManualCityItemization")
        self.tb_ManualCityItemization.setEnabled(False)
        self.tb_ManualCityItemization.setIcon(icon6)
        self.tb_ManualCityItemization.setIconSize(QSize(26, 26))

        self.gridLayout_8.addWidget(self.tb_ManualCityItemization, 4, 2, 1, 1)

        self.tb_SmartCityItemization = QToolButton(self.gb_EmployementAndBenefits)
        self.tb_SmartCityItemization.setObjectName(u"tb_SmartCityItemization")
        self.tb_SmartCityItemization.setEnabled(False)
        self.tb_SmartCityItemization.setIcon(icon5)
        self.tb_SmartCityItemization.setIconSize(QSize(26, 26))

        self.gridLayout_8.addWidget(self.tb_SmartCityItemization, 4, 3, 1, 1)


        self.gridLayout_5.addWidget(self.gb_EmployementAndBenefits, 2, 0, 1, 2)

        self.pb_Submit = QPushButton(self.SecondPage)
        self.pb_Submit.setObjectName(u"pb_Submit")
        self.pb_Submit.setEnabled(False)
        icon10 = QIcon()
        icon10.addFile(u":/Buttons/submit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Submit.setIcon(icon10)
        self.pb_Submit.setIconSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.pb_Submit, 4, 1, 1, 1)

        self.pb_Back = QPushButton(self.SecondPage)
        self.pb_Back.setObjectName(u"pb_Back")
        icon11 = QIcon()
        icon11.addFile(u":/Buttons/Previous.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_Back.setIcon(icon11)
        self.pb_Back.setIconSize(QSize(26, 26))

        self.gridLayout_5.addWidget(self.pb_Back, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.SecondPage)
        self.ThirdPage = QWidget()
        self.ThirdPage.setObjectName(u"ThirdPage")
        self.gridLayout_6 = QGridLayout(self.ThirdPage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pb_Ok = QPushButton(self.ThirdPage)
        self.pb_Ok.setObjectName(u"pb_Ok")

        self.gridLayout_6.addWidget(self.pb_Ok, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.tb_Copy = QToolButton(self.ThirdPage)
        self.tb_Copy.setObjectName(u"tb_Copy")
        icon12 = QIcon()
        icon12.addFile(u":/Buttons/Copy.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_Copy.setIcon(icon12)
        self.tb_Copy.setIconSize(QSize(26, 26))

        self.gridLayout_6.addWidget(self.tb_Copy, 1, 1, 1, 1)

        self.tb_Inform = QTextBrowser(self.ThirdPage)
        self.tb_Inform.setObjectName(u"tb_Inform")

        self.gridLayout_6.addWidget(self.tb_Inform, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.ThirdPage)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 650, 33))
        self.menuAccount = QMenu(self.menubar)
        self.menuAccount.setObjectName(u"menuAccount")
        self.menuRegisteredAccounts = QMenu(self.menuAccount)
        self.menuRegisteredAccounts.setObjectName(u"menuRegisteredAccounts")
        self.menuRegisteredAccounts.setFont(font)
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tb_EULA, self.pb_AgreeAndContinue)
        QWidget.setTabOrder(self.pb_AgreeAndContinue, self.pb_DeclineAndExit)
        QWidget.setTabOrder(self.pb_DeclineAndExit, self.le_FirstName)
        QWidget.setTabOrder(self.le_FirstName, self.le_LastName)
        QWidget.setTabOrder(self.le_LastName, self.cb_Status)
        QWidget.setTabOrder(self.cb_Status, self.le_Income)
        QWidget.setTabOrder(self.le_Income, self.pb_Next)
        QWidget.setTabOrder(self.pb_Next, self.pb_Exit)
        QWidget.setTabOrder(self.pb_Exit, self.pb_Login)
        QWidget.setTabOrder(self.pb_Login, self.cb_EmployementStatus)
        QWidget.setTabOrder(self.cb_EmployementStatus, self.cb_StateDeductionType)
        QWidget.setTabOrder(self.cb_StateDeductionType, self.le_StateTotalItemization)
        QWidget.setTabOrder(self.le_StateTotalItemization, self.pb_Submit)
        QWidget.setTabOrder(self.pb_Submit, self.pb_Back)
        QWidget.setTabOrder(self.pb_Back, self.tb_Inform)
        QWidget.setTabOrder(self.tb_Inform, self.tb_Copy)
        QWidget.setTabOrder(self.tb_Copy, self.pb_Ok)

        self.menubar.addAction(self.menuAccount.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuAccount.addAction(self.actionNew_Account)
        self.menuAccount.addAction(self.menuRegisteredAccounts.menuAction())
        self.menuAccount.addSeparator()
        self.menuAccount.addAction(self.actionAccount_Manager)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionUpdate)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TaxiCal", None))
        self.actionNew_Account.setText(QCoreApplication.translate("MainWindow", u"New Account", None))
        self.actionAccount_1.setText(QCoreApplication.translate("MainWindow", u"Account 1", None))
        self.actionAccount_Manager.setText(QCoreApplication.translate("MainWindow", u"Account Manager", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pb_DeclineAndExit.setText(QCoreApplication.translate("MainWindow", u" Decline and Exit ", None))
        self.pb_AgreeAndContinue.setText(QCoreApplication.translate("MainWindow", u"  Agree and Continue ", None))
        self.tb_EULA.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">TaxiCal Terms of Use</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Effective Date: [3/11/2025]</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span styl"
                        "e=\" font-size:10pt;\">By using TaxiCal (&quot;the App&quot;), you agree to the following terms and conditions. If you do not agree, do not proceed with the use of the App.</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Personal Use Only\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TaxiCal is licensed for personal, non-commercial use only.</li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Any commercial use, including but not limited to selling, redistributing"
                        ", or integrating TaxiCal into other financial services, is strictly prohibited.</li></ul></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">No Warranty &amp; Limitation of Liability\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TaxiCal is provided &quot;as is&quot; without any warranties, express or implied.</li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">We do not guarantee the accuracy, reliability, or completeness of the calculations and information provided.</li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;"
                        " -qt-block-indent:0; text-indent:0px;\">You acknowledge that any tax-related decisions made based on the App's output are your sole responsibility.</li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Under no circumstances shall we be liable for any direct, indirect, incidental, or consequential damages arising from the use of the App.</li></ul></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">No Professional Advice\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TaxiCal is a tax estimation tool and does not provide legal, financial, or tax advice.</li>\n"
"<li style=\" font-size:10p"
                        "t;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Users should consult with a qualified tax professional for official tax filings and financial decisions.</li></ul></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Data &amp; Privacy\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The App does not collect or store personal financial data.</li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Any data entered remains on the user's device and is not shared with third parties.</li></ul></li>\n"
"<li style=\" font-size"
                        ":10pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Modifications &amp; Termination\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">We reserve the right to update or discontinue the App at any time without notice.</li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Continued use after modifications constitutes acceptance of the new terms.</li></ul></li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">By clicking &quot;Next&quot; or continuing to use the App, you acknowledge that you have read, understo"
                        "od, and agreed to these Terms of Use.</span></p></body></html>", None))
        self.lb_AccountQuestion.setText(QCoreApplication.translate("MainWindow", u"Already have an account?", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.lb_BlankTotalFederalItemized.setText("")
        self.cb_FederalDeductionType.setItemText(0, QCoreApplication.translate("MainWindow", u"Itemized", None))
        self.cb_FederalDeductionType.setItemText(1, QCoreApplication.translate("MainWindow", u"Standard", None))

        self.tb_SmartFederalItemization.setText("")
        self.le_TotalFederalItemization.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Federal Total Itemization", None))
        self.lb_FederalDeductionType.setText(QCoreApplication.translate("MainWindow", u"Deduction Type", None))
        self.tb_ManualFederalItemization.setText("")
        self.gb_MaritalStatusAndIncome.setTitle(QCoreApplication.translate("MainWindow", u"Income and Marital Status", None))
        self.lb_MaritualStatus.setText(QCoreApplication.translate("MainWindow", u"Marital Status", None))
        self.cb_Status.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Status", None))
        self.cb_Status.setItemText(1, QCoreApplication.translate("MainWindow", u"Single", None))
        self.cb_Status.setItemText(2, QCoreApplication.translate("MainWindow", u"Married (Joint Account)", None))
        self.cb_Status.setItemText(3, QCoreApplication.translate("MainWindow", u"Married (No Joint Account)", None))

        self.lb_Income.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.le_Income.setPlaceholderText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.gb_Name.setTitle(QCoreApplication.translate("MainWindow", u"Name", None))
        self.le_FirstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"John", None))
        self.lb_FirstName.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.lb_LastName.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.le_LastName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Smith", None))
        self.gb_NextAndExit.setTitle("")
        self.pb_Exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pb_Next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pb_Login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lb_FederalMessege.setText("")
        self.lb_DontSeeYourCityQuestion.setText(QCoreApplication.translate("MainWindow", u"Don't see your city on the list?", None))
        self.gb_StateAndCity.setTitle(QCoreApplication.translate("MainWindow", u"State and City", None))
        self.lb_State.setText(QCoreApplication.translate("MainWindow", u"State", None))
        self.cb_State.setItemText(0, QCoreApplication.translate("MainWindow", u"Select State", None))
        self.cb_State.setItemText(1, QCoreApplication.translate("MainWindow", u"Alabama", None))
        self.cb_State.setItemText(2, QCoreApplication.translate("MainWindow", u"Alaska", None))
        self.cb_State.setItemText(3, QCoreApplication.translate("MainWindow", u"Arizona", None))
        self.cb_State.setItemText(4, QCoreApplication.translate("MainWindow", u"Arkansas", None))
        self.cb_State.setItemText(5, QCoreApplication.translate("MainWindow", u"California", None))
        self.cb_State.setItemText(6, QCoreApplication.translate("MainWindow", u"Colorado", None))
        self.cb_State.setItemText(7, QCoreApplication.translate("MainWindow", u"Connecticut", None))
        self.cb_State.setItemText(8, QCoreApplication.translate("MainWindow", u"Delaware", None))
        self.cb_State.setItemText(9, QCoreApplication.translate("MainWindow", u"Florida", None))
        self.cb_State.setItemText(10, QCoreApplication.translate("MainWindow", u"Georgia", None))
        self.cb_State.setItemText(11, QCoreApplication.translate("MainWindow", u"Hawaii", None))
        self.cb_State.setItemText(12, QCoreApplication.translate("MainWindow", u"Idaho", None))
        self.cb_State.setItemText(13, QCoreApplication.translate("MainWindow", u"Illinois", None))
        self.cb_State.setItemText(14, QCoreApplication.translate("MainWindow", u"Indiana", None))
        self.cb_State.setItemText(15, QCoreApplication.translate("MainWindow", u"Iowa", None))
        self.cb_State.setItemText(16, QCoreApplication.translate("MainWindow", u"Kansas", None))
        self.cb_State.setItemText(17, QCoreApplication.translate("MainWindow", u"Kentucky", None))
        self.cb_State.setItemText(18, QCoreApplication.translate("MainWindow", u"Louisiana", None))
        self.cb_State.setItemText(19, QCoreApplication.translate("MainWindow", u"Maine", None))
        self.cb_State.setItemText(20, QCoreApplication.translate("MainWindow", u"Maryland", None))
        self.cb_State.setItemText(21, QCoreApplication.translate("MainWindow", u"Massachusetts", None))
        self.cb_State.setItemText(22, QCoreApplication.translate("MainWindow", u"Michigan", None))
        self.cb_State.setItemText(23, QCoreApplication.translate("MainWindow", u"Minnesota", None))
        self.cb_State.setItemText(24, QCoreApplication.translate("MainWindow", u"Mississippi", None))
        self.cb_State.setItemText(25, QCoreApplication.translate("MainWindow", u"Missouri", None))
        self.cb_State.setItemText(26, QCoreApplication.translate("MainWindow", u"Montana", None))
        self.cb_State.setItemText(27, QCoreApplication.translate("MainWindow", u"Nebraska", None))
        self.cb_State.setItemText(28, QCoreApplication.translate("MainWindow", u"Nevada", None))
        self.cb_State.setItemText(29, QCoreApplication.translate("MainWindow", u"New Hampshire", None))
        self.cb_State.setItemText(30, QCoreApplication.translate("MainWindow", u"New Jersey", None))
        self.cb_State.setItemText(31, QCoreApplication.translate("MainWindow", u"New Mexico", None))
        self.cb_State.setItemText(32, QCoreApplication.translate("MainWindow", u"New York", None))
        self.cb_State.setItemText(33, QCoreApplication.translate("MainWindow", u"North Carolina", None))
        self.cb_State.setItemText(34, QCoreApplication.translate("MainWindow", u"North Dakota", None))
        self.cb_State.setItemText(35, QCoreApplication.translate("MainWindow", u"Ohio", None))
        self.cb_State.setItemText(36, QCoreApplication.translate("MainWindow", u"Oklahoma", None))
        self.cb_State.setItemText(37, QCoreApplication.translate("MainWindow", u"Oregon", None))
        self.cb_State.setItemText(38, QCoreApplication.translate("MainWindow", u"Pennsylvania", None))
        self.cb_State.setItemText(39, QCoreApplication.translate("MainWindow", u"Rhode Island", None))
        self.cb_State.setItemText(40, QCoreApplication.translate("MainWindow", u"South Carolina", None))
        self.cb_State.setItemText(41, QCoreApplication.translate("MainWindow", u"South Dakota", None))
        self.cb_State.setItemText(42, QCoreApplication.translate("MainWindow", u"Tennessee", None))
        self.cb_State.setItemText(43, QCoreApplication.translate("MainWindow", u"Texas", None))
        self.cb_State.setItemText(44, QCoreApplication.translate("MainWindow", u"Utah", None))
        self.cb_State.setItemText(45, QCoreApplication.translate("MainWindow", u"Vermont", None))
        self.cb_State.setItemText(46, QCoreApplication.translate("MainWindow", u"Virginia", None))
        self.cb_State.setItemText(47, QCoreApplication.translate("MainWindow", u"Washington", None))
        self.cb_State.setItemText(48, QCoreApplication.translate("MainWindow", u"West Virginia", None))
        self.cb_State.setItemText(49, QCoreApplication.translate("MainWindow", u"Wisconsin", None))
        self.cb_State.setItemText(50, QCoreApplication.translate("MainWindow", u"Wyoming", None))

        self.lb_City.setText(QCoreApplication.translate("MainWindow", u"City", None))
        self.cb_City.setItemText(0, QCoreApplication.translate("MainWindow", u"Select City", None))

        self.pb_AddCity.setText(QCoreApplication.translate("MainWindow", u"Add City", None))
        self.lb_StateMessege.setText("")
        self.gb_EmployementAndBenefits.setTitle(QCoreApplication.translate("MainWindow", u"Employement Status and Tax benefits", None))
        self.le_StateTotalItemization.setPlaceholderText(QCoreApplication.translate("MainWindow", u"State Total Itemization", None))
        self.lb_Employement.setText(QCoreApplication.translate("MainWindow", u"Employement", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"City Deductions", None))
        self.lb_StateDeductionType.setText(QCoreApplication.translate("MainWindow", u"State Deductions", None))
        self.cb_EmployementStatus.setItemText(0, QCoreApplication.translate("MainWindow", u"Employed (W-2)", None))
        self.cb_EmployementStatus.setItemText(1, QCoreApplication.translate("MainWindow", u"Self-employed", None))
        self.cb_EmployementStatus.setItemText(2, QCoreApplication.translate("MainWindow", u"Retired", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Standard", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Itemized", None))

#if QT_CONFIG(tooltip)
        self.tb_ManualStateItemization.setToolTip(QCoreApplication.translate("MainWindow", u"Manually Total Itemized", None))
#endif // QT_CONFIG(tooltip)
        self.tb_ManualStateItemization.setText("")
#if QT_CONFIG(tooltip)
        self.tb_SmartStateItemization.setToolTip(QCoreApplication.translate("MainWindow", u"Smart Itemization", None))
#endif // QT_CONFIG(tooltip)
        self.tb_SmartStateItemization.setText("")
        self.lb_Blank.setText(QCoreApplication.translate("MainWindow", u"\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0", None))
        self.cb_StateDeductionType.setItemText(0, QCoreApplication.translate("MainWindow", u"Standard", None))
        self.cb_StateDeductionType.setItemText(1, QCoreApplication.translate("MainWindow", u"Itemized", None))

        self.lb_Blank2.setText("")
        self.le_CityTotalItemization.setPlaceholderText(QCoreApplication.translate("MainWindow", u"City Total Itemization", None))
        self.tb_ManualCityItemization.setText("")
        self.tb_SmartCityItemization.setText("")
        self.pb_Submit.setText(QCoreApplication.translate("MainWindow", u"\u00a0Submit", None))
        self.pb_Back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.pb_Ok.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.tb_Copy.setText("")
        self.menuAccount.setTitle(QCoreApplication.translate("MainWindow", u"Account", None))
        self.menuRegisteredAccounts.setTitle(QCoreApplication.translate("MainWindow", u"Registered Accounts", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

