import sys

import WindowFuntion

# import qdarkstyle

from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = WindowFuntion.MainWindow()
    qss_file = open('qss//q.qss').read()
    mainWindow.setStyleSheet(qss_file)
    # mainWindow.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainWindow.show()
    sys.exit(app.exec_())
