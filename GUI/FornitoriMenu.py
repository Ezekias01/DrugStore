from IPython.external.qt_for_kernel import QtGui, QtCore
from PyQt5.uic import *
from PyQt5.QtWidgets import *

from GUI.ArchivioClienti import ArchivioClienti
from GUI.ArchivioEsiti import ArchivioEsiti
from GUI.ArchivioVendite import ArchivioVendite
from GUI.CalendarioScreen import CalendarioScreen
from GUI.FirstSupplierScreen import FirstSupplierScreen
from GUI.SecondSupplierScreen import SecondSupplierScreen


class FornitoriMenu(QDialog):
    def __init__(self):
        super(FornitoriMenu, self).__init__()
        loadUi("fornitoriscreen.ui", self)
        self.firstsuplButton.setGeometry(230, 370, 341, 331)
        self.secondsuplButton.setGeometry(630, 370, 341, 331)
        self.firstsuplButton.setStyleSheet("border-image : url(img/supl.png);")
        self.secondsuplButton.setStyleSheet("border-image : url(img/supl2.png);")
        self.firstsuplButton.clicked.connect(self.gotoFirstSupl)
        self.secondsuplButton.clicked.connect(self.gotoSecondSupl)
        self.homeBtn.clicked.connect(self.returnHome)

    def returnHome(self):
        from GUI.FunzionalitaScreen import FunzionalitaScreen
        self.funzionalita = FunzionalitaScreen()
        self.close()
        self.funzionalita.show()

    def gotoFirstSupl(self):
        self.firstsupplmenu = FirstSupplierScreen()
        self.close()
        self.firstsupplmenu.show()

    def gotoSecondSupl(self):
        self.secondsupplmenu = SecondSupplierScreen()
        self.close()
        self.secondsupplmenu.show()

