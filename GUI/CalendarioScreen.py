from PyQt5.uic import *
from PyQt5.QtWidgets import *
from GUI.FormAppuntamento import FormAppuntamento
from GestioneSistema.Sistema import *
import datetime


from GestioneTamponi.ClassiTamponi import Tampone, Cliente, Appuntamento


class CalendarioScreen(QDialog):
    def __init__(self):
        super(CalendarioScreen, self).__init__()
        loadUi("calendarioscreen.ui", self)
        self.ricerca = ['',"Non Concluso", "Concluso"]
        self.ricercaappCombo.addItems(self.ricerca)
        self.calendarWidget.selectionChanged.connect(self.popolaCalendario)   #connetto l'evento di selzione della data all'UPDATE TASK
        self.nuovoappbtn.clicked.connect(self.openFormAppuntamento)             #questi due bottoni (SalvaButton pushButton) sono delle prove, vanno cambiati
        self.ricercaappCombo.activated.connect(self.filtraAppuntamenti)
        self.chiudiappbtn.clicked.connect(self.chiudiAppuntamento)
        self.eliminaappbtn.clicked.connect(self.eliminaAppuntamento)
        self.homeBtn.clicked.connect(self.returnHome)


    def returnHome(self):
        from GUI.FunzionalitaScreen import FunzionalitaScreen
        self.funzionalita = FunzionalitaScreen()
        self.close()
        self.funzionalita.show()

    def popolaCalendario(self):
        self.AppuntamentiTable.setRowCount(0)                       #fa partire da vuota la table
        Sistema.downloadAppuntamenti()
        row = 0
        self.AppuntamentiTable.setRowCount(len(Sistema.listaAppuntamenti))           #setto la quangtità di righe della table come uguale alla lunghezza della lista di appuntamenti
        for appuntamento in Sistema.listaAppuntamenti:
             if appuntamento.get_data().strftime("%y-%m-%d") == self.getgiorno():
                self.AppuntamentiTable.setItem(row, 0, QTableWidgetItem(str(appuntamento.get_idapp()))) #nella colonna id appuntamneto metto l'id dell'appuntamento i esimo
                self.AppuntamentiTable.setItem(row, 1, QTableWidgetItem(appuntamento.get_cff()))  #nella colonna cf metto il cf dell'appuntamento i esimo
                self.AppuntamentiTable.setItem(row, 2, QTableWidgetItem(appuntamento.get_data().strftime("%y-%m-%d")))
                if appuntamento.get_stato() == False:   #in base allo stato dell'appuntamento faccuio comparire la scritta CONCLUSO o NON CONCLUSO
                  self.AppuntamentiTable.setItem(row, 3, QTableWidgetItem("Non concluso"))
                  self.AppuntamentiTable.setItem(row, 4, QTableWidgetItem("Nessun Risultato"))
                else:
                  self.AppuntamentiTable.setItem(row, 3, QTableWidgetItem("Concluso"))
                  if appuntamento.get_tampone().get_esito() == False: #in base allo stato faccio comparire la scritta POSITIVO O NEGATIVO
                      self.AppuntamentiTable.setItem(row, 4, QTableWidgetItem("NEGATIVO"))
                  else:
                      self.AppuntamentiTable.setItem(row, 4, QTableWidgetItem("POSITIVO"))
                row = row+1

    def getgiorno(self):  #prende la data selezionata sul calendario e la trasformo in una data Python convertita in stringa per usarla nei confronti
        giorno = self.calendarWidget.selectedDate().toPyDate().strftime("%y-%m-%d")
        return giorno

    def filtraAppuntamenti(self):
        if self.ricercaappCombo.currentText() == "Non Concluso":
            self.visualizzaNonConclusi()
        elif self.ricercaappCombo.currentText() == "Concluso":
            self.visualizzaConclusi()
        elif self.ricercaappCombo.currentText() == '':
            self.AppuntamentiTable.setRowCount(0)

    def visualizzaNonConclusi(self):
        self.AppuntamentiTable.setRowCount(0)
        Sistema.downloadAppuntamenti()
        row=0
        self.AppuntamentiTable.setRowCount(len(Sistema.listaAppuntamenti))
        for appuntamento in Sistema.listaAppuntamenti:
             if appuntamento.get_stato() == False:
                self.AppuntamentiTable.setItem(row, 0, QTableWidgetItem(str(appuntamento.get_idapp()))) #nella colonna id appuntamneto metto l'id dell'appuntamento i esimo
                self.AppuntamentiTable.setItem(row, 1, QTableWidgetItem(appuntamento.get_cff()))  #nella colonna cf metto il cf dell'appuntamento i esimo
                self.AppuntamentiTable.setItem(row, 2, QTableWidgetItem(appuntamento.get_data().strftime("%y-%m-%d")))
                self.AppuntamentiTable.setItem(row, 3, QTableWidgetItem("Non concluso"))
                self.AppuntamentiTable.setItem(row, 4, QTableWidgetItem("Nessun Risultato"))
                row = row+1

    def visualizzaConclusi(self):
        self.AppuntamentiTable.setRowCount(0)
        Sistema.downloadEsiti()
        row=0
        self.AppuntamentiTable.setRowCount(len(Sistema.listaEsiti))
        for appuntamento in Sistema.listaEsiti:
                self.AppuntamentiTable.setItem(row, 0, QTableWidgetItem(str(appuntamento.get_idapp()))) #nella colonna id appuntamneto metto l'id dell'appuntamento i esimo
                self.AppuntamentiTable.setItem(row, 1, QTableWidgetItem(appuntamento.get_cff()))  #nella colonna cf metto il cf dell'appuntamento i esimo
                self.AppuntamentiTable.setItem(row, 2, QTableWidgetItem(appuntamento.get_data().strftime("%y-%m-%d")))
                self.AppuntamentiTable.setItem(row, 3, QTableWidgetItem("Concluso"))
                if appuntamento.get_tampone().get_esito() == False:
                    self.AppuntamentiTable.setItem(row, 4, QTableWidgetItem("NEGATIVO"))
                else:
                    self.AppuntamentiTable.setItem(row, 4, QTableWidgetItem("POSITIVO"))
                row = row+1



    def openFormAppuntamento(self):#serviva ocn la widget list ma ora non serve
        self.form = FormAppuntamento()
        self.form.svutaForm()
        self.form.show()

    def eliminaAppuntamento(self):
        cod = self.AppuntamentiTable.item(self.AppuntamentiTable.currentRow(), 0)
        if cod is not None:
            Sistema.downloadAppuntamenti()
            co = self.AppuntamentiTable.item(self.AppuntamentiTable.currentRow(), 0).text()
            for a in Sistema.listaAppuntamenti:
                if a.get_idapp() == int(co):
                    if a.get_stato() == False:
                        index = Sistema.listaAppuntamenti.index(a)
                        Sistema.listaAppuntamenti.pop(index)
                        Sistema.uploadAppuntamenti()
                        QMessageBox.about(self, "Avviso", "Appuntamento eliminato")
                        return

                    else:
                        QMessageBox.about(self, "Avviso", "Appuntamento già concluso, non si può eliminare!")
                        return


        else:
             QMessageBox.about(self, "Error", "Seleziona una riga non vuota")


    def chiudiAppuntamento(self):
        import random
        from _datetime import datetime
        y = self.AppuntamentiTable.item(self.AppuntamentiTable.currentRow(), 0)
        if y is not None:
            d = self.AppuntamentiTable.item(self.AppuntamentiTable.currentRow(), 2).text()
            dataapp = datetime.strptime(d, '%y-%m-%d')
            if Sistema.today >= dataapp:
                Sistema.downloadAppuntamenti()
                y = self.AppuntamentiTable.item(self.AppuntamentiTable.currentRow(), 0).text()
                for a in Sistema.listaAppuntamenti:
                    if a.get_idapp() == int(y):
                        if a.get_stato() == False:
                            a.set_isconcluso()
                            if random.randint(0,1) == 1:
                                a.get_tampone().set_esito()
                                QMessageBox.about(self, "Avviso", "Tampone effettuato!")
                                Sistema.uploadAppuntamenti()
                                Sistema.listaEsiti.append(a)
                                Sistema.uploadEsiti()
                                return
                            else:
                                QMessageBox.about(self, "Avviso", "Tampone effettuato!")
                                Sistema.uploadAppuntamenti()
                                Sistema.listaEsiti.append(a)
                                Sistema.uploadEsiti()
                                return
                        else:
                            QMessageBox.about(self, "Avviso","Il tampone è già stato somministrato!")
                            return
            else:
                QMessageBox.about(self, "Avviso", "Non puoi effettuare tamponi prima del giorno dell'appuntamento!")
                return

        else:
            QMessageBox.about(self, "Error", "Seleziona una riga non vuota")

