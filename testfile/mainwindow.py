# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

import easyquotation
import logindialog
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(518, 344)
        MainWindow.setAutoFillBackground(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("")
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 491, 276))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.code = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.code.setObjectName("code")
        self.horizontalLayout_5.addWidget(self.code)
        self.codeinput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.codeinput.sizePolicy().hasHeightForWidth())
        self.codeinput.setSizePolicy(sizePolicy)
        self.codeinput.setObjectName("codeinput")
        self.horizontalLayout_5.addWidget(self.codeinput)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.search = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.search.setObjectName("search")
        self.horizontalLayout_5.addWidget(self.search)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setSpacing(6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.name = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.name.setObjectName("name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name)
        self.nameoutput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameoutput.sizePolicy().hasHeightForWidth())
        self.nameoutput.setSizePolicy(sizePolicy)
        self.nameoutput.setBaseSize(QtCore.QSize(0, 0))
        self.nameoutput.setObjectName("nameoutput")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameoutput)
        self.code2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.code2.setObjectName("code2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.code2)
        self.codeoutput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.codeoutput.sizePolicy().hasHeightForWidth())
        self.codeoutput.setSizePolicy(sizePolicy)
        self.codeoutput.setObjectName("codeoutput")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.codeoutput)
        self.price = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.price.setObjectName("price")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.price)
        self.priceoutput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.priceoutput.sizePolicy().hasHeightForWidth())
        self.priceoutput.setSizePolicy(sizePolicy)
        self.priceoutput.setObjectName("priceoutput")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.priceoutput)
        self.number = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.number.setBaseSize(QtCore.QSize(0, 0))
        self.number.setObjectName("number")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.number)
        self.numberoutput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberoutput.sizePolicy().hasHeightForWidth())
        self.numberoutput.setSizePolicy(sizePolicy)
        self.numberoutput.setObjectName("numberoutput")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.numberoutput)
        self.increase = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.increase.setObjectName("increase")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.increase)
        self.increaseoutput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.increaseoutput.sizePolicy().hasHeightForWidth())
        self.increaseoutput.setSizePolicy(sizePolicy)
        self.increaseoutput.setObjectName("increaseoutput")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.increaseoutput)
        self.time = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.time.setObjectName("time")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.time)
        self.timeoutput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeoutput.sizePolicy().hasHeightForWidth())
        self.timeoutput.setSizePolicy(sizePolicy)
        self.timeoutput.setBaseSize(QtCore.QSize(0, 0))
        self.timeoutput.setObjectName("timeoutput")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.timeoutput)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.account = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.account.setObjectName("account")
        self.verticalLayout_4.addWidget(self.account)
        self.purchase = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.purchase.setObjectName("purchase")
        self.verticalLayout_4.addWidget(self.purchase)
        self.sell = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sell.setObjectName("sell")
        self.verticalLayout_4.addWidget(self.sell)
        self.accountinformation = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.accountinformation.setObjectName("accountinformation")
        self.verticalLayout_4.addWidget(self.accountinformation)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 0, 401, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.search.clicked.connect(self.ShowStock)

        self.account.clicked.connect(self.showbox)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showbox(self):

        self.account.hide()

        # QtWidgets.QMessageBox.information(self.pushButton, "标题", "这是第一个PyQt5 GUI程序")

        # lg = QDialog()
        # ui = logindialog.Ui_logindialog()
        # qss_file = open('qss/black.css').read()
        # lg.setStyleSheet(qss_file)
        # ui.setupUi(lg)
        # lg.show()
        # if lg.exec_()==1:
        #     print(ui.username.e)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "股票模拟系统"))
        self.code.setText(_translate("MainWindow", "股票代码："))
        self.comboBox.setItemText(0, _translate("MainWindow", "腾讯"))
        self.comboBox.setItemText(1, _translate("MainWindow", "新浪"))
        self.search.setText(_translate("MainWindow", "查询"))
        self.name.setText(_translate("MainWindow", "股票名称："))
        self.code2.setText(_translate("MainWindow", "股票代码："))
        self.price.setText(_translate("MainWindow", "股票单价："))
        self.number.setText(_translate("MainWindow", "持股数量："))
        self.increase.setText(_translate("MainWindow", "  涨幅："))
        self.time.setText(_translate("MainWindow", "数据时间："))
        self.account.setText(_translate("MainWindow", "账户登陆"))
        self.purchase.setText(_translate("MainWindow", "股票购入"))
        self.sell.setText(_translate("MainWindow", "股票售出"))
        self.accountinformation.setText(_translate("MainWindow", "个人股票信息"))
        self.label.setText(_translate("MainWindow", "当前登录账号:"))
        self.label_2.setText(_translate("MainWindow", "用户1"))
        self.pushButton.setText(_translate("MainWindow", "退出登录"))

    def ShowStock(self):
        self.account.show()
        # self.StockCodeEdit.setText('162411')
        code = self.codeinput.text()
        if code.isdigit() and len(code) == 6:
            if self.comboBox.currentText() == '新浪':
                quotation = easyquotation.use('sina')
                stockdata = quotation.stocks(code)
                if stockdata:
                    stockdata = stockdata[code]
                    print(stockdata)
                    self.nameoutput.setText(stockdata['name'])
                    self.codeoutput.setText(code)
                    self.priceoutput.setText(str(stockdata['now']))
                    self.timeoutput.setText(stockdata['time'])
                    self.numberoutput.setText('0')


                else:
                    self.codeinput.setText('请输入正确的股票代码')
            elif self.comboBox.currentText() == '腾讯':
                quotation = easyquotation.use('qq')
                stockdata = quotation.stocks(code)
                if stockdata:
                    stockdata = stockdata[code]
                    print(stockdata)
                    self.nameoutput.setText(stockdata['name'])
                    self.codeoutput.setText(code)
                    self.priceoutput.setText(str(stockdata['now']))
                    self.increaseoutput.setText(str(stockdata['涨跌(%)']) + '%')
                    self.timeoutput.setText(str(stockdata['datetime']))
                    self.numberoutput.setText('0')



                else:
                    self.codeinput.setText('请输入正确的股票代码')


        else:
            self.codeinput.setText('请输入6位数字的股票代码')

