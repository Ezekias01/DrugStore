from random import randint

from PyQt5.uic import *
from PyQt5.QtWidgets import *
from GUI.FormAppuntamento import FormAppuntamento
from GestioneCassa.Vendita import Vendita
from GestioneMagazzino.Farmaco import Farmaco
from GestioneSistema.Sistema import *
import datetime


from GestioneTamponi.ClassiTamponi import Tampone, Cliente, Appuntamento


class CassaScreen(QDialog):
    prodSelezionati = []
    totale = []

    def __init__(self):
        super(CassaScreen, self).__init__()
        loadUi("cassascreen.ui", self)
        self.prodSelezionati.clear()
        self.totale.clear()
        self.popolaListaVendita()
        self.Ricercaprodottobtn.clicked.connect(self.ricercaArticolo)
        self.mettinelcarrelloBtn.clicked.connect(self.scegliProdotto)
        self.acquistaBtn.clicked.connect(self.chiudiVendita)
        self.eliminaprodcarrellobtn.clicked.connect(self.eliminaProdottoSelezionatoCarrello)
        self.homeBtn.clicked.connect(self.returnHome)


    def returnHome(self):
        from GUI.FunzionalitaScreen import FunzionalitaScreen
        self.funzionalita = FunzionalitaScreen()
        self.close()
        self.funzionalita.show()

    def popolaListaVendita(self):
        Sistema.downloadArticoli()
        row = 0
        self.VenditaTable.setRowCount(
            len(Sistema.magazzino))  # setto la quangtità di righe della table come uguale alla lunghezza della lista di appuntamenti
        for articolo in Sistema.magazzino:
            self.VenditaTable.setItem(row, 0, QTableWidgetItem(str(articolo.get_idarticolo())))
            self.VenditaTable.setItem(row, 1, QTableWidgetItem(
                articolo.get_tipo_articolo()))  # nella colonna cf metto il cf dell'appuntamento i esimo
            self.VenditaTable.setItem(row, 2, QTableWidgetItem(articolo.get_nome()))
            self.VenditaTable.setItem(row, 3, QTableWidgetItem(str(articolo.get_prezzo())))
            if articolo.get_data_scadenza() is None:
                self.VenditaTable.setItem(row, 4, QTableWidgetItem("Assente"))
            else:
                self.VenditaTable.setItem(row, 4, QTableWidgetItem(articolo.get_data_scadenza().strftime("%y-%m-%d")))
            self.VenditaTable.setItem(row, 5, QTableWidgetItem(articolo.get_dosaggio()))
            if isinstance(articolo, Farmaco):
                self.VenditaTable.setItem(row, 7, QTableWidgetItem(articolo.get_minsan()))
                if articolo.get_flagRicetta() == True:
                    self.VenditaTable.setItem(row, 6, QTableWidgetItem("RICETTA"))
                else:
                    self.VenditaTable.setItem(row, 6, QTableWidgetItem("NO RICETTA"))
            else:
                self.VenditaTable.setItem(row, 6, QTableWidgetItem("Assente"))
                self.VenditaTable.setItem(row, 7, QTableWidgetItem("Assente"))
            self.VenditaTable.setItem(row, 8, QTableWidgetItem(str(articolo.get_quantita())))
            row = row + 1

    def ricercaArticolo(self):
        Sistema.downloadArticoli()
        param = self.ricercaprodottoLE.text()
        if (param == ""):
            self.popolaListaVendita()
            return
        else:
            prodottiRicercati = []
            for element in Sistema.magazzino:
                if param in element.get_nome() or param in str(element.get_idarticolo()):
                    prodottiRicercati.append(element)
        self.popolaRicerca(prodottiRicercati)

    def popolaRicerca(self, prodRicercati):
        row = 0
        self.VenditaTable.setRowCount(
            len(prodRicercati))  # setto la quangtità di righe della table come uguale alla lunghezza della lista di appuntamenti
        for articolo in prodRicercati:
            self.VenditaTable.setItem(row, 0, QTableWidgetItem(str(articolo.get_idarticolo())))
            self.VenditaTable.setItem(row, 1, QTableWidgetItem(
                articolo.get_tipo_articolo()))  # nella colonna cf metto il cf dell'appuntamento i esimo
            self.VenditaTable.setItem(row, 2, QTableWidgetItem(articolo.get_nome()))
            self.VenditaTable.setItem(row, 3, QTableWidgetItem(str(articolo.get_prezzo())))
            if articolo.get_data_scadenza() is None:
                self.VenditaTable.setItem(row, 4, QTableWidgetItem("Assente"))
            else:
                self.VenditaTable.setItem(row, 4, QTableWidgetItem(articolo.get_data_scadenza().strftime("%y-%m-%d")))
            self.VenditaTable.setItem(row, 5, QTableWidgetItem(articolo.get_dosaggio()))
            if isinstance(articolo, Farmaco):
                self.VenditaTable.setItem(row, 7, QTableWidgetItem(articolo.get_minsan()))
                if articolo.get_flagRicetta() == True:
                    self.VenditaTable.setItem(row, 6, QTableWidgetItem("RICETTA"))
                else:
                    self.VenditaTable.setItem(row, 6, QTableWidgetItem("NO RICETTA"))
            else:
                self.VenditaTable.setItem(row, 6, QTableWidgetItem("Assente"))
                self.VenditaTable.setItem(row, 7, QTableWidgetItem("Assente"))
            self.VenditaTable.setItem(row, 8, QTableWidgetItem(str(articolo.get_quantita())))
            row = row + 1

    def scegliProdotto(self):

        if self.spinquantitaBox.value() == 0:
            QMessageBox.about(self, "Error", "La quantità non può essere nulla.")
            return

        itemcod = self.VenditaTable.item(self.VenditaTable.currentRow(), 0)
        if itemcod is not None:

            for a in Sistema.magazzino:
                codselezionato = self.VenditaTable.item(self.VenditaTable.currentRow(), 0).text()

                if int(codselezionato) == a.get_idarticolo():
                    nProdSelezionati = len(self.prodSelezionati)
                    self.prodSelezionati.append(a)
                    if self.spinquantitaBox.value() <= self.prodSelezionati[nProdSelezionati].get_quantita():
                        self.prodSelezionati[nProdSelezionati].set_numero(self.spinquantitaBox.value())
                        print(self.prodSelezionati[nProdSelezionati].get_numero())
                        for x in range(nProdSelezionati):

                            if int(codselezionato) == self.prodSelezionati[x].get_idarticolo():
                                elemrimosso = self.prodSelezionati[x]
                                self.prodSelezionati.pop()
                                QMessageBox.about(self, "Imprevisto",
                                                  "L'articolo è già stato selezionato in precedenza, è stato eliminato dal carrello"
                                                  " a favore dell'inserimento del prodotto appena selezionato")
                                nProdSelezionati -= 1
                                self.modificaCarrello(x, elemrimosso)
                                return


                        self.riempiCarrello(nProdSelezionati)
                        return
                    else:
                        self.prodSelezionati.remove(a)
                        QMessageBox.about(self, "Errore", "La quantità inserita è maggiore della giacenza dell'articolo")
                        return
        else:
            QMessageBox.about(self, "Errore", "Seleziona elemento")
            return

    def riempiCarrello(self, nProdSelezionati):
        self.CarrelloTable.setRowCount(len(self.prodSelezionati))  # setto la quangtità di righe della table come uguale alla lunghezza della lista di appuntamenti
        self.CarrelloTable.setItem(nProdSelezionati, 0, QTableWidgetItem(self.prodSelezionati[nProdSelezionati].get_nome()))
        self.CarrelloTable.setItem(nProdSelezionati, 1, QTableWidgetItem(str(self.prodSelezionati[nProdSelezionati].get_prezzo())))  # nella colonna cf metto il cf dell'appuntamento i esimo
        self.CarrelloTable.setItem(nProdSelezionati, 2, QTableWidgetItem(self.prodSelezionati[nProdSelezionati].get_tipo_articolo()))
        if self.prodSelezionati[nProdSelezionati].get_data_scadenza() is None:
            self.CarrelloTable.setItem(nProdSelezionati, 3, QTableWidgetItem("Assente"))
        else:
            self.CarrelloTable.setItem(nProdSelezionati, 3, QTableWidgetItem(self.prodSelezionati[nProdSelezionati].get_data_scadenza().strftime("%y-%m-%d")))
        self.CarrelloTable.setItem(nProdSelezionati, 4, QTableWidgetItem(str(self.prodSelezionati[nProdSelezionati].get_idarticolo())))
        self.CarrelloTable.setItem(nProdSelezionati, 8, QTableWidgetItem(self.prodSelezionati[nProdSelezionati].get_dosaggio()))
        if isinstance(self.prodSelezionati[nProdSelezionati], Farmaco):
            self.CarrelloTable.setItem(nProdSelezionati, 7, QTableWidgetItem(self.prodSelezionati[nProdSelezionati].get_minsan()))
            if self.prodSelezionati[nProdSelezionati].get_flagRicetta() == True:
                self.CarrelloTable.setItem(nProdSelezionati, 6, QTableWidgetItem("RICETTA"))
            else:
                self.CarrelloTable.setItem(nProdSelezionati, 6, QTableWidgetItem("NO RICETTA"))
        else:
            self.CarrelloTable.setItem(nProdSelezionati, 6, QTableWidgetItem("Assente"))
            self.CarrelloTable.setItem(nProdSelezionati, 7, QTableWidgetItem("Assente"))
        self.CarrelloTable.setItem(nProdSelezionati, 5, QTableWidgetItem(str(self.spinquantitaBox.value())))
        self.totale.append(self.prodSelezionati[nProdSelezionati].get_prezzo() * self.spinquantitaBox.value())

    def modificaCarrello(self, riga, elemrimosso):
        self.CarrelloTable.setItem(riga, 0, QTableWidgetItem(elemrimosso.get_nome()))
        self.CarrelloTable.setItem(riga, 1, QTableWidgetItem(
            str(elemrimosso.get_prezzo())))  # nella colonna cf metto il cf dell'appuntamento i esimo
        self.CarrelloTable.setItem(riga, 2, QTableWidgetItem(elemrimosso.get_tipo_articolo()))
        if elemrimosso.get_data_scadenza() is None:
            self.CarrelloTable.setItem(riga, 3, QTableWidgetItem("Assente"))
        else:
            self.CarrelloTable.setItem(riga, 3, QTableWidgetItem(elemrimosso.get_data_scadenza().strftime("%y-%m-%d")))
        self.CarrelloTable.setItem(riga, 4, QTableWidgetItem(str(elemrimosso.get_idarticolo())))
        self.CarrelloTable.setItem(riga, 8, QTableWidgetItem(elemrimosso.get_dosaggio()))
        if isinstance(elemrimosso, Farmaco):
            self.CarrelloTable.setItem(riga, 7, QTableWidgetItem(elemrimosso.get_minsan()))
            if elemrimosso.get_flagRicetta() == True:
                self.CarrelloTable.setItem(riga, 6, QTableWidgetItem("RICETTA"))
            else:
                self.CarrelloTable.setItem(riga, 6, QTableWidgetItem("NO RICETTA"))
        else:
            self.CarrelloTable.setItem(riga, 6, QTableWidgetItem("Assente"))
            self.CarrelloTable.setItem(riga, 7, QTableWidgetItem("Assente"))
        self.CarrelloTable.setItem(riga, 5, QTableWidgetItem(str(self.spinquantitaBox.value())))
        self.totale[riga] = elemrimosso.get_prezzo()*self.spinquantitaBox.value()

    def chiudiVendita(self):
        if not self.prodSelezionati:
            QMessageBox.about(self, "Error", "Inserisci almeno un prodotto nel carrello.")
            return

        Sistema.downloadArticoli()
        for prodotto in self.prodSelezionati:
            for articolo in Sistema.magazzino:
                if (prodotto.get_idarticolo() == articolo.get_idarticolo()):
                    if (prodotto.get_numero() == articolo.get_quantita()):
                        Sistema.magazzino.remove(articolo)
                    else:
                        giacenza = articolo.get_quantita()
                        quantita = prodotto.get_numero()
                        giacenza -= quantita
                        print(giacenza)
                        articolo.set_quantita(giacenza)


        totcassa = str(sum(self.totale))
        QMessageBox.about(self, "Error", f"Spesa totale: Il totale è {totcassa[0:5]} €")
        self.returnHome()
        self.updateArchivio(totcassa)
        Sistema.uploadArticoli()
        Sistema.downloadArticoli()
        self.popolaListaVendita()

    def updateArchivio(self, tmp):
        Sistema.downloadArchivioVendite()
        if not(self.generaCodice() == 0):
            today = datetime.date.today()
            vendita = Vendita(self.generaCodice(), tmp, today)
            Sistema.archivioVendite.append(vendita)
            Sistema.uploadArchivioVendite()
        else:
            self.updateArchivio()

    def generaCodice(self):
        codice = randint(1,1000000)
        for prod in Sistema.archivioVendite:
            if codice == prod.get_codicevendita():
                return 0
        return codice

    def eliminaProdottoSelezionatoCarrello(self):
        itemcodfield = self.CarrelloTable.item(self.CarrelloTable.currentRow(), 4)
        if itemcodfield is not None:
            codselezionato = self.CarrelloTable.item(self.CarrelloTable.currentRow(), 4).text()
            nProdSelezionati = len(self.prodSelezionati)
            for x in self.prodSelezionati:
                if int(codselezionato) == x.get_idarticolo():
                    QMessageBox.about(self, "Avviso", f"Eliminato elemento con codice {x.get_idarticolo()} dal carrello.")
                    index = self.prodSelezionati.index(x)
                    self.prodSelezionati.pop(index)
                    nProdSelezionati -= 1
                    temp = nProdSelezionati - 1
                    if self.prodSelezionati:
                        self.riempiCarrello(temp)
                    else:
                        self.CarrelloTable.setRowCount(0)
                    return

        else:
            QMessageBox.about(self, "Error", "Seleziona un elemento da eliminare nel carrello.")
            return



