# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stock01.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

import easyquotation
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(451, 395)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 421, 75))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.StockCodeEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.StockCodeEdit.setObjectName("StockCodeEdit")
        self.horizontalLayout.addWidget(self.StockCodeEdit)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.StockCodeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.StockCodeButton.setObjectName("StockCodeButton")
        self.StockCodeButton.clicked.connect(self.ShowStockInfo)
        self.horizontalLayout.addWidget(self.StockCodeButton)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 90, 421, 291))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "股票实时信息查询"))
        self.label.setText(_translate("MainWindow", "股票代码:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "新浪"))
        self.comboBox.setItemText(1, _translate("MainWindow", "腾讯"))
        self.StockCodeButton.setText(_translate("MainWindow", "查询"))

    #self.StockCodeButton.clicked.connect(self.ShowStockInfo)




    def ShowStockInfo(self):
        #self.StockCodeEdit.setText('162411')
        code=self.StockCodeEdit.text()
        if code.isdigit() and len(code)==6 :
            if self.comboBox.currentText()=='新浪':
                quotation = easyquotation.use('sina')
            elif self.comboBox.currentText()=='腾讯':
                quotation = easyquotation.use('qq')
            stockdata = quotation.stocks(code)
            if stockdata:
                stockdata = stockdata[code]
                print(stockdata)
                self.model = QtGui.QStandardItemModel(self.tableView)

                self.tableView.verticalHeader().setVisible(False)
                self.tableView.horizontalHeader().setVisible(False)

                self.model.setColumnCount(2)
                self.model.setRowCount(8)
                self.model.setItem(1, 0, QtGui.QStandardItem('股票名称'))
                self.model.setItem(1, 1, QtGui.QStandardItem(stockdata['name']))
                self.model.setItem(0, 0, QtGui.QStandardItem('股票代码'))
                self.model.setItem(0, 1, QtGui.QStandardItem(self.StockCodeEdit.text()))
                self.model.setItem(2, 0, QtGui.QStandardItem('现价'))
                self.model.setItem(2, 1, QtGui.QStandardItem(str(stockdata['now'])))
                self.model.setItem(3, 0, QtGui.QStandardItem('开盘价'))
                self.model.setItem(3, 1, QtGui.QStandardItem(str(stockdata['open'])))
                self.model.setItem(4, 0, QtGui.QStandardItem('昨日收盘价'))
                self.model.setItem(4, 1, QtGui.QStandardItem(str(stockdata['close'])))
                self.model.setItem(5, 0, QtGui.QStandardItem('今日最高价'))
                self.model.setItem(5, 1, QtGui.QStandardItem(str(stockdata['high'])))
                self.model.setItem(5, 0, QtGui.QStandardItem('今日最低价'))
                self.model.setItem(5, 1, QtGui.QStandardItem(str(stockdata['low'])))
                self.model.setItem(6, 0, QtGui.QStandardItem('时间'))
                self.model.setItem(6, 1, QtGui.QStandardItem(stockdata['time']))
                self.model.setItem(7, 0, QtGui.QStandardItem('日期'))
                self.model.setItem(7, 1, QtGui.QStandardItem(stockdata['date']))

                self.tableView.setModel(self.model)
            else:
                self.StockCodeEdit.setText('请输入正确的股票代码')

        else:
            self.StockCodeEdit.setText('请输入6位数字的股票代码')
