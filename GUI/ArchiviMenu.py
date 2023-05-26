from IPython.external.qt_for_kernel import QtGui, QtCore
from PyQt5.uic import *
from PyQt5.QtWidgets import *

from GUI.ArchivioClienti import ArchivioClienti
from GUI.ArchivioEsiti import ArchivioEsiti
from GUI.ArchivioOrdine import ArchivioOrdine
from GUI.ArchivioVendite import ArchivioVendite
from GUI.CalendarioScreen import CalendarioScreen
from GUI.FornitoriMenu import FornitoriMenu



class ArchiviMenu(QDialog):
    def __init__(self):
        super(ArchiviMenu, self).__init__()
        loadUi("archiviscreen.ui", self)
        self.archclientiBtn.clicked.connect(self.gotoArchivioClienti)
        self.archesitiBtn.clicked.connect(self.gotoArchivioEsiti)
        self.archvenditeBtn.clicked.connect(self.gotoArchivioVendite)
        self.archordiniButton.clicked.connect(self.gotoArchivioOrdini)
        self.homeBtn.clicked.connect(self.returnHome)


    def returnHome(self):
        from GUI.FunzionalitaScreen import FunzionalitaScreen
        self.funzionalita = FunzionalitaScreen()
        self.close()
        self.funzionalita.show()

    def gotoArchivioOrdini(self):
        self.ordini = ArchivioOrdine()
        self.close()
        self.ordini.show()

    def gotoArchivioClienti(self):
        self.client = ArchivioClienti()
        self.close()
        self.client.show()

    def gotoArchivioEsiti(self):
        self.esiti = ArchivioEsiti()
        self.close()
        self.esiti.show()

    def gotoArchivioVendite(self):
        self.vendita = ArchivioVendite()
        self.close()
        self.vendita.show()

