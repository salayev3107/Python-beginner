class Fan:
    def __init__(self,nomi):
        self.nomi = nomi
    def gett_info(self):
        return f'fanning nomi: {self.nomi}'
    

class talaba:
    __talabalar_soni = 10
    def __init__(self,ism,familiya,yil):
        self.ism = ism
        self.familiya = familiya
        self.yil = yil
        self.fanlar = []
    def fanga_yozil(self,fann):
        self.fanlar.append(fann)
    @classmethod 
    def get_talablar_soni(cls):
        return cls.__talabalar_soni

    def remove_fan(self,r_f):
        if r_f in self.fanlar:
           self.fanlar.remove(r_f)
        else: print('siz bu fanga yozilmagansiz')

    def get_info(self):
        return [t.gett_info() for t in self.fanlar]

fan1= Fan('matem')
fan2= Fan('Rustili')
fan3= Fan('fizika')
fan4= Fan('kimyo')

talaba1 = talaba('shermat','niyazov',2000)
talaba1.fanga_yozil(fan1)
talaba1.fanga_yozil(fan2)
talaba1.fanga_yozil(fan3)
talaba1.fanga_yozil(fan4)
print(talaba1.get_info())
talaba1.remove_fan(fan4)
print(talaba1.get_info())
print(talaba1.get_talablar_soni())



class Shahs:
    __odamlar_soni = 20
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.passport = passport
        self.tyil = tyil
        self.familiya = familiya
    def get_info(self):
        info = f'{self.ism} {self.familiya}'
        info+=f' passport: {self.passport} , {self.tyil} da tugilgan'
        return info
    def get_age(self,yil):
        return yil - self.tyil
    @classmethod 
    def get_odamlar_soni(cls):
        return cls.__odamlar_soni
    
shahs1 = Shahs('erkin','mominov','ad124578',2006)
print(shahs1.get_odamlar_soni())
class professor(Shahs):
    def __init__(self, ism, familiya, passport, tyil,ish_joyi):
        super().__init__(ism, familiya, passport, tyil)
        self.ish_joyi = ish_joyi
    def dars_berish(self):
        return f'Professor {self.ism} {self.familiya} dars bermoqda' 
    def get_info(self):
        info = f'professor {self.ism} {self.familiya} {self.ish_joyi} da ishlaydi' 
        return info   
class foydalanuvchi(Shahs):
    def __init__(self, ism, familiya, passport, tyil,id_raqam):
        super().__init__(ism, familiya, passport, tyil)
        self.id_raqam = id_raqam

    def tizimga_kirish(self):
        return f'foydalanuvchi {self.ism} {self.familiya} tizimga kirmoqda'
    def get_info(self):
        info = f' {self.ism} {self.familiya} id raqami {self.id_raqam}'  
        return info
class sotuvchi(Shahs):
    def __init__(self, ism, familiya, passport, tyil,dukon):
        super().__init__(ism, familiya, passport, tyil)
        self.dukon = dukon

    def sotish(self):
        return f'{self.ism} li sotuchi narsasini sotyabdi'
    def get_info(self):
        info = f'sotuvchi {self.ism} {self.familiya}  {self.dukon} nomli dukonda ishlaydi'
        return info
class mijoz(Shahs):
    def __init__(self, ism, familiya, passport, tyil,navbat):
        super().__init__(ism, familiya, passport, tyil)   
        self.navbat = navbat
    def sotib_olish(self):
        return f'({self.navbat} navbat dagi mijoz narsa sotib olyabti)'
    def get_info(self):
        info = f' {self.ism} {self.familiya} mijoz va uning navbati: {self.navbat}'

class admin(foydalanuvchi):
    def __init__(self, ism, familiya, passport, tyil, id_raqam,admin_lavozim):
        super().__init__(ism, familiya, passport, tyil, id_raqam)
        self.admin_lavozim = admin_lavozim
    def ban_user(self):
        return 'Foydalanuvchi bloklandi'
    def get_info(self):
        info = f'{self.ism} {self.familiya} '
        info += f' lavozimi: {self.admin_lavozim}! yili: {self.tyil}'
        return info
admin1 = admin('john','stounz','ad12345',1999,'00132345','bosh admin')
print(admin1.ban_user())
print(admin1.get_info())