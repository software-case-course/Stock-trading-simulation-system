
from PyQt5.QtWidgets import QMainWindow

import mainwindowui


class MainWindow(QMainWindow, mainwindowui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)



    def sss(self):
        print(1)

