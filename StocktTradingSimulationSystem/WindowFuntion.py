
from PyQt5.QtWidgets import QMainWindow,QTableWidgetItem,QMessageBox



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
        self.sellbutton.clicked.connect(self.sell)
        self.StockCodeEdit.setPlaceholderText('请输入查询股票代码')
        self.informationbutton.clicked.connect(self.updateinfo)



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
                QMessageBox.information(self, '欢迎', '登陆成功')
                self.username.setText(user.username)
                self.remainder.setText(str(user.money))
                self.tabWidget.setCurrentIndex(1)
                self.updateinfo()

            else:
                print('登陆失败')
                QMessageBox.information(self, '登陆失败', '登陆失败，请检查用户名或密码是否正确')

        else:
            user=UserInfo.userinfo.register(users, self.accountnumberline.text(), self.passwordline.text())
            if user!=0:

                print('注册成功')
                QMessageBox.information(self, '成功', '注册成功')
                UserInfo.userinfo.save(users)
                self.loginpage()
            else:
                print('注册失败')
                QMessageBox.information(self, '注册失败', '注册失败，用户名重复')

    def buy(self):
        if self.sharenumberline.text()=='':
            QMessageBox.information(self, '购买失败', '请选择购买股票')
        else:
            global user,users
            if UserInfo.userinfo.butstock(user,self.sharenumberline.text(),int(self.numberbox.text()),float(self.sharepriceline.text())):
                print('购买成功')
                self.shareholdingline.setText(str(user.stocks[self.sharenumberline.text()]))
                self.updateinfo()
                users.append(user)
                UserInfo.userinfo.save(users)
            else:
                QMessageBox.information(self, '购买失败', '余额不足')
    def sell(self):
        if self.sharenumberline.text()=='':
            QMessageBox.information(self, '卖出失败', '请选择购买股票')
        else:
            global user
            if UserInfo.userinfo.sellstock(user,self.sharenumberline.text(),int(self.numberbox.text()),float(self.sharepriceline.text())):
                print('卖出成功')
                self.shareholdingline.setText(str(user.stocks[self.sharenumberline.text()]))

                users.append(user)
                UserInfo.userinfo.save(users)
                self.updateinfo()

            else:
                QMessageBox.information(self, '卖出失败', '请确认卖出数量')

    def updateinfo(self):
        global user
        self.remainder.setText(str("%.2f" % user.money))
        self.tabWidget.setCurrentIndex(1)
        if user!=None:
            self.tableWidget.setRowCount(len(user.stocks))
            i=0
            for code in user.stocks:
                quotationall = easyquotation.use('qq')
                stock=quotationall.stocks(code)
                self.tableWidget.setItem(i,1,QTableWidgetItem(code))
                self.tableWidget.setItem(i, 0, QTableWidgetItem(stock[code]['name']))

                self.tableWidget.setItem(i, 3, QTableWidgetItem(str(stock[code]['涨跌(%)'])+'%'))

                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(stock[code]['now'])))
                self.tableWidget.setItem(i, 4, QTableWidgetItem(str(stock[code]['open'])))
                self.tableWidget.setItem(i, 5, QTableWidgetItem(str(stock[code]['close'])))
                self.tableWidget.setItem(i, 6, QTableWidgetItem(str(stock[code]['datetime'])))
                self.tableWidget.setItem(i, 7, QTableWidgetItem(str(user.stocks[code])))
                self.tableWidget.setItem(i, 8, QTableWidgetItem(str("%.2f" % (int(user.stocks[code])*stock[code]['now']))))
                self.tableWidget.resizeColumnsToContents()
                self.tableWidget.resizeRowsToContents()

                i += 1



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
                    QMessageBox.information(self, "错误", "请输入正确的股票代码")
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
                    QMessageBox.information(self, "错误", "请输入正确的股票代码")



        else:
            QMessageBox.information(self, '错误', "请输入6位数字的股票代码")

