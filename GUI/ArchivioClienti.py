from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import *

from GestioneSistema.Sistema import Sistema


class ArchivioClienti(QDialog):
    def __init__(self):
        super(ArchivioClienti, self).__init__()
        loadUi("archivioclienti.ui", self)
        self.homeBtn.clicked.connect(self.returnHome)
        self.Ricercaclientebtn.clicked.connect(self.ricercaClienti)
        self.popolaClienti()

    def returnHome(self):
        from GUI.FunzionalitaScreen import FunzionalitaScreen
        self.funzionalita = FunzionalitaScreen()
        self.close()
        self.funzionalita.show()

    def popolaClienti(self):
        self.ClientiTable.setRowCount(0)  # fa partire da vuota la table
        Sistema.downloadClienti()
        row = 0
        self.ClientiTable.setRowCount(len(Sistema.listaClienti))  # setto la quangtità di righe della table come uguale alla lunghezza della lista di appuntamenti
        for cliente in Sistema.listaClienti:
            self.ClientiTable.setItem(row, 0, QTableWidgetItem(
                cliente.get_nome()))  # nella colonna id appuntamneto metto l'id dell'appuntamento i esimo
            self.ClientiTable.setItem(row, 1, QTableWidgetItem(
                cliente.get_cognome()))  # nella colonna cf metto il cf dell'appuntamento i esimo
            self.ClientiTable.setItem(row, 2, QTableWidgetItem(cliente.get_cf()))
            row = row + 1

    def ricercaClienti(self):
        param = self.ricercacliente.text()
        clientiRicercati = []
        if (param == ""):
            self.popolaClienti()
            return
        for element in Sistema.listaClienti:
            if (param in element.get_nome() or param in element.get_cognome() or param in element.get_cf()):
                clientiRicercati.append(element)
        self.popolaRicercaClienti(clientiRicercati)

    def popolaRicercaClienti(self, esitiRicercati):
        row = 0
        self.ClientiTable.setRowCount(len(esitiRicercati))  # setto la quangtità di righe della table come uguale alla lunghezza della lista di appuntamenti
        for cliente in esitiRicercati:
            self.ClientiTable.setItem(row, 0, QTableWidgetItem(cliente.get_nome()))  # nella colonna id appuntamneto metto l'id dell'appuntamento i esimo
            self.ClientiTable.setItem(row, 1, QTableWidgetItem(cliente.get_cognome()))  # nella colonna cf metto il cf dell'appuntamento i esimo
            self.ClientiTable.setItem(row, 2, QTableWidgetItem(cliente.get_cf()))
            row = row + 1


