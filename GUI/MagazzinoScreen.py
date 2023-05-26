from PyQt5.uic import *
from PyQt5.QtWidgets import *

from GUI.FornitoriMenu import FornitoriMenu
from GUI.ScadenziarioScreen import ScadenziarioScreen
from GestioneMagazzino.Farmaco import Farmaco
from GestioneMagazzino.Articolo import Articolo
from GestioneSistema.Sistema import *
import datetime




class MagazzinoScreen(QDialog):
    def __init__(self):
        super(MagazzinoScreen, self).__init__()
        loadUi("magazzinoscreen.ui", self)
        self.filtra = ['Tutti', "Farmaco", "Non Farmaco"]
        self.popolaMagazzino()
        self.filtramagazzCombo.addItems(self.filtra)
        self.filtramagazzCombo.activated.connect(self.filtraArticoli)
        self.nuovoordbtn.clicked.connect(self.gotoMenuFornitori)
        self.scadenziariobtn.clicked.connect(self.gotoScadenziario)
        self.homeBtn.clicked.connect(self.returnHome)



    def returnHome(self):
        from GUI.FunzionalitaScreen import FunzionalitaScreen
        self.funzionalita = FunzionalitaScreen()
        self.close()
        self.funzionalita.show()

    def popolaMagazzino(self):
        Sistema.downloadArticoli()
        row = 0
        self.MagazzinoTable.setRowCount(len(Sistema.magazzino))
        for articolo in Sistema.magazzino:
                self.MagazzinoTable.setItem(row, 0, QTableWidgetItem(str(articolo.get_idarticolo())))
                self.MagazzinoTable.setItem(row, 1, QTableWidgetItem(articolo.get_tipo_articolo()))
                self.MagazzinoTable.setItem(row, 2, QTableWidgetItem(articolo.get_nome()))
                self.MagazzinoTable.setItem(row, 3, QTableWidgetItem(str(articolo.get_prezzo())))
                if articolo.get_data_scadenza() is None:
                  self.MagazzinoTable.setItem(row, 4, QTableWidgetItem("Assente"))
                else:
                  self.MagazzinoTable.setItem(row, 4, QTableWidgetItem(articolo.get_data_scadenza().strftime("%y-%m-%d")))
                self.MagazzinoTable.setItem(row, 5, QTableWidgetItem(articolo.get_dosaggio()))
                if isinstance(articolo,Farmaco):
                    self.MagazzinoTable.setItem(row, 7, QTableWidgetItem(articolo.get_minsan()))
                    if articolo.get_flagRicetta() == True:
                        self.MagazzinoTable.setItem(row, 6, QTableWidgetItem("RICETTA"))
                    else:
                        self.MagazzinoTable.setItem(row, 6, QTableWidgetItem("NO RICETTA"))
                else:
                    self.MagazzinoTable.setItem(row, 6, QTableWidgetItem("Assente"))
                    self.MagazzinoTable.setItem(row, 7, QTableWidgetItem("Assente"))
                self.MagazzinoTable.setItem(row, 8, QTableWidgetItem(str(articolo.get_quantita())))
                row = row+1

    def filtraArticoli(self):
        if self.filtramagazzCombo.currentText() == "Farmaco":
            self.visualizzaFarmaci()
        elif self.filtramagazzCombo.currentText() == "Non Farmaco":
            self.visualizzaNonFarmaci()
        elif self.filtramagazzCombo.currentText() == 'Tutti':
            self.popolaMagazzino()

    def visualizzaFarmaci(self):
        self.MagazzinoTable.setRowCount(0)
        Sistema.downloadArticoli()
        cont = 0
        for articolo in Sistema.magazzino:
            if articolo.get_tipo_articolo() == "Farmaco":
                cont += 1
        prodfar = cont
        row = 0
        self.MagazzinoTable.setRowCount(prodfar)
        for articolo in Sistema.magazzino:
            if articolo.get_tipo_articolo() == "Farmaco":
                self.MagazzinoTable.setItem(row, 0, QTableWidgetItem(str(articolo.get_idarticolo())))
                self.MagazzinoTable.setItem(row, 1, QTableWidgetItem(articolo.get_tipo_articolo()))  # nella colonna cf metto il cf dell'appuntamento i esimo
                self.MagazzinoTable.setItem(row, 2, QTableWidgetItem(articolo.get_nome()))
                self.MagazzinoTable.setItem(row, 3, QTableWidgetItem(str(articolo.get_prezzo())))
                if articolo.get_data_scadenza() is None:
                    self.MagazzinoTable.setItem(row, 4, QTableWidgetItem("Assente"))
                else:
                    self.MagazzinoTable.setItem(row, 4, QTableWidgetItem(articolo.get_data_scadenza().strftime("%y-%m-%d")))
                self.MagazzinoTable.setItem(row, 5, QTableWidgetItem(articolo.get_dosaggio()))
                if articolo.get_flagRicetta() == True:
                    self.MagazzinoTable.setItem(row, 6, QTableWidgetItem("RICETTA"))
                else:
                    self.MagazzinoTable.setItem(row, 6, QTableWidgetItem("NO RICETTA"))
                self.MagazzinoTable.setItem(row, 7, QTableWidgetItem(articolo.get_minsan()))
                self.MagazzinoTable.setItem(row, 8, QTableWidgetItem(str(articolo.get_quantita())))
                row = row+1

    def visualizzaNonFarmaci(self):
        self.MagazzinoTable.setRowCount(0)
        Sistema.downloadArticoli()
        cont=0
        for articolo in Sistema.magazzino:
            if articolo.get_tipo_articolo() == "Non Farmaco":
                cont += 1
        prodnonfar = cont
        row = 0
        self.MagazzinoTable.setRowCount(prodnonfar)
        for articolo in Sistema.magazzino:
            if articolo.get_tipo_articolo() == "Non Farmaco":
                self.MagazzinoTable.setItem(row, 0, QTableWidgetItem(str(articolo.get_idarticolo())))
                self.MagazzinoTable.setItem(row, 1, QTableWidgetItem(
                    articolo.get_tipo_articolo()))  # nella colonna cf metto il cf dell'appuntamento i esimo
                self.MagazzinoTable.setItem(row, 2, QTableWidgetItem(articolo.get_nome()))
                self.MagazzinoTable.setItem(row, 3, QTableWidgetItem(str(articolo.get_prezzo())))
                if articolo.get_data_scadenza() is None:
                    self.MagazzinoTable.setItem(row, 4, QTableWidgetItem("Assente"))
                else:
                    self.MagazzinoTable.setItem(row, 4, QTableWidgetItem(articolo.get_data_scadenza().strftime("%y-%m-%d")))
                self.MagazzinoTable.setItem(row, 5, QTableWidgetItem(articolo.get_dosaggio()))
                self.MagazzinoTable.setItem(row, 6, QTableWidgetItem("Assente"))
                self.MagazzinoTable.setItem(row, 7, QTableWidgetItem("Assente"))
                self.MagazzinoTable.setItem(row, 8, QTableWidgetItem(str(articolo.get_quantita())))
                row = row + 1

    def gotoMenuFornitori(self):
        self.menuf = FornitoriMenu()
        self.close()
        self.menuf.show()

    def gotoScadenziario(self):
        self.scadenziario = ScadenziarioScreen()
        self.close()
        self.scadenziario.show()
