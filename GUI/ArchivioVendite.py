from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import *

from GestioneSistema.Sistema import Sistema


class ArchivioVendite(QDialog):
    def __init__(self):
        super(ArchivioVendite, self).__init__()
        loadUi("archiviovendite.ui", self)
        self.homeBtn.clicked.connect(self.returnHome)
        self.Ricercavenditabtn.clicked.connect(self.ricercaVendite)
        self.popolaVendite()

    def returnHome(self):
        from GUI.FunzionalitaScreen import FunzionalitaScreen
        self.funzionalita = FunzionalitaScreen()
        self.close()
        self.funzionalita.show()

    def popolaVendite(self):
        self.arcVenditeTable.setRowCount(0)  # fa partire da vuota la table
        Sistema.downloadArchivioVendite()
        row = 0
        self.arcVenditeTable.setRowCount(Sistema.nVendite)  # setto la quangtità di righe della table come uguale alla lunghezza della lista di appuntamenti
        for vendita in Sistema.archivioVendite:
            self.arcVenditeTable.setItem(row, 0, QTableWidgetItem(str(vendita.get_codicevendita())))
            self.arcVenditeTable.setItem(row, 1, QTableWidgetItem(vendita.get_totvendita()))  # nella colonna cf metto il cf dell'appuntamento i esimo
            self.arcVenditeTable.setItem(row, 2, QTableWidgetItem(vendita.get_datavendita().strftime("%y-%m-%d")))
            row = row + 1

    def ricercaVendite(self):
        param = self.ricercavendita.text()
        venditeRicercate = []
        if (param == ""):
            self.popolaVendite()
            return
        for element in Sistema.archivioVendite:
            if str(param) in str(element.get_codicevendita()):
                venditeRicercate.append(element)
        self.popolaRicercaVendite(venditeRicercate)

    def popolaRicercaVendite(self, venditeRicercate):
        row = 0
        self.arcVenditeTable.setRowCount(len(venditeRicercate))  # setto la quangtità di righe della table come uguale alla lunghezza della lista di appuntamenti
        for vendita in venditeRicercate:
            self.arcVenditeTable.setItem(row, 0, QTableWidgetItem(str(vendita.get_codicevendita())))  # nella colonna id appuntamneto metto l'id dell'appuntamento i esimo
            self.arcVenditeTable.setItem(row, 1, QTableWidgetItem(vendita.get_totvendita()))  # nella colonna cf metto il cf dell'appuntamento i esimo
            self.arcVenditeTable.setItem(row, 2, QTableWidgetItem(vendita.get_datavendita().strftime("%y-%m-%d")))
            row = row + 1


