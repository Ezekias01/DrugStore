import datetime
from GestioneMagazzino.Articolo import Articolo

class Cliente:

    def __init__(self, nome, cognome, cf):
        self.nome = nome
        self.cognome = cognome
        self.cf = cf

    def get_nome(self):
        return self.nome

    def get_cognome(self):
        return self.cognome

    def get_cf(self):
        return self.cf

    def get_schedacliente(self):
        return f"Dati Cliente\n Nome:{self.nome} Cognome:{self.cognome} Cf:{self.cf} "


class Tampone(Articolo):

    def __init__(self, tipo):
        Articolo.__init__(self, 3, 15, "Tampone")
        self.tipo = tipo
        self.esito = False

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_esito(self):
        return self.esito

    def set_esito(self):
        self.esito = True

    def get_schedatampone(self):
        return f"Dati Tampone\n Nome:{self.get_tipo()} Cognome:{self.get_esito()} Cf:{self.get_prezzo()} "


class Appuntamento:
    #counter = 0

    def __init__(self, cliente: Cliente, tampone: Tampone, data: datetime):
        self.cliente = cliente
        #self.id_app = Appuntamento.counter
        #Appuntamento.counter += 1
        self.esito = False
        self.data = data
        self.isconcluso = False
        self.tampone = tampone

    #getter methods
    def get_esito(self):
        return self.esito

    def get_tampone(self):
        return self.tampone

    def get_idapp(self):
        return self.id_app

    def get_stato(self):
        return self.isconcluso

    def get_cliente(self):
        return self.cliente

    def get_data(self):
        return self.data

    def get_cff(self):
        return self.get_cliente().get_cf()

    def get_schedappuntamnto(self):
        return f"Codice Appuntamento:{self.get_idapp()} cf:{self.get_cliente().get_cf()} Data:{self.data}"

    #setter methods
    def set_idapp(self, n: int):
        self.id_app = n

    def set_isconcluso(self):
        self.isconcluso = True

