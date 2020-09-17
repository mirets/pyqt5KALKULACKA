from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = 'This is my pushbutton'
        top = 250
        left = 250
        width = 500
        height = 300
        self.iconname = "youtube.png"

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(self.iconname))
        self.setGeometry(top, left, width, height)

        self.UiComponents()
        self.show()

    def UiComponents(self):
        button = QPushButton(" button", self)
        button.setGeometry(QRect(150, 150, 100, 28))
        button.setIcon(QtGui.QIcon(self.iconname))
        button.setToolTip("thiss is shit")


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())