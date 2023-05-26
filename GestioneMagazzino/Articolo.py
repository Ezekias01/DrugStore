

class Articolo:
    counter = 0

    def __init__(self, tipo_articolo, nome, prezzo, data_scadenza, quantita, dosaggio):
        self.nome = nome
        self.tipo_articolo = tipo_articolo
        self.id_articolo = Articolo.counter
        self.dosaggio = dosaggio
        Articolo.counter += 1
        self.prezzo = prezzo
        self.data_scadenza = data_scadenza
        self.quantita = quantita
        self.numero = 0

    #getter methods
    def get_idarticolo(self):
        return self.id_articolo

    def get_numero(self):
        return self.numero

    def get_tipo_articolo(self):
        return self.tipo_articolo

    def get_prezzo(self):
        return self.prezzo

    def get_data_scadenza(self):
        return self.data_scadenza

    def get_nome(self):
        return self.nome

    def get_dosaggio(self):
        return self.dosaggio

    def get_quantita(self):
        return self.quantita

    def getInfoProd(self):
        return f"tipo: {self.get_tipo_articolo()} id: {self.get_idarticolo()} nome:{self.get_nome()} prezzo: {self.get_prezzo()} giacenza: {self.get_quantita()} dosaggio: {self.get_dosaggio()} scadenza: {self.get_data_scadenza()}"

    #setter methods
    def set_quantita(self, n :int):
        self.quantita = n

    def set_idtipoarticolo(self, n):
        self.id_articolo = n

    def set_numero(self, n :int):
        self.numero = n

