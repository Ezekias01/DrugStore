import matplotlib.pyplot as plt
from GUI.GraphDialog import GraphDialog
from GestioneSistema.Sistema import Sistema

class Statistiche():

    def __init__(self):
        pass


    def plotPieEsiti(self):
        Sistema.downloadEsiti()
        cp = 0
        cn = 0
        for esiti in Sistema.listaEsiti:
            if esiti.get_tampone().get_esito() == True:
                cp += 1
            else:
                cn += 1

        labels = 'Positivi', 'Negativi'
        sizes = [cp, cn]
        figure, ax = plt.subplots(figsize=(6, 6), dpi=200)
        plt.subplots_adjust(hspace=0)
        ax.pie(sizes, labels=labels,  autopct='%1.1f%%')
        plt.savefig("img/esitiplot.png")
        self.g = GraphDialog()
        self.g.setGraph("img/esitiplot.png")

    def plotPieScadenze(self):
        Sistema.downloadArticoli()
        primofiltroscad = Sistema.today.year + 3
        secondofiltroscad = Sistema.today.year + 4
        terzoofiltroscad = Sistema.today.year + 5
        contprimofiltro = 0
        contsecondofiltro = 0
        contterzofiltro = 0
        for articolo in Sistema.magazzino:
            if articolo.get_data_scadenza() is not None:
                annoscadenza = articolo.get_data_scadenza().year
                if annoscadenza == primofiltroscad:
                    contprimofiltro += 1
                elif annoscadenza == secondofiltroscad:
                    contsecondofiltro += 1
                elif annoscadenza == terzoofiltroscad:
                    contterzofiltro += 1

        labels = 'Scadenza '+str(Sistema.today.year + 3), 'Scadenza' +str(Sistema.today.year + 4), 'Scadenza '+str(Sistema.today.year + 5)
        sizes = [contprimofiltro, contsecondofiltro, contterzofiltro]
        figure, ax = plt.subplots(figsize=(6, 6), dpi=200)
        plt.subplots_adjust(hspace=0)
        ax.pie(sizes, labels=labels,  autopct='%1.1f%%')
        plt.savefig("img/scadenzeplot.png")
        self.g = GraphDialog()
        self.g.setGraph("img/scadenzeplot.png")
