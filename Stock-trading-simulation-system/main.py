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
    ui.account.clicked.connect(showbox())
    MainWindow.show()
    sys.exit(app.exec_())



def showbox(self):
    # QtWidgets.QMessageBox.information(self.pushButton, "标题", "这是第一个PyQt5 GUI程序")

    lg = QDialog()
    ui = logindialog.Ui_logindialog()
    qss_file = open('qss/black.css').read()
    lg.setStyleSheet(qss_file)
    ui.setupUi(lg)
    lg.show()