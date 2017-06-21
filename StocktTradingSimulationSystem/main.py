import sys, WindowFuntion

from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = WindowFuntion.MainWindow()
    qss_file = open('qss//style.qss').read()
    mainWindow.setStyleSheet(qss_file)
    mainWindow.show()
    sys.exit(app.exec_())
