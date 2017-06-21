
from PyQt5.QtWidgets import QMainWindow


import mainwindowui,UserInfo,easyquotation,pickle


users=[]
user=None

class MainWindow(QMainWindow, mainwindowui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.selectlogin.clicked.connect(self.loginpage)
        self.loginbutton_2.clicked.connect(self.login)
        self.reloginbutton.clicked.connect(self.relogin)
        self.searcherbutton.clicked.connect(self.search)
        self.buybutton.clicked.connect(self.buy)
        # self.sellbutton.clicked.connect(self.sell)



    def loginpage(self):
        self.loginbutton_2.setText('登陆')
        self.accountnumberline.setText('')
        self.passwordline.setText('')
        self.tabWidget.setCurrentIndex(0)

    def relogin(self):
        if self.loginbutton_2.text()=='登陆':
            self.loginbutton_2.setText('注册')
            self.tabWidget.setCurrentIndex(0)

    def login(self):
        global users,user
        if self.loginbutton_2.text()=='登陆':
            users=pickle.load(open("user.data", "rb"))
            user=UserInfo.userinfo.login(users, self.accountnumberline.text(), self.passwordline.text())
            if user!=0:
                print('登陆成功')

                self.username.setText(user.username)
                self.remainder.setText(str(user.money))
                self.tabWidget.setCurrentIndex(1)

            else:
                print('登陆失败')

        else:
            user=UserInfo.userinfo.register(users, self.accountnumberline.text(), self.passwordline.text())
            if user!=0:

                print('注册成功')
                UserInfo.userinfo.save(users)
                self.loginpage()
            else:
                print('注册失败')

    def buy(self):
        global user
        if UserInfo.userinfo.butstock(user,self.sharenumberline.text(),int(self.numberbox.text()),float(self.sharepriceline.text())):
            print('购买成功')
            self.shareholdingline.setText(str(user.stocks[self.sharenumberline.text()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ]))



    def search(self):
        self.tabWidget.setCurrentIndex(2)

        code = self.StockCodeEdit.text()
        if code.isdigit() and len(code) == 6:
            if self.comboBox.currentText() == '新浪':
                quotation = easyquotation.use('sina')
                stockdata = quotation.stocks(code)
                if stockdata:
                    stockdata = stockdata[code]
                    print(stockdata)
                    self.sharenameline.setText(stockdata['name'])
                    self.sharenumberline.setText(self.StockCodeEdit.text())
                    self.sharepriceline.setText(str(stockdata['now']))
                    if user!=None:
                        if user.stocks.get(code)!=None:

                            self.shareholdingline.setText(str(user.stocks[code]))
                        else:

                            self.shareholdingline.setText('0')
                    else:
                        self.shareholdingline.setText('0')

                    # self.increaseline.setText()
                    self.datatimeline.setText(stockdata['time'])

                else:
                    self.StockCodeEdit.setText('请输入正确的股票代码')
            elif self.comboBox.currentText() == '腾讯':
                quotation = easyquotation.use('qq')
                stockdata = quotation.stocks(code)
                if stockdata:
                    stockdata = stockdata[code]
                    print(stockdata)
                    self.sharenameline.setText(stockdata['name'])
                    self.sharenumberline.setText(self.StockCodeEdit.text())
                    self.sharepriceline.setText(str(stockdata['now']))
                    if user!=None:
                        if user.stocks.get(code)!=None:

                            self.shareholdingline.setText(str(user.stocks[code]))
                        else:

                            self.shareholdingline.setText('0')
                    else:
                        self.shareholdingline.setText('0')

                    self.increaseline.setText(str(stockdata['振幅']))
                    self.datatimeline.setText(str(stockdata['datetime']))

                else:
                    self.StockCodeEdit.setText('请输入正确的股票代码')


        else:
            self.StockCodeEdit.setText('请输入6位数字的股票代码')

