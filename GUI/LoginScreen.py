from PyQt5.uic import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from GUI.FunzionalitaScreen import FunzionalitaScreen


class LoginScreen(QDialog):

    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("loginscreen.ui", self)
        self.passfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginButton.clicked.connect(self.loginfunction)
        self.checkPass.clicked.connect(self.checkPassword)
        self.show()


    def gotoFunzionalita(self):
        self.funzionalita = FunzionalitaScreen()
        self.close()
        self.funzionalita.show()

    def loginfunction(self):
        password = self.passfield.text()
        user = self.userfield.text()

        if len(password) == 0 or len(user) == 0:
            self.label3.setText("Riempi campo vuoto")
        else:
            if user == "FarmaciaAncona" and password == "tachitachi":
                self.loginButton.clicked.connect(self.gotoFunzionalita)
            else:
                self.label3.setText("Password o Username errati")

    def checkPassword(self):
        if (self.checkPass.isChecked()):
            self.passfield.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.passfield.setEchoMode(QtWidgets.QLineEdit.Password)