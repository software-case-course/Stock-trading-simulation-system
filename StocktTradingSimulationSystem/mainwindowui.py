# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowui.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(881, 643)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 891, 601))
        self.widget.setStyleSheet("background-image: url(:/images/background);")
        self.widget.setObjectName("widget")
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 110, 861, 471))
        self.tabWidget.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_login = QtWidgets.QWidget()
        self.tab_login.setObjectName("tab_login")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_login)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(320, 90, 251, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.accountnumbetlabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.accountnumbetlabel.setStyleSheet("font: 14pt \"04b_21\";")
        self.accountnumbetlabel.setObjectName("accountnumbetlabel")
        self.horizontalLayout_3.addWidget(self.accountnumbetlabel)
        self.accountnumberline = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.accountnumberline.setObjectName("accountnumberline")
        self.horizontalLayout_3.addWidget(self.accountnumberline)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_login)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(320, 160, 251, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.passwordlabel = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.passwordlabel.setStyleSheet("font: 14pt \"04b_21\";")
        self.passwordlabel.setObjectName("passwordlabel")
        self.horizontalLayout_4.addWidget(self.passwordlabel)
        self.passwordline = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.passwordline.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordline.setObjectName("passwordline")
        self.horizontalLayout_4.addWidget(self.passwordline)
        self.loginbutton_2 = QtWidgets.QPushButton(self.tab_login)
        self.loginbutton_2.setGeometry(QtCore.QRect(390, 240, 101, 31))
        self.loginbutton_2.setStyleSheet("font: 14pt \"04b_21\";")
        self.loginbutton_2.setObjectName("loginbutton_2")
        self.tabWidget.addTab(self.tab_login, "")
        self.tab_stocks = QtWidgets.QWidget()
        self.tab_stocks.setObjectName("tab_stocks")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_stocks)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 831, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tabWidget.addTab(self.tab_stocks, "")
        self.tab_trade = QtWidgets.QWidget()
        self.tab_trade.setObjectName("tab_trade")
        self.informationbox = QtWidgets.QGroupBox(self.tab_trade)
        self.informationbox.setGeometry(QtCore.QRect(10, 20, 581, 381))
        self.informationbox.setObjectName("informationbox")
        self.informationbutton = QtWidgets.QPushButton(self.informationbox)
        self.informationbutton.setGeometry(QtCore.QRect(430, 340, 101, 23))
        self.informationbutton.setObjectName("informationbutton")
        self.layoutWidget = QtWidgets.QWidget(self.informationbox)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 501, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sharename = QtWidgets.QLabel(self.layoutWidget)
        self.sharename.setObjectName("sharename")
        self.horizontalLayout_5.addWidget(self.sharename)
        self.sharenameline = QtWidgets.QLineEdit(self.layoutWidget)
        self.sharenameline.setObjectName("sharenameline")
        self.horizontalLayout_5.addWidget(self.sharenameline)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sharenumber = QtWidgets.QLabel(self.layoutWidget)
        self.sharenumber.setObjectName("sharenumber")
        self.horizontalLayout_7.addWidget(self.sharenumber)
        self.sharenumberline = QtWidgets.QLineEdit(self.layoutWidget)
        self.sharenumberline.setObjectName("sharenumberline")
        self.horizontalLayout_7.addWidget(self.sharenumberline)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.shareprice = QtWidgets.QLabel(self.layoutWidget)
        self.shareprice.setObjectName("shareprice")
        self.horizontalLayout_10.addWidget(self.shareprice)
        self.sharepriceline = QtWidgets.QLineEdit(self.layoutWidget)
        self.sharepriceline.setObjectName("sharepriceline")
        self.horizontalLayout_10.addWidget(self.sharepriceline)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.shareholding = QtWidgets.QLabel(self.layoutWidget)
        self.shareholding.setObjectName("shareholding")
        self.horizontalLayout_9.addWidget(self.shareholding)
        self.shareholdingline = QtWidgets.QLineEdit(self.layoutWidget)
        self.shareholdingline.setObjectName("shareholdingline")
        self.horizontalLayout_9.addWidget(self.shareholdingline)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.increase = QtWidgets.QLabel(self.layoutWidget)
        self.increase.setMinimumSize(QtCore.QSize(71, 0))
        self.increase.setObjectName("increase")
        self.horizontalLayout_11.addWidget(self.increase)
        self.increaseline = QtWidgets.QLineEdit(self.layoutWidget)
        self.increaseline.setMinimumSize(QtCore.QSize(418, 0))
        self.increaseline.setMaximumSize(QtCore.QSize(418, 16777215))
        self.increaseline.setObjectName("increaseline")
        self.horizontalLayout_11.addWidget(self.increaseline)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.datatime = QtWidgets.QLabel(self.layoutWidget)
        self.datatime.setObjectName("datatime")
        self.horizontalLayout_8.addWidget(self.datatime)
        self.datatimeline = QtWidgets.QLineEdit(self.layoutWidget)
        self.datatimeline.setObjectName("datatimeline")
        self.horizontalLayout_8.addWidget(self.datatimeline)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.layoutWidget.raise_()
        self.informationbutton.raise_()
        self.tradebox = QtWidgets.QGroupBox(self.tab_trade)
        self.tradebox.setGeometry(QtCore.QRect(620, 160, 191, 121))
        self.tradebox.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.tradebox.setObjectName("tradebox")
        self.layoutWidget1 = QtWidgets.QWidget(self.tradebox)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 141, 26))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.numberbox = QtWidgets.QSpinBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.numberbox.setFont(font)
        self.numberbox.setMouseTracking(False)
        self.numberbox.setProperty("value", 10)
        self.numberbox.setObjectName("numberbox")
        self.horizontalLayout_13.addWidget(self.numberbox)
        self.numberline = QtWidgets.QLabel(self.layoutWidget1)
        self.numberline.setMaximumSize(QtCore.QSize(21, 16777215))
        self.numberline.setObjectName("numberline")
        self.horizontalLayout_13.addWidget(self.numberline)
        self.layoutWidget2 = QtWidgets.QWidget(self.tradebox)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 70, 158, 29))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.buybutton = QtWidgets.QPushButton(self.layoutWidget2)
        self.buybutton.setObjectName("buybutton")
        self.horizontalLayout_15.addWidget(self.buybutton)
        self.sellbutton = QtWidgets.QPushButton(self.layoutWidget2)
        self.sellbutton.setObjectName("sellbutton")
        self.horizontalLayout_15.addWidget(self.sellbutton)
        self.tabWidget.addTab(self.tab_trade, "")
        self.tab_test = QtWidgets.QWidget()
        self.tab_test.setObjectName("tab_test")
        self.tabWidget.addTab(self.tab_test, "")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(500, 20, 351, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.StockCodeEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.StockCodeEdit.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.StockCodeEdit.setObjectName("StockCodeEdit")
        self.horizontalLayout.addWidget(self.StockCodeEdit)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.searcherbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.searcherbutton.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.searcherbutton.setObjectName("searcherbutton")
        self.horizontalLayout.addWidget(self.searcherbutton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 211, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.username = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.username.setStyleSheet("QLabel{\n"
"     border-width: 2px;\n"
"     border-style: solid;\n"
"     border-color: rgb(100, 160,220);\n"
"     border-radius:15px;\n"
"     font: 10pt \"微软雅黑\";\n"
"}")
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.horizontalLayout_2.addWidget(self.username)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.selectlogin = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.selectlogin.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.selectlogin.setObjectName("selectlogin")
        self.verticalLayout_2.addWidget(self.selectlogin)
        self.reloginbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.reloginbutton.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.reloginbutton.setObjectName("reloginbutton")
        self.verticalLayout_2.addWidget(self.reloginbutton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.remainderlabel = QtWidgets.QLabel(self.widget)
        self.remainderlabel.setGeometry(QtCore.QRect(250, 40, 101, 31))
        self.remainderlabel.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.remainderlabel.setObjectName("remainderlabel")
        self.remainder = QtWidgets.QLabel(self.widget)
        self.remainder.setGeometry(QtCore.QRect(350, 40, 121, 41))
        self.remainder.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.remainder.setStyleSheet("QLabel{\n"
"     border-width: 2px;\n"
"     border-style: solid;\n"
"     border-color: rgb(100, 160,220);\n"
"     border-radius:15px;\n"
"     font: 10pt \"微软雅黑\";\n"
"}")
        self.remainder.setAlignment(QtCore.Qt.AlignCenter)
        self.remainder.setObjectName("remainder")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.accountnumbetlabel.setText(_translate("MainWindow", "账号："))
        self.passwordlabel.setText(_translate("MainWindow", "密码："))
        self.loginbutton_2.setText(_translate("MainWindow", "登陆"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_login), _translate("MainWindow", "登陆注册页"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "股票名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "股票代码"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "当前价格"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "开盘价"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "昨日收盘价"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "上次刷新时间"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "持股数"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "买入价格"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "总金额"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stocks), _translate("MainWindow", " 股票信息"))
        self.informationbox.setTitle(_translate("MainWindow", "       股票信息"))
        self.informationbutton.setText(_translate("MainWindow", "个人股票信息"))
        self.sharename.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">股票名称：</span></p></body></html>"))
        self.sharenumber.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">股票代码：</span></p></body></html>"))
        self.shareprice.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">股票单价：</span></p></body></html>"))
        self.shareholding.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">持股数量：</span></p></body></html>"))
        self.increase.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">涨幅：</span></p></body></html>"))
        self.datatime.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">数据时间：</span></p></body></html>"))
        self.tradebox.setTitle(_translate("MainWindow", " 交易"))
        self.numberline.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">股</span></p></body></html>"))
        self.buybutton.setText(_translate("MainWindow", "买入"))
        self.sellbutton.setText(_translate("MainWindow", "卖出"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_trade), _translate("MainWindow", "股票交易"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_test), _translate("MainWindow", "Tab test"))
        self.StockCodeEdit.setText(_translate("MainWindow", "请输入股票代码"))
        self.comboBox.setItemText(0, _translate("MainWindow", "腾讯"))
        self.comboBox.setItemText(1, _translate("MainWindow", "新浪"))
        self.searcherbutton.setText(_translate("MainWindow", "查询"))
        self.username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">游客</span></p></body></html>"))
        self.selectlogin.setText(_translate("MainWindow", "登陆"))
        self.reloginbutton.setText(_translate("MainWindow", "注册"))
        self.remainderlabel.setText(_translate("MainWindow", "账户余额："))
        self.remainder.setText(_translate("MainWindow", "0"))

