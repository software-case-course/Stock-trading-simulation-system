
from PyQt5.QtWidgets import QMainWindow


import mainwindowui
import UserInfo

users=[]

class MainWindow(QMainWindow, mainwindowui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.selectlogin.clicked.connect(self.loginpage)
        self.loginbutton_2.clicked.connect(self.login)
        self.reloginbutton.clicked.connect(self.relogin)



    def loginpage(self):
        self.loginbutton_2.setText('登陆')
        self.accountnumberline.setText('')
        self.passwordline.setText('')
        self.tabWidget.setCurrentIndex(0)

    def relogin(self):
        if self.loginbutton_2.text()=='登陆':
            self.loginbutton_2.setText('注册')

    def login(self):
        if self.loginbutton_2.text()=='登陆':
            user=UserInfo.userinfo.login(users, self.accountnumberline.text(), self.passwordline.text())
            if user!=0:
                print('登陆成功')
                self.username.setText(user.username)
            else:
                print('登陆失败')

        else:
            user=UserInfo.userinfo.register(users, self.accountnumberline.text(), self.passwordline.text())
            if user!=0:
                print('注册成功')
            else:
                print('注册失败')

