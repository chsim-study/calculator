from calculator import Calculator

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

save_list = []

class Calculate(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/cal.ui", self)
        self.setWindowTitle("Calculator")
        
        self.num_buttons = [
            self.btn_num0, self.btn_num1, self.btn_num2, self.btn_num3, self.btn_num4,
            self.btn_num5, self.btn_num6, self.btn_num7, self.btn_num8, self.btn_num9
        ]

        for i, btn in enumerate(self.num_buttons):
            btn.clicked.connect(lambda _, x=i: self.add_num(str(x)))

    def add_num(self, num: str):
        current_text = self.edit_result.text()
        self.edit_result.setText(current_text + num)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculate()
    window.show()
    sys.exit(app.exec_())