from calculator import Calculator

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/cal.ui", self)
        self.setWindowTitle("Calculator")

        self.left = None 
        self.cal = ""

        self.btn_sum.clicked.connect(self.cal_sum)
        self.btn_sub.clicked.connect(self.cal_sub)
        self.btn_mul.clicked.connect(self.cal_mul)
        self.btn_div.clicked.connect(self.cal_div)
        self.btn_mod.clicked.connect(self.cal_mod)
        self.btn_equal.clicked.connect(self.cal_equal)
        self.btn_clear.clicked.connect(self.clear_all)
        self.btn_com.clicked.connect(self.add_com)
        self.btn_neg.clicked.connect(self.change_sign)
        num_buttons = [
            self.btn_num0, self.btn_num1, self.btn_num2, self.btn_num3, self.btn_num4,
            self.btn_num5, self.btn_num6, self.btn_num7, self.btn_num8, self.btn_num9
        ]
        for i, btn in enumerate(num_buttons):
            btn.clicked.connect(lambda _, x=i: self.add_num(str(x)))
        
        self.edit_result.setReadOnly(True)
    
    def change_sign(self):
        value = self._read_input()
        value = -1 * value
        self.edit_result.setText(str(value))
    
    def clear_all(self):
        self.edit_result.clear()
        self.left = None
        self.cal = ""

    def add_com(self):
        if not self.edit_result.text().count("."):
            self.edit_result.setText(self.edit_result.text() + ".")

    def add_num(self, num: str):
        self.edit_result.setText(self.edit_result.text() + num)

    def _read_input(self) -> float:
        text = self.edit_result.text().strip()
        if text:
            return float(text)
        return 0

    def cal_sum(self):
        self.left = self._read_input()
        self.edit_result.clear()
        self.cal = "sum"
    
    def cal_sub(self):
        self.left = self._read_input()
        self.edit_result.clear()
        self.cal = "sub"
    
    def cal_mul(self):
        self.left = self._read_input()
        self.edit_result.clear()
        self.cal = "mul"
    
    def cal_div(self):
        self.left = self._read_input()
        self.edit_result.clear()
        self.cal = "div"
    
    def cal_mod(self):
        self.left = self._read_input()
        self.edit_result.clear()
        self.cal = "mod"

    def cal_equal(self):
        right = self._read_input()
        if self.left is not None:
            left = self.left    
        else:
            left = 0

        if self.cal in ["sum", "sub", "mul", "div", "mod"]:
            if self.cal == "sum":
                result = Calculator.sum(left, right)
            elif self.cal == "sub":
                result = Calculator.sub(left, right)
            elif self.cal == "div":
                result = Calculator.div(left, right)
            elif self.cal == "mul":
                result = Calculator.mul(left, right)
            elif self.cal == "mod":
                result = Calculator.mod(left, right)
            else:
                result = right
        self.edit_result.setText(str(result))
        self.left = None
    
    def keyPressEvent(self, event):
        key = event.key()
        text = event.text()

        if key == Qt.Key_Backspace:
            self.edit_result.backspace()
            return

        if key in (Qt.Key_Return, Qt.Key_Enter):
            self.cal_equal()
            return

        if text.isdigit():
            self.add_num(text)
            return

        if text == ".":
            if not self.edit_result.text().count("."):
                self.add_com()
                return
        if text in {"+", "-", "*", "/", "%"}:
            if text == "+":
                self.cal_sum()
            elif text == "-":
                self.cal_sub()
            elif text == "*":
                self.cal_mul()
            elif text == "/":
                self.cal_div()
            elif text == "%":
                self.cal_mod()
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
