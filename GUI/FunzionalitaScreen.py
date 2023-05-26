from PyQt5.uic import *
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtGui, QtCore

from GUI.ArchiviMenu import ArchiviMenu
from GUI.CalendarioScreen import CalendarioScreen
from GUI.CassaScreen import CassaScreen
from GUI.MagazzinoScreen import MagazzinoScreen


class FunzionalitaScreen(QDialog):
    def __init__(self):
        super(FunzionalitaScreen, self).__init__()
        loadUi("funzionalitascreen.ui", self)
        self.tamponiButton.clicked.connect(self.gotoCalendario)
        self.archiviButton.clicked.connect(self.gotoArchivi)
        self.magazzinoButton.clicked.connect(self.gotoMagazzino)
        self.cassaButton.clicked.connect(self.gotoCassa)


    def gotoMagazzino(self):
        self.magazzino = MagazzinoScreen()
        self.close()
        self.magazzino.show()

    def gotoCassa(self):
        self.cassa = CassaScreen()
        self.close()
        self.cassa.show()

    def gotoCalendario(self):
        self.calendario = CalendarioScreen()
        self.close()
        self.calendario.show()

    def gotoArchivi(self):
        self.archivi = ArchiviMenu()
        self.close()
        self.archivi.show()

