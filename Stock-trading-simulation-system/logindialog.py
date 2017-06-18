# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logindialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_logindialog(object):
    def setupUi(self, logindialog):
        logindialog.setObjectName("logindialog")
        logindialog.resize(242, 173)
        self.cancelbutton = QtWidgets.QDialogButtonBox(logindialog)
        self.cancelbutton.setGeometry(QtCore.QRect(30, 110, 161, 32))
        self.cancelbutton.setOrientation(QtCore.Qt.Horizontal)
        self.cancelbutton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.cancelbutton.setObjectName("cancelbutton")
        self.gridLayoutWidget = QtWidgets.QWidget(logindialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 20, 160, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.username = QtWidgets.QLabel(self.gridLayoutWidget)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 0, 1, 1)
        self.userpw = QtWidgets.QLabel(self.gridLayoutWidget)
        self.userpw.setObjectName("userpw")
        self.gridLayout.addWidget(self.userpw, 1, 0, 1, 1)
        self.Edit_username = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Edit_username.setObjectName("Edit_username")
        self.gridLayout.addWidget(self.Edit_username, 0, 1, 1, 1)
        self.Edit_passwd = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Edit_passwd.setObjectName("Edit_passwd")
        self.gridLayout.addWidget(self.Edit_passwd, 1, 1, 1, 1)

        self.retranslateUi(logindialog)
        self.cancelbutton.accepted.connect(logindialog.accept)
        self.cancelbutton.rejected.connect(logindialog.reject)
        QtCore.QMetaObject.connectSlotsByName(logindialog)

    def retranslateUi(self, logindialog):
        _translate = QtCore.QCoreApplication.translate
        logindialog.setWindowTitle(_translate("logindialog", "用户登陆"))
        self.username.setText(_translate("logindialog", "用户名"))
        self.userpw.setText(_translate("logindialog", "密码"))

