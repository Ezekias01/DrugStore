from PyQt5.uic import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import datetime

from GestioneSistema.Sistema import Sistema
from GestioneTamponi.ClassiTamponi import Tampone, Appuntamento, Cliente


#from GUI.CalendarioScreen import *


class FormAppuntamento(QDialog):

    def __init__(self):
        super(FormAppuntamento, self).__init__()
        loadUi("formAppuntamento.ui", self)
        self.setupCombo()
        self.annoCombo.addItems(self.years)
        self.tamponeCombo.addItems(self.tamponetipo)
        self.meseCombo.activated.connect(self.popolaCombo)
        self.inviaformBtn.clicked.connect(self.aggiungiAppuntamento)
        self.backBtn.clicked.connect(self.backtoCalendario)

    def backtoCalendario(self):
        self.svutaForm()
        self.close()

    def aggiungiAppuntamento(self):
        if self.nomeLe.text() != '' and self.cognomeLe.text() != '' and self.cfLe.text() != '' and self.giornoCombo.currentText() != '' and self.tamponeCombo.currentText() != '':
            txt = self.cfLe.text()
            if txt.isalpha() and len(txt)==6:
                a = int(self.annoCombo.currentText())
                m = int(self.meseCombo.currentText())
                g = int(self.giornoCombo.currentText())
                data = datetime.datetime(a, m, g)
                if data >= Sistema.today:
                    Sistema.downloadAppuntamenti()
                    nome = self.nomeLe.text()
                    cognome = self.cognomeLe.text()
                    cf = self.cfLe.text()
                    cf.upper()
                    tipo = self.tamponeCombo.currentText()
                    tampone = Tampone(tipo)
                    cliente = Cliente(nome, cognome, cf)
                    newid = Sistema.listaAppuntamenti[len(Sistema.listaAppuntamenti)-1].get_idapp()+1
                    appuntamento = Appuntamento(cliente, tampone, data)
                    appuntamento.set_idapp(newid)
                    Sistema.listaAppuntamenti.append(appuntamento)
                    Sistema.uploadAppuntamenti()
                    QMessageBox.about(self, "Avviso", "Appuntamento aggiunto!")
                    self.svutaForm()
                    self.close()
                else:
                    QMessageBox.about(self, "Error", "La data inserita deve essere uguale o successiva a quella odierna")
            else:
                QMessageBox.about(self, "Error", "Nel campo codice fiscale inserire solo caratteri senza spazi. La lunghezza deve essere 6 caratteri.")
        else:
            QMessageBox.about(self, "Error", "Riempi tutti i campi")

    def svutaForm(self):
        self.nomeLe.clear()
        self.cognomeLe.clear()
        self.cfLe.clear()
        self.giornoCombo.clear()
        #self.tamponeCombo.clear()

    def setupCombo(self):
        self.tamponetipo = ['', "Molecolare", "Rapido"]
        year = Sistema.today.year
        self.giorni = []
        self.years = [str(year), str(year + 1)]
        for i in range(1, 32, 1):
            self.giorni.append(str(i))

    def popolaCombo(self):
        self.giornoCombo.clear()
        temp = []
        if self.meseCombo.currentText() == "01":
           for i in range(0, 31, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "02":
           for i in range(0, 27, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "03":
           for i in range(0, 31, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "04":
           for i in range(0, 30, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "05":
           for i in range(0, 31, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "06":
           for i in range(0, 30, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "07":
           for i in range(0, 31, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "08":
           for i in range(0, 31, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "09":
           for i in range(0, 30, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "10":
           for i in range(0, 31, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "11":
           for i in range(0, 30, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "12":
           for i in range(0, 31, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)




