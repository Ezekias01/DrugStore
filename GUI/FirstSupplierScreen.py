from datetime import datetime
from random import randint

from IPython.external.qt_for_kernel import QtGui, QtCore
from PyQt5.uic import *
from PyQt5.QtWidgets import *

from GUI.ArchivioClienti import ArchivioClienti
from GUI.ArchivioEsiti import ArchivioEsiti
from GUI.ArchivioVendite import ArchivioVendite
from GUI.CalendarioScreen import CalendarioScreen
from GestioneMagazzino.Farmaco import Farmaco
from GestioneMagazzino.Ordine import Ordine
from GestioneSistema.Sistema import Sistema


class FirstSupplierScreen(QDialog):
    prodSelezionati = []
    totale = []

    def __init__(self):
        super(FirstSupplierScreen, self).__init__()
        loadUi("menuprimofornitore.ui", self)
        self.prodSelezionati.clear()
        self.totale.clear()
        self.popolaListaVenditaPrimoFornitore()
        self.mettinelcarrelloBtn.clicked.connect(self.scegliProdotto)
        self.Ricercaprodottobtn.clicked.connect(self.ricercaArticolo)
        self.acquistaBtn.clicked.connect(self.chiudiOrdine)
        self.eliminaprodcarrellobtn.clicked.connect(self.eliminaProdottoSelezionatoCarrello)
        self.homeBtn.clicked.connect(self.returnHome)

    def returnHome(self):
        from GUI.FunzionalitaScreen import FunzionalitaScreen
        self.funzionalita = FunzionalitaScreen()
        self.close()
        self.funzionalita.show()

    def popolaListaVenditaPrimoFornitore(self):
        Sistema.downloadCatalogoFornitore()
        row = 0
        self.VenditaTable.setRowCount(len(Sistema.catalogoFornitore))  # setto la quangtità di righe della table come uguale alla lunghezza della lista di appuntamenti
        for articolo in Sistema.catalogoFornitore:
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
        Sistema.downloadCatalogoFornitore()
        param = self.ricercaprodottoLE.text()
        if (param == ""):
            self.popolaListaVenditaPrimoFornitore()
            return
        else:
            prodottiRicercati = []
            for element in Sistema.catalogoFornitore:
                if param in element.get_nome() or param in str(element.get_idarticolo()):
                    prodottiRicercati.append(element)
        self.popolaRicerca(prodottiRicercati)

    def popolaRicerca(self, prodRicercati):
        row = 0
        self.VenditaTable.setRowCount(len(prodRicercati))  # setto la quangtità di righe della table come uguale alla lunghezza della lista di appuntamenti
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

            for a in Sistema.catalogoFornitore:
                codselezionato = self.VenditaTable.item(self.VenditaTable.currentRow(), 0).text()

                if int(codselezionato) == a.get_idarticolo():
                    nProdSelezionati = len(self.prodSelezionati)
                    self.prodSelezionati.append(a)
                    if self.spinquantitaBox.value() <= self.prodSelezionati[nProdSelezionati].get_quantita():
                        self.prodSelezionati[nProdSelezionati].set_numero(self.spinquantitaBox.value())
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
                        QMessageBox.about(self, "Errore",
                                          "La quantità inserita è maggiore della giacenza dell'articolo")
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

    def chiudiOrdine(self):
        if not self.prodSelezionati:
            QMessageBox.about(self, "Error", "Inserisci almeno un prodotto nel carrello.")
            return
        giapresente = False
        Sistema.downloadArticoli()
        Sistema.downloadCatalogoFornitore()
        for prodotto in self.prodSelezionati:
            for articolo in Sistema.catalogoFornitore:
                if (prodotto.get_idarticolo() == articolo.get_idarticolo()):
                    if (prodotto.get_numero() == articolo.get_quantita()):
                        Sistema.catalogoFornitore.remove(articolo)
                    else:
                        giacenza = articolo.get_quantita()
                        quantita = prodotto.get_numero()
                        giacenza -= quantita
                        articolo.set_quantita(giacenza)

                    for prodottoMag in Sistema.magazzino:
                        if (prodotto.get_idarticolo() == prodottoMag.get_idarticolo()):
                            giacenza = prodottoMag.get_quantita()
                            quantita = prodotto.get_numero()
                            giacenza += quantita
                            prodottoMag.set_quantita(giacenza)
                            giapresente = True

                    if not(giapresente):
                            Sistema.magazzino.append(prodotto)
                            nuovagia = prodotto.get_numero()
                            Sistema.magazzino[len(Sistema.magazzino) - 1].set_quantita(nuovagia)



        totcassa = str(sum(self.totale))
        QMessageBox.about(self, "Error", f"Spesa totale: Il totale è {totcassa[0:5]} €")
        self.returnHome()
        self.updateArchivio(totcassa)
        Sistema.uploadArticoli()
        Sistema.uploadCatalogoFornitore()
        Sistema.downloadArticoli()
        Sistema.downloadCatalogoFornitore()
        self.popolaListaVenditaPrimoFornitore()

    def updateArchivio(self, tmp):
        import datetime
        Sistema.downloadArchivioOrdini()
        if not (self.generaCodice() == 0):
            today = datetime.date.today()
            ordine = Ordine(self.generaCodice(), "PFIZER", tmp, today)
            Sistema.archivioOrdini.append(ordine)
            Sistema.uploadArchivioOrdini()
        else:
            self.updateArchivio()

    def generaCodice(self):
        codice = randint(1, 1000000)
        for element in Sistema.archivioOrdini:
            if codice == element.get_codiceordine():
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
                    temp = nProdSelezionati-1
                    if self.prodSelezionati:
                        self.riempiCarrello(temp)
                    else:
                        self.CarrelloTable.setRowCount(0)
                    return

        else:
             QMessageBox.about(self, "Error", "Seleziona un elemento da eliminare nel carrello.")
             return