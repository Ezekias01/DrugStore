class Ordine():

    def __init__(self, codice, fornitore, totale, date):
        self.codice = codice
        self.fornitore = fornitore
        self.totale = totale
        self.date = date

    #getter methods
    def get_codiceordine(self):
        return self.codice

    def get_totordine(self):
        return self.totale

    def get_dataordine(self):
        return self.date

    def get_fornitore(self):
        return self.fornitore

    def getInfoOrdine(self):
        return f"codice: {self.get_codiceordine()} tot: {self.get_totordine() }"
