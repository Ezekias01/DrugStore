import pickle
from datetime import datetime

from GestioneMagazzino.Articolo import Articolo
from GestioneMagazzino.Farmaco import Farmaco



lista = []
magazzino = []
a = 2026
m = 5
g = 8
datas = datetime(a, m, g)
pro = Articolo("Non Farmaco", "Zuccari Succo di Aloe", 18.89, datas, 170, "500ml")
magazzino.append(pro)

a = 2028
m = 6
g = 19
datas = datetime(a, m, g)
f = Farmaco("Esi Propolaid Rinoact",5.76,datas,290,"20ml","973263825")
magazzino.append(f)

m = 7
g = 20
datas = datetime(a, m, g)
fa = Farmaco("Malox Plus",12.7,datas,200,"50 compresse x 8,5mg","005672993")
fa.set_flagricetta()
magazzino.append(fa)

g = 19
datas = datetime(a, m, g)
far = Farmaco("Foille Scottature",10,datas,600,"29,5g","040313013")
magazzino.append(far)



a = 2028
m = 3
g = 1
datas = datetime(a, m, g)
prod = Articolo("Non Farmaco", "Rilastil Crema Pelli", 36.50, datas, 260, "200ml")
magazzino.append(prod)

a = 2024
m = 3
g = 11
datas = datetime(a, m, g)
prodot = Articolo("Non Farmaco", "Shampoo Euphidra", 5.10, datas, 300, "200ml")
magazzino.append(prodot)




x = open("catalogofornitore.pickle", "wb")
pickle.dump(magazzino, x)
x.close()
y = open("catalogofornitore.pickle", "rb")
lista = pickle.load(y)
y.close()

for i in lista:
   print( i.getInfoProd() )