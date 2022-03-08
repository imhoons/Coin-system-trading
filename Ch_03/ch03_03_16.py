# ch03/03_16.py
import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,200,300,400)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon("2203534_cash_coin_money_value_icon.png"))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()