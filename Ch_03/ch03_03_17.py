# ch03/03_17.py
import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,200,300,400)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon("2203534_cash_coin_money_value_icon.png"))

        btn = QPushButton("버튼1",self) #첫번째 인자는 버튼에 생성될 문자열, 두번째는 표시될 위젯

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()