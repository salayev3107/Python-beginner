#
import datetime as dt
bugun = dt.datetime.now()

new_date = dt.timedelta(weeks=2)
second_date = bugun.date()+new_date

for i in range(0,10):
 f = i * new_date
 news = f+bugun.date() 
 print(news)
 
 #

bugun = dt.date.today()
ramazon = dt.date(2026,3,20)
qurbon_hayit = dt.date(2026,5,27)
farq = ramazon - bugun
farq2 = qurbon_hayit - bugun
print (f'Ramazon hayitigacha {farq} qoldi')
print (f'Qurbon hayitigacha {farq2} qoldi')

#

from dateutil.relativedelta import relativedelta
bugun = dt.date.today()
birthday = dt.date(2004,7,31)
diff = relativedelta(bugun,birthday)
print(f'yil:{diff.years}, oy: {diff.months}, kun: {diff.days}')

#

import re
nums = input('Write your tel number: ')
andoza = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
if re.match(andoza,nums):
 print('togri keldi')
else: print('togri kelmadi')
 
#

andoza1 = r'https?://\S+'
matn = """🧵 Tikuvchilik biznesingiz uchun zamonaviy veb-sayt kerakmi?

LORATEX tikuvchilik firmasi uchun to‘liq funksional va zamonaviy veb-sayt ishlab chiqdik 👨‍💻

🌐 Sayt: https://loratex.uz/

🔥 Sayt imkoniyatlari:

✅ Zamonaviy va professional dizayn
✅ Mobil telefon, planshet va kompyuterga mos (Responsive)
✅ Kompaniya xizmatlari va mahsulotlari aniq ko‘rsatilgan
✅ Tez yuklanish va SEO asoslari
✅ Mijozlar ishonchini oshiruvchi tuzilma

💡 Nima uchun sayt muhim?

📌 Brendingingizni kuchaytiradi
📌 Yangi mijozlarni jalb qiladi
📌 Ishonch va professional imidj yaratadi
📌 Reklama va marketing uchun tayyor platforma

Agar siz ham:
— Tikuvchilik sexi
— Fabrika
— Atelier
— Ishlab chiqarish korxonasi
uchun shaxsiy sayt xohlasangiz — yozing 👇

📩 Buyurtma va hamkorlik uchun:
Telegram: @jonibekuralov

🚀 Biznesingizni internetga olib chiqing!"""
f = re.findall(andoza1,matn)
print(f)