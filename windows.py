# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import functools
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1045, 640)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 500, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 500, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(150, 370, 591, 87))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(150, 20, 591, 341))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "发送"))
        self.pushButton_2.setText(_translate("Dialog", "退出"))
        self.pushButton_2.clicked.connect(functools.partial(self.click_exit, Dialog))
        self.pushButton.clicked.connect(self.click_send)

    def click_exit(self, dialog: QtWidgets.QMainWindow):
        assert isinstance(dialog, QtWidgets.QMainWindow), print('type error')
        dialog.close()

    def click_send(self):
        msg = self.textEdit.toPlainText()
        if len(msg) > 0:
            if len(self.textEdit_2.toPlainText()) > 0:
                self.textEdit_2.append(msg)
            else:
                self.textEdit_2.setText(msg)
            self.textEdit.clear()
        else:
            print('ee')
