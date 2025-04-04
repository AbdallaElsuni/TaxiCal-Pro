from PySide6 import QtWidgets
from PySide6.QtCore import QTimer
from PySide6.QtGui import QIcon
from OldUI.MainWindow import Ui_MainWindow
import sys

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tb_EULA.verticalScrollBar().valueChanged.connect(self.user_scrolled)
        self.pb_DeclineAndExit.clicked.connect(self.close)
        self.pb_Exit.clicked.connect(self.close)
        self.pb_AgreeAndContinue.clicked.connect(self.switch_to_first_page)
        self.le_FirstName.textEdited.connect(lambda : (self.first_name_edited(), self.first_page_input_changed()))
        self.le_LastName.textEdited.connect(lambda : (self.last_name_edited(), self.first_page_input_changed()))
        self.cb_Status.currentIndexChanged.connect(self.first_page_input_changed)
        self.le_Income.textEdited.connect(lambda :(self.income_edited(), self.first_page_input_changed()))
        self.cb_FederalDeductionType.currentIndexChanged.connect(lambda :(self.federal_deduction_type_changed(), self.first_page_input_changed()))
        self.tb_ManualFederalItemization.clicked.connect(lambda :(self.manual_federal_itemization_button_clicked(), self.first_page_input_changed()))
        self.le_TotalFederalItemization.textChanged.connect(lambda :(self.federal_manual_itemization_changed(), self.first_page_input_changed()))
        self.pb_Next.clicked.connect(self.switch_to_second_page)
        self.pb_Back.clicked.connect(self.switch_to_first_page)
        self.show()
    def user_scrolled(self):
        if self.tb_EULA.verticalScrollBar().value() == self.tb_EULA.verticalScrollBar().maximum():
            self.pb_AgreeAndContinue.setEnabled(True)
    def switch_to_first_page(self):
        self.stackedWidget.setCurrentWidget(self.FirstPage)
    def first_name_edited(self):
        alpha_input = allow_alpha_only(self.le_FirstName.text())
        self.le_FirstName.setText(alpha_input.capitalize())
    def last_name_edited(self):
        alpha_input = allow_alpha_only(self.le_LastName.text())
        self.le_LastName.setText(alpha_input.capitalize())
    def income_edited(self):
        digit_input = allow_digit_only(self.le_Income.text())
        self.le_Income.setText(digit_input)
    def federal_deduction_type_changed(self):
        if self.cb_FederalDeductionType.currentIndex() == 0:
            self.tb_SmartFederalItemization.setEnabled(True)
            self.tb_ManualFederalItemization.setEnabled(True)
        elif self.cb_FederalDeductionType.currentIndex() == 1:
            self.tb_SmartFederalItemization.setEnabled(False)
            self.tb_ManualFederalItemization.setEnabled(False)
    def manual_federal_itemization_button_clicked(self):
        if not self.le_TotalFederalItemization.isEnabled():
            self.le_TotalFederalItemization.setEnabled(True)
            self.tb_ManualFederalItemization.setIcon(QIcon(":/Buttons/RedSaveButtonWithPencil.png"))
        else:
            self.le_TotalFederalItemization.setEnabled(False)
            self.tb_ManualFederalItemization.setIcon(QIcon(":/Buttons/Confirm2Smaller.png"))
            QTimer.singleShot(1500, lambda :(self.tb_ManualFederalItemization.setIcon(QIcon(":/Buttons/RedPencilSmaller.png"))))
    def auto_federal_itemization_button_clicked(self):
        pass
    def federal_manual_itemization_changed(self):
        digit_input = allow_digit_only(self.le_TotalFederalItemization.text())
        self.le_TotalFederalItemization.setText(digit_input)
    def first_page_input_changed(self):
        if self.valid_first_page_input():
            self.pb_Next.setEnabled(True)
        else:
            self.pb_Next.setEnabled(False)
    def valid_first_page_input(self):
        arguments = [16 > len(self.le_FirstName.text()) > 4, 16 > len(self.le_LastName.text()) > 4, self.le_Income.text().replace(".", "", 1).isdigit() and float(self.le_Income.text()) > 0, self.cb_Status.currentIndex() != 0]
        if all(argument for argument in arguments):
            if self.cb_FederalDeductionType.currentIndex() == 1:
                return True
            elif self.cb_FederalDeductionType.currentIndex() == 0:
                if self.le_TotalFederalItemization.text().replace(".", "", 1).isdigit() and float(self.le_TotalFederalItemization.text()) > 0:
                    if not self.le_TotalFederalItemization.isEnabled():
                        return True
    def switch_to_second_page(self):
        self.stackedWidget.setCurrentWidget(self.SecondPage)
def allow_alpha_only(user_input:str):
    for c in user_input:
        if not c.isalpha():
            user_input = user_input.replace(c, "")
    return user_input
def allow_digit_only(user_input:str):
    for c in user_input:
        if not c.isdigit():
            if c != ".":
                user_input = user_input.replace(c, "")
    if user_input.find(".") >= 0:
        first_dot = user_input.find(".")
        if first_dot == 0:
            user_input = "0" + user_input
    if user_input.count(".") > 1:
        first_dot = user_input.find(".")
        first_portion = user_input[:first_dot+1]
        second_portion = user_input[first_dot:]
        second_portion = second_portion.replace(".", "")
        user_input = first_portion + second_portion
    return user_input
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())