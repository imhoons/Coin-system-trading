# ch03/03_13.py
import sys
from PyQt5.QtWidgets import*
app= QApplication(sys.argv)
btn=QPushButton("hello")  #버튼객체 생성
btn.show()
app.exec_()       #이벤트 루프 생성
