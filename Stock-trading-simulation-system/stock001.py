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
        MainWindow.resize(362, 538)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 110, 361, 111))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.StockNameEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.StockNameEdit.setObjectName("StockNameEdit")
        self.horizontalLayout_2.addWidget(self.StockNameEdit)
        self.StockNameButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.StockNameButton.setObjectName("StockNameButton")
        self.horizontalLayout_2.addWidget(self.StockNameButton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 111))
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
        self.StockCodeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.StockCodeButton.setObjectName("StockCodeButton")
        self.StockCodeButton.clicked.connect(self.ShowStockInfo)
        self.horizontalLayout.addWidget(self.StockCodeButton)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(5, 231, 351, 291))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "股票名称:"))
        self.StockNameButton.setText(_translate("MainWindow", "查询"))
        self.label.setText(_translate("MainWindow", "股票代码:"))
        self.StockCodeButton.setText(_translate("MainWindow", "查询"))
        # self.tableView_set()

    # def tableView_set(self):
    #
    #     # 添加表头：
    #

    def ShowStockInfo(self):
        self.StockCodeEdit.setText('162411')
        quotation = easyquotation.use('sina')
        print(quotation.stocks('162411'))
        stockdate = quotation.stocks(self.StockCodeEdit.text())
        stockdate = stockdate[self.StockCodeEdit.text()]
        print(stockdate['name'])

        self.model = QtGui.QStandardItemModel(self.tableView)

        self.tableView.verticalHeader().setVisible(False)
        self.tableView.horizontalHeader().setVisible(False)

        self.model.setColumnCount(2)
        self.model.setRowCount(10)
        self.model.setItem(0, 0, QtGui.QStandardItem('股票名称'))
        self.model.setItem(0, 1,QtGui.QStandardItem(stockdate['name']))
        self.model.setItem(1, 0, QtGui.QStandardItem('股票代码'))
        self.model.setItem(1, 1, QtGui.QStandardItem(self.StockCodeEdit.text()))
        self.model.setItem(2, 0, QtGui.QStandardItem('股票名称'))
        self.model.setItem(2, 1, QtGui.QStandardItem(stockdate['name']))


        self.tableView.setModel(self.model)




