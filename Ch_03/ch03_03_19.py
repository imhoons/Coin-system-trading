# ch03/03_19.py
import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #위젯생성코드
        self.setGeometry(100,200,300,400)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon("2203534_cash_coin_money_value_icon.png"))

        btn1 = QPushButton("버튼1",self) #첫번째 인자는 버튼에 생성될 문자열, 두번째는 표시될 위젯
        btn1.move(10,10)
        btn1.clicked.connect(self.btn_clicked)

        btn2 = QPushButton("버튼2",self)
        btn2.move(10,40)
        btn2.clicked.connect(self.btn_clicked)

    #이벤트 처리 코드
    def btn_clicked(self):
        print("버튼클릭")
# QApplication 객체 생성 및 이벤트 루프 생성 코드
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()