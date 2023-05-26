import datetime
import pickle

class Sistema:

    listaAppuntamenti = []
    listaEsiti = []
    listaClienti = []
    magazzino = []
    archivioOrdini = []
    archivioVendite = []
    catalogoFornitore = []
    nVendite = 0
    nOrdini = 0
    nArticoli = 0
    today = datetime.datetime.now()

    def __init__(self):
        pass

    #
    @staticmethod
    def downloadAppuntamenti():
        f = open('appuntamenti.pickle', 'rb')
        appuntamenti = pickle.load(f)
        f.close()
        Sistema.listaAppuntamenti.clear()
        for i in range(len(appuntamenti)):
            Sistema.listaAppuntamenti.append(appuntamenti[i])

    #
    @staticmethod
    def downloadEsiti():
        Sistema.downloadAppuntamenti()
        temp = []
        for app in Sistema.listaAppuntamenti:
            if app.get_stato() == True:
                temp.append(app)
        f = open('archivioesiti.pickle', 'wb')
        pickle.dump(temp, f)
        f.close()
        f = open('archivioesiti.pickle', 'rb')
        esiti = pickle.load(f)
        f.close()
        Sistema.listaEsiti.clear()
        for i in range(len(esiti)):
            Sistema.listaEsiti.append(esiti[i])

    #
    @staticmethod
    def downloadClienti():
        Sistema.downloadAppuntamenti()
        temp = []
        for app in Sistema.listaAppuntamenti:
            temp.append(app.get_cliente())
        f = open('archivioclienti.pickle', 'wb')
        pickle.dump(temp, f)
        f.close()
        f = open('archivioclienti.pickle', 'rb')
        clienti = pickle.load(f)
        f.close()
        Sistema.listaClienti.clear()
        for i in range(len(clienti)):
            Sistema.listaClienti.append(clienti[i])

    #
    @staticmethod
    def downloadArticoli():
        f = open('magazzino.pickle', 'rb')
        articoli = pickle.load(f)
        f.close()
        Sistema.magazzino.clear()
        for i in range(len(articoli)):
            Sistema.magazzino.append(articoli[i])
        Sistema.nArticoli = len(Sistema.magazzino)

    #
    @staticmethod
    def downloadCatalogoFornitore():
        f = open('catalogofornitore.pickle', 'rb')
        catalogo = pickle.load(f)
        f.close()
        Sistema.catalogoFornitore.clear()
        for i in range(len(catalogo)):
            Sistema.catalogoFornitore.append(catalogo[i])

    #
    @staticmethod
    def downloadArchivioVendite():
        f = open("archiviovendite.pickle", "rb")
        vendite = pickle.load(f)
        f.close()
        Sistema.archivioVendite.clear()
        for i in range(len(vendite)):
            Sistema.archivioVendite.append(vendite[i])
        Sistema.nVendite = len(Sistema.archivioVendite)

    #
    @staticmethod
    def downloadArchivioOrdini():
        f = open("archivioordini.pickle", "rb")
        ordini = pickle.load(f)
        f.close()
        Sistema.archivioOrdini.clear()
        for i in range(len(ordini)):
            Sistema.archivioOrdini.append(ordini[i])
        Sistema.nOrdini = len(Sistema.archivioOrdini)

    #
    @staticmethod
    def uploadArchivioVendite():
        f = open("archiviovendite.pickle", "wb")
        pickle.dump(Sistema.archivioVendite, f)
        f.close()

    #
    @staticmethod
    def uploadArchivioOrdini():
        f = open("archivioordini.pickle", "wb")
        pickle.dump(Sistema.archivioOrdini, f)
        f.close()

    #
    @staticmethod
    def uploadAppuntamenti():
        f = open('appuntamenti.pickle', 'wb')
        pickle.dump(Sistema.listaAppuntamenti, f)

    #
    @staticmethod
    def uploadEsiti():
        f = open('archivioesiti.pickle', 'wb')
        pickle.dump(Sistema.listaEsiti, f)

    #
    @staticmethod
    def uploadClienti():
        f = open('archivioclienti.pickle', 'wb')
        pickle.dump(Sistema.listaClienti, f)

    #
    @staticmethod
    def uploadArticoli():
        f = open('magazzino.pickle', 'wb')
        pickle.dump(Sistema.magazzino, f)

    #
    @staticmethod
    def uploadCatalogoFornitore():
        f = open('catalogofornitore.pickle', 'wb')
        pickle.dump(Sistema.catalogoFornitore, f)

