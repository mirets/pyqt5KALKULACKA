from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtGui
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PYQT5 mirets Window"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("youtube.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width, self.height)
        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
