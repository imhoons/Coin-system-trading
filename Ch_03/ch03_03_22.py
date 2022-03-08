# ch03/03_22.py
import sys
from PyQt5.QtWidgets import*
from PyQt5 import uic

form_class = uic.loadUiType("코빗 시세 조회기.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)

    def inquiry(self):
        print("조회 버튼 클릭")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()