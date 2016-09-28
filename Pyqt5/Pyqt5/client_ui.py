# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Client_Form(object):
    def setupUi(self, Client_Form):
        Client_Form.setObjectName("Client_Form")
        Client_Form.resize(500, 500)
        Client_Form.setMinimumSize(QtCore.QSize(0, 0))
        Client_Form.setMaximumSize(QtCore.QSize(500, 500))
        Client_Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Client_Form.setAccessibleName("")
        Client_Form.setStyleSheet("background-image: url(:/seigaiha.png);")
        self.connectbutton = QtWidgets.QPushButton(Client_Form)
        self.connectbutton.setGeometry(QtCore.QRect(360, 80, 81, 32))
        self.connectbutton.setMouseTracking(True)
        self.connectbutton.setStyleSheet("background-image: url(:/button.png);")
        self.connectbutton.setCheckable(False)
        self.connectbutton.setFlat(True)
        self.connectbutton.setObjectName("connectbutton")
        self.closebutton = QtWidgets.QPushButton(Client_Form)
        self.closebutton.setGeometry(QtCore.QRect(360, 130, 81, 31))
        self.closebutton.setObjectName("closebutton")
        self.label = QtWidgets.QLabel(Client_Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(20, 0, 211, 81))
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.sendButton = QtWidgets.QPushButton(Client_Form)
        self.sendButton.setGeometry(QtCore.QRect(30, 220, 91, 31))
        self.sendButton.setObjectName("sendButton")
        self.showButton = QtWidgets.QPushButton(Client_Form)
        self.showButton.setGeometry(QtCore.QRect(30, 260, 91, 31))
        self.showButton.setObjectName("showButton")
        self.radioBtnApache = QtWidgets.QRadioButton(Client_Form)
        self.radioBtnApache.setGeometry(QtCore.QRect(30, 330, 111, 17))
        self.radioBtnApache.setChecked(True)
        self.radioBtnApache.setObjectName("radioBtnApache")
        self.radioBtnData = QtWidgets.QRadioButton(Client_Form)
        self.radioBtnData.setGeometry(QtCore.QRect(30, 360, 82, 17))
        self.radioBtnData.setObjectName("radioBtnData")
        self.radioBtnQuit = QtWidgets.QRadioButton(Client_Form)
        self.radioBtnQuit.setGeometry(QtCore.QRect(30, 390, 82, 17))
        self.radioBtnQuit.setObjectName("radioBtnQuit")
        self.to_trayButton = QtWidgets.QPushButton(Client_Form)
        self.to_trayButton.setGeometry(QtCore.QRect(360, 180, 81, 31))
        self.to_trayButton.setObjectName("to_trayButton")

        self.retranslateUi(Client_Form)
        QtCore.QMetaObject.connectSlotsByName(Client_Form)

    def retranslateUi(self, Client_Form):
        _translate = QtCore.QCoreApplication.translate
        Client_Form.setWindowTitle(_translate("Client_Form", "Client (Server Status)"))
        self.connectbutton.setText(_translate("Client_Form", "Connect"))
        self.closebutton.setText(_translate("Client_Form", "Close"))
        self.label.setText(_translate("Client_Form", "TextLabel"))
        self.sendButton.setText(_translate("Client_Form", "Send Request"))
        self.showButton.setText(_translate("Client_Form", "Show Answer"))
        self.radioBtnApache.setText(_translate("Client_Form", "Apache Status"))
        self.radioBtnData.setText(_translate("Client_Form", "Data"))
        self.radioBtnQuit.setText(_translate("Client_Form", "Quit"))
        self.to_trayButton.setText(_translate("Client_Form", "To tray"))

import client_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Client_Form = QtWidgets.QDialog()
    ui = Ui_Client_Form()
    ui.setupUi(Client_Form)
    Client_Form.show()
    sys.exit(app.exec_())

