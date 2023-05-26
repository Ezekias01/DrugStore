class Vendita():
    # classe di modellazione

    def __init__(self, codice, totale, date):
        self.codice = codice
        self.totale = totale
        self.date = date

    #getter methods
    def get_codicevendita(self):
        return self.codice

    def get_totvendita(self):
        return self.totale

    def get_datavendita(self):
        return self.date
