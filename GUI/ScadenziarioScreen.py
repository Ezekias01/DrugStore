from PyQt5.uic import *
from PyQt5.QtWidgets import *

from GUI.FornitoriMenu import FornitoriMenu
from GestioneMagazzino.Farmaco import Farmaco
from GestioneMagazzino.Articolo import Articolo
from GestioneSistema.Sistema import *
import datetime

from GestioneStatistiche.Statistiche import Statistiche


class ScadenziarioScreen(QDialog):
    def __init__(self):
        super(ScadenziarioScreen, self).__init__()
        loadUi("scadenziarioscreen.ui", self)
        self.filtra = [str(Sistema.today.year+3), str(Sistema.today.year+4), str(Sistema.today.year+5)]
        self.popolaScadenziario(Sistema.today.year+3)
        self.filtrascadenzCombo.addItems(self.filtra)
        self.filtrascadenzCombo.activated.connect(self.filtraScadenziario)
        self.plotScadenzeBtn.clicked.connect(self.showStatisticheScadenze)
        self.homeBtn.clicked.connect(self.returnHome)

    def returnHome(self):
        from GUI.FunzionalitaScreen import FunzionalitaScreen
        self.funzionalita = FunzionalitaScreen()
        self.close()
        self.funzionalita.show()

    def showStatisticheScadenze(self):
        self.stat = Statistiche()
        self.stat.plotPieScadenze()

    def popolaScadenziario(self, datafiltro):
        Sistema.downloadArticoli()
        row = 0
        self.ScadenziarioTable.setRowCount(len(Sistema.magazzino))
        flag = False

        for articolo in Sistema.magazzino:
            if articolo.get_data_scadenza() is not None:
                annoscadenza = articolo.get_data_scadenza().year
                if annoscadenza == datafiltro:
                    self.ScadenziarioTable.setItem(row, 0, QTableWidgetItem(str(articolo.get_idarticolo())))
                    self.ScadenziarioTable.setItem(row, 1, QTableWidgetItem(articolo.get_tipo_articolo()))
                    self.ScadenziarioTable.setItem(row, 2, QTableWidgetItem(articolo.get_nome()))
                    self.ScadenziarioTable.setItem(row, 3, QTableWidgetItem(str(articolo.get_prezzo())))
                    self.ScadenziarioTable.setItem(row, 4, QTableWidgetItem(articolo.get_data_scadenza().strftime("%y-%m-%d")))
                    self.ScadenziarioTable.setItem(row, 5, QTableWidgetItem(articolo.get_dosaggio()))
                    if isinstance(articolo, Farmaco):
                        self.ScadenziarioTable.setItem(row, 7, QTableWidgetItem(articolo.get_minsan()))
                        if articolo.get_flagRicetta() == True:
                            self.ScadenziarioTable.setItem(row, 6, QTableWidgetItem("RICETTA"))
                        else:
                            self.ScadenziarioTable.setItem(row, 6, QTableWidgetItem("NO RICETTA"))
                    else:
                        self.ScadenziarioTable.setItem(row, 6, QTableWidgetItem("Assente"))
                        self.ScadenziarioTable.setItem(row, 7, QTableWidgetItem("Assente"))
                    self.ScadenziarioTable.setItem(row, 8, QTableWidgetItem(str(articolo.get_quantita())))
                    row = row + 1
                    flag = True

        if flag == False:
            QMessageBox(self,"Avviso",f"Non ci sono prodotti che scadono nel {datafiltro}")
            return

    def filtraScadenziario(self):
        if self.filtrascadenzCombo.currentText() == str(Sistema.today.year+3):
            self.ScadenziarioTable.setRowCount(0)
            self.popolaScadenziario(Sistema.today.year+3)
        elif self.filtrascadenzCombo.currentText() == str(Sistema.today.year+4):
            self.ScadenziarioTable.setRowCount(0)
            self.popolaScadenziario(Sistema.today.year+4)
        elif self.filtrascadenzCombo.currentText() == str(Sistema.today.year+5):
            self.ScadenziarioTable.setRowCount(0)
            self.popolaScadenziario(Sistema.today.year+5)