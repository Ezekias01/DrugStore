from GestioneMagazzino.Articolo import Articolo


class Farmaco(Articolo):

    def __init__(self, nome, prezzo, data_scadenza, quantita, dosaggio, minsan):
        super().__init__("Farmaco", nome, prezzo, data_scadenza, quantita, dosaggio)
        self.minsan = minsan
        self.dosaggio = dosaggio
        self.flagRicetta = False

    #getter methods
    def get_minsan(self):
        return self.minsan

    def get_flagRicetta(self):
        return self.flagRicetta

    def get_dosaggio(self):
        return self.dosaggio

    def getInfoProd(self):
        return f"tipo: {self.get_tipo_articolo()} id: {self.get_idarticolo()} nome:{self.get_nome()} prezzo: {self.get_prezzo()} dosaggio: {self.get_dosaggio()} giacenza: {self.get_quantita()} scadenza: {self.get_data_scadenza()} minsan:{self.get_minsan()}"

    #setter methods
    def set_flagricetta(self):
        self.flagRicetta = True

