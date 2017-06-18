import sys
import stockinfo
import mainwindow
import logindialog
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    # ui = stockinfo.Ui_MainWindow()
    ui = mainwindow.Ui_MainWindow()
    qss_file = open('qss/black.css').read()
    MainWindow.setStyleSheet(qss_file)

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

