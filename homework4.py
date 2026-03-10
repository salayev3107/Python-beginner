class Avto:
    def __init__(self,model,rang,korobka,narx):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narx = narx
        self.kilometr = 0
    def get_info(self):
        return f'model:{self.model},rangi:{self.rang},karobkasi:{self.korobka}, narxi:{self.narx}$ '
    def update_km(self,km):
        self.kilometr +=km

avto1 = Avto('malibu','qora','avtomat',20000)
avto2 = Avto('spark','yashil','elektro',10000)
avto3 = Avto('damas','oq','mexanika',5000)
avto1.update_km(5000)
print(avto1.kilometr)
print(Avto.get_info(avto1)) 


class Avtosalon:
    def __init__(self,nomi,manzili):
        self.nomi =nomi
        self.manzili =manzili
        self.garaj = []
        self.avtomobillar_soni = 0
    def add_avto(self,car):
        self.garaj.append(car)
        self.avtomobillar_soni +=1
    def get_cars(self):
      return [avto.get_info() for avto in self.garaj]

salon1 = Avtosalon('uzavto','urgench')
salon1.add_avto(avto1)
salon1.add_avto(avto2)
salon1.add_avto(avto3)

print(salon1.get_cars())
print(salon1.avtomobillar_soni)

print(dir(Avto))
print(dir(avto1.__dict__.keys))
print(dir(str))
print(dir(int))

