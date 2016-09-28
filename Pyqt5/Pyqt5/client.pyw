import sys
import socket
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QCheckBox, QComboBox,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QMessageBox, QMenu, QPushButton, QSpinBox, QStyle, QSystemTrayIcon,
        QTextEdit, QVBoxLayout)
from PyQt5.QtCore import QTimer, Qt

from client_ui import Ui_Client_Form

class Program_Client_Gui(Ui_Client_Form):
    def __init__(self,dialog):
        Ui_Client_Form.__init__(self)
        self.setupUi(dialog)
      
        dialog.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
     #   dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
       # self.createActions()
        self.createTrayIcon()
        self.trayIcon.show()
     
       # self.trayIcon.setVisible
        self.connectbutton.clicked.connect(self.connect_to_server)
        self.sendButton.clicked.connect(self.send_request)
        self.showButton.clicked.connect(self.show_answer)
         #   self.showButton.setStyleSheet("background-image: url(:/bg1.png);")
        self.to_trayButton.clicked.connect(self.to_tray)
        self.closebutton.clicked.connect(self.close)
        self.trayIcon.setIcon(QIcon(':/bad.png'))
        self.trayIcon.activated.connect(self.iconActivated)

        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.result_string=""
    def iconActivated(self, reason):
        if reason in (QSystemTrayIcon.Trigger, QSystemTrayIcon.DoubleClick):
            self.restore()
        elif reason == QSystemTrayIcon.MiddleClick:
            self.showMessage()
            pass

    def showMessage(self):
        icon = QSystemTrayIcon.MessageIcon(3)
        self.trayIcon.showMessage("Status Server", "Na serwerze www.bitowy.pl nie działa usługa Apache!",icon, 3000 * 10000)

    def restore(self):
        dialog.showNormal()
    def minimize(self):
        dialog.showMinimized()
    def to_tray(self):
        dialog.hide()
    def createTrayIcon(self):
         self.trayIconMenu = QMenu()

         self.trayIconMenu.addAction("Restore",self.restore)
         self.trayIconMenu.addAction("To Tray",self.to_tray)
         self.trayIconMenu.addSeparator()
         self.trayIconMenu.addAction("Quit",self.close)

         self.trayIcon = QSystemTrayIcon()
         self.trayIcon.setContextMenu(self.trayIconMenu)

    def send_request(self):
        
        if self.radioBtnApache.isChecked():
           clients_input="n"
        elif self.radioBtnData.isChecked():
            clients_input="d"
        else:
            clients_input="q"
        self.soc.send(clients_input.encode("utf8"))
        result_bytes = self.soc.recv(4096) # the number means how the response can be in bytes  
        self.result_string = result_bytes.decode("utf8") # the return will be in bytes, so decode
        self.result_string= self.result_string.replace('\n',"")
        if (self.result_string == "inactive"):
            self.showMessage()
        if (self.result_string == 'stop'):
            self.soc.close()

    def show_answer(self):
        txt=self.result_string
        self.label.setText(txt)

    def connect_to_server(self):
        
        IP_ADDRES = '89.40.126.143'
        PORT = 12345
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.soc.bind(('',PORT))
        self.soc.connect((IP_ADDRES, 12345))
        welcom_message = self.soc.recv(4096) # the number means how the response can be in bytes  
        self.result_string = welcom_message.decode("utf8") # the return will be in bytes, so decode

        txt=self.result_string
        self.label.setText(txt)

        #self.timer = QTimer()
        #self.timer.setInterval(4000)
        #self.timer.timeout.connect(self.send_request)
        #self.timer.start()

    def close(self):
        clients_input="q"
        self.soc.send(clients_input.encode("utf8"))
        self.soc.close()
        self.trayIcon.hide()
        QtCore.QCoreApplication.exit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    program = Program_Client_Gui(dialog)
    dialog.show()
    
    sys.exit(app.exec_())