import sys
import matplotlib.pyplot as plt
from IPython.external.qt_for_kernel import QtCore
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QApplication
from PyQt5.uic import *

from GUI.GraphDialog import GraphDialog
from GestioneSistema.Sistema import Sistema
from GestioneStatistiche.Statistiche import Statistiche


class ArchivioEsiti(QDialog):
    def __init__(self):
        super(ArchivioEsiti, self).__init__()
        loadUi("archivioesiti.ui", self)
        self.homeBtn.clicked.connect(self.returnHome)
        self.graficiesitiCombo.activated.connect(self.FiltraStatistiche)
        self.popolaEsiti()
        self.Ricercaappuntamentobtn.clicked.connect(self.ricercaEsiti)


    def returnHome(self):
        from GUI.FunzionalitaScreen import FunzionalitaScreen
        self.funzionalita = FunzionalitaScreen()
        self.close()
        self.funzionalita.show()

    def FiltraStatistiche(self):
        if self.graficiesitiCombo.currentText() == "Esiti":
            self.st = Statistiche()
            self.st.plotPieEsiti()

    def popolaEsiti(self):
        Sistema.downloadEsiti()
        row = 0
        self.EsitiTable.setRowCount(len(Sistema.listaEsiti))
        for appuntamento in Sistema.listaEsiti:
                self.EsitiTable.setItem(row, 0, QTableWidgetItem(str(appuntamento.get_idapp())))  # nella colonna id appuntamneto metto l'id dell'appuntamento i esimo
                self.EsitiTable.setItem(row, 1, QTableWidgetItem( appuntamento.get_cff()))  # nella colonna cf metto il cf dell'appuntamento i esimo
                self.EsitiTable.setItem(row, 2, QTableWidgetItem(appuntamento.get_data().strftime("%y-%m-%d")))
                self.EsitiTable.setItem(row, 3, QTableWidgetItem("Concluso"))
                if appuntamento.get_tampone().get_esito() == False:
                    self.EsitiTable.setItem(row, 4, QTableWidgetItem("NEGATIVO"))
                else:
                    self.EsitiTable.setItem(row, 4, QTableWidgetItem("POSITIVO"))
                row = row + 1



    def ricercaEsiti(self):
        param = self.ricercaappuntamento.text()
        esitiRicercati = []
        if (param == ""):
            self.popolaEsiti()
            return
        for element in Sistema.listaEsiti:
            if (param in element.cliente.cf or param in str(element.get_data())):
                esitiRicercati.append(element)
        self.popolaRicercaEsiti(esitiRicercati)

    def popolaRicercaEsiti(self, esitiRicercati):
        roww = 0
        self.EsitiTable.setRowCount(len(esitiRicercati))
        for appuntamento in esitiRicercati:
            self.EsitiTable.setItem(roww, 0, QTableWidgetItem(str(appuntamento.get_idapp())))  # nella colonna id appuntamneto metto l'id dell'appuntamento i esimo
            self.EsitiTable.setItem(roww, 1, QTableWidgetItem(
                appuntamento.get_cff()))  # nella colonna cf metto il cf dell'appuntamento i esimo
            self.EsitiTable.setItem(roww, 2, QTableWidgetItem(appuntamento.get_data().strftime("%y-%m-%d")))
            self.EsitiTable.setItem(roww, 3, QTableWidgetItem("Concluso"))
            if appuntamento.get_tampone().get_esito() == False:
                self.EsitiTable.setItem(roww, 4, QTableWidgetItem("NEGATIVO"))
            else:
                self.EsitiTable.setItem(roww, 4, QTableWidgetItem("POSITIVO"))
            roww = roww + 1
