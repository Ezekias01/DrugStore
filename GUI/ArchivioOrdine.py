from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import *

from GestioneSistema.Sistema import Sistema


class ArchivioOrdine(QDialog):
    def __init__(self):
        super(ArchivioOrdine, self).__init__()
        loadUi("archivioordini.ui", self)
        self.homeBtn.clicked.connect(self.returnHome)
        self.Ricercaordinebtn.clicked.connect(self.ricercaOrdini)
        self.popolaArchOrdini()

    def returnHome(self):
        from GUI.FunzionalitaScreen import FunzionalitaScreen
        self.funzionalita = FunzionalitaScreen()
        self.close()
        self.funzionalita.show()

    def popolaArchOrdini(self):
        self.arcOrdineTable.setRowCount(0)
        Sistema.downloadArchivioOrdini()
        row = 0
        self.arcOrdineTable.setRowCount(len(Sistema.archivioOrdini))  # setto la quangtità di righe della table come uguale alla lunghezza della lista di appuntamenti
        for ordine in Sistema.archivioOrdini:
            self.arcOrdineTable.setItem(row, 0, QTableWidgetItem(str(ordine.get_codiceordine())))
            self.arcOrdineTable.setItem(row, 1, QTableWidgetItem(ordine.get_fornitore()))
            self.arcOrdineTable.setItem(row, 2, QTableWidgetItem(ordine.get_totordine()))  # nella colonna cf metto il cf dell'appuntamento i esimo
            self.arcOrdineTable.setItem(row, 3, QTableWidgetItem(ordine.get_dataordine().strftime("%y-%m-%d")))
            row = row + 1

    def ricercaOrdini(self):
        param = self.ricercaordine.text()
        ordiniRicercati = []
        if (param == ""):
            self.popolaArchOrdini()
            return
        for element in Sistema.archivioOrdini:
            if str(param) in str(element.get_codiceordine()) or str(param) in element.get_fornitore():
                ordiniRicercati.append(element)
        self.popolaRicercaOrdini(ordiniRicercati)

    def popolaRicercaOrdini(self, ordiniRicercati):
        row = 0
        self.arcOrdineTable.setRowCount(len(ordiniRicercati))  # setto la quangtità di righe della table come uguale alla lunghezza della lista di appuntamenti
        for ordine in ordiniRicercati:
            self.arcOrdineTable.setItem(row, 0, QTableWidgetItem(str(ordine.get_codiceordine())))
            self.arcOrdineTable.setItem(row, 1, QTableWidgetItem(ordine.get_fornitore()))
            self.arcOrdineTable.setItem(row, 2, QTableWidgetItem(ordine.get_totordine()))  # nella colonna cf metto il cf dell'appuntamento i esimo
            self.arcOrdineTable.setItem(row, 3, QTableWidgetItem(ordine.get_dataordine().strftime("%y-%m-%d")))
            row = row + 1


