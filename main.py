from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Calculate(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/cal.ui", self)
        self.setWindowTitle("Calculator")

    def calculate(self):
        try:
            num1 = float(self.lineEdit.text())
            num2 = float(self.lineEdit_2.text())
            result = num1 + num2
            self.label_result.setText(f"Result: {result}")
        except ValueError:
            self.label_result.setText("Invalid input")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculate()
    window.show()
    sys.exit(app.exec_())