from calculator import Calculator

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/cal.ui", self)
        self.setWindowTitle("Calculator")

        self.left = None 

        self.btn_sum.clicked.connect(self.cal_sum)
        self.btn_equal.clicked.connect(self.cal_equal)
        num_buttons = [
            self.btn_num0, self.btn_num1, self.btn_num2, self.btn_num3, self.btn_num4,
            self.btn_num5, self.btn_num6, self.btn_num7, self.btn_num8, self.btn_num9
        ]
        for i, btn in enumerate(num_buttons):
            btn.clicked.connect(lambda _, x=i: self.add_num(str(x)))

    def add_num(self, num: str):
        self.edit_result.setText(self.edit_result.text() + num)

    def _read_input(self) -> int:
        text = self.edit_result.text().strip()
        if text:
            return int(text)
        return 0

    def cal_sum(self):
        self.left = self._read_input()
        self.edit_result.clear()

    def cal_equal(self):
        right = self._read_input()
        if self.left is not None:
            left = self.left    
        else:
            left = 0
        result = Calculator.sum(left, right)
        self.edit_result.setText(str(result))
        self.left = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
