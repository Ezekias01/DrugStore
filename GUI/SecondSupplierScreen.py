from IPython.external.qt_for_kernel import QtGui, QtCore
from PyQt5.uic import *
from PyQt5.QtWidgets import *

from GUI.ArchivioClienti import ArchivioClienti
from GUI.ArchivioEsiti import ArchivioEsiti
from GUI.ArchivioVendite import ArchivioVendite
from GUI.CalendarioScreen import CalendarioScreen


class SecondSupplierScreen(QDialog):
    def __init__(self):
        super(SecondSupplierScreen, self).__init__()
        loadUi("menusecondofornitore.ui", self)
        self.homeBtn.clicked.connect(self.returnHome)

    def returnHome(self):
        from GUI.FunzionalitaScreen import FunzionalitaScreen
        self.funzionalita = FunzionalitaScreen()
        self.close()
        self.funzionalita.show()


