# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(953, 627)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 10, 891, 601))
        self.widget.setStyleSheet("background-image: url(:/images/background);")
        self.widget.setObjectName("widget")
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 110, 861, 471))
        self.tabWidget.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_login = QtWidgets.QWidget()
        self.tab_login.setObjectName("tab_login")
        self.label_2 = QtWidgets.QLabel(self.tab_login)
        self.label_2.setGeometry(QtCore.QRect(220, 140, 54, 12))
        self.label_2.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(self.tab_login)
        self.label_10.setGeometry(QtCore.QRect(220, 180, 54, 12))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_login, "")
        self.tab_stocks = QtWidgets.QWidget()
        self.tab_stocks.setObjectName("tab_stocks")
        self.tableView = QtWidgets.QTableView(self.tab_stocks)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 831, 411))
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.tab_stocks, "")
        self.tab_trade = QtWidgets.QWidget()
        self.tab_trade.setObjectName("tab_trade")
        self.groupBox = QtWidgets.QGroupBox(self.tab_trade)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 581, 381))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(430, 340, 101, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 501, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_7.addWidget(self.lineEdit_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_10.addWidget(self.lineEdit_8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_9.addWidget(self.lineEdit_7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(71, 0))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(418, 0))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(418, 16777215))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_11.addWidget(self.lineEdit_9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_8.addWidget(self.lineEdit_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.layoutWidget.raise_()
        self.pushButton_7.raise_()
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_trade)
        self.groupBox_2.setGeometry(QtCore.QRect(620, 160, 191, 121))
        self.groupBox_2.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 141, 26))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.spinBox.setFont(font)
        self.spinBox.setMouseTracking(False)
        self.spinBox.setProperty("value", 10)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_13.addWidget(self.spinBox)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setMaximumSize(QtCore.QSize(21, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_13.addWidget(self.label_4)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 70, 158, 29))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_15.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_15.addWidget(self.pushButton_9)
        self.tabWidget.addTab(self.tab_trade, "")
        self.tab_test = QtWidgets.QWidget()
        self.tab_test.setObjectName("tab_test")
        self.tabWidget.addTab(self.tab_test, "")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(520, 10, 351, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.checkbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.checkbutton.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.checkbutton.setObjectName("checkbutton")
        self.horizontalLayout.addWidget(self.checkbutton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 211, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setStyleSheet("QLabel{\n"
"     border-width: 2px;\n"
"     border-style: solid;\n"
"     border-color: rgb(0, 0,0);\n"
"     border-radius:15px;\n"
"     font: 10pt \"微软雅黑\";\n"
"}")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.loginbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.loginbutton.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.loginbutton.setObjectName("loginbutton")
        self.verticalLayout_2.addWidget(self.loginbutton)
        self.reloginbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.reloginbutton.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.reloginbutton.setObjectName("reloginbutton")
        self.verticalLayout_2.addWidget(self.reloginbutton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_login), _translate("MainWindow", "登陆页"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stocks), _translate("MainWindow", " 股票信息"))
        self.groupBox.setTitle(_translate("MainWindow", "       股票信息"))
        self.pushButton_7.setText(_translate("MainWindow", "个人股票信息"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">股票名称：</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">股票代码：</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">股票单价：</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">持股数量：</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">涨幅：</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">数据时间：</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", " 交易"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">股</span></p></body></html>"))
        self.pushButton_8.setText(_translate("MainWindow", "买入"))
        self.pushButton_9.setText(_translate("MainWindow", "卖出"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_trade), _translate("MainWindow", "股票交易"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_test), _translate("MainWindow", "Tab test"))
        self.lineEdit.setText(_translate("MainWindow", "请输入股票代码"))
        self.comboBox.setItemText(0, _translate("MainWindow", "腾讯"))
        self.comboBox.setItemText(1, _translate("MainWindow", "新浪"))
        self.checkbutton.setText(_translate("MainWindow", "查询"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">user</span></p></body></html>"))
        self.loginbutton.setText(_translate("MainWindow", "登陆"))
        self.reloginbutton.setText(_translate("MainWindow", "注销"))

