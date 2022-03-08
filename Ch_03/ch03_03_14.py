# ch03/03_14.py
import sys
from PyQt5.QtWidgets import*

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #자식 객체에도 __init__ 객체가 있으므로 super를 통해 부모클래스의 객체를 가져옴.
        # PyQt의 QMainWindow 클래스는 부모 클래스 초기화자가 필요해서 그런거임.

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()