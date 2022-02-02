talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }
# print(talaba_0.items())
for kalit,qiymat in talaba_0.items():
    print(f"Kalit : {kalit}")
    print(f"Qiymat : {qiymat}")

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310', 
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'
    }

for k,q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")
 

mahsulotlar = {     
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

print("Dokondagi mahsulotlar :")
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())


bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()}ning narxi {mahsulotlar[mahsulot]} som")

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"iltimos dokonigizga {buyum.title()}ni ham olip keling!")

print("Dokonimizdagi mahsulotlar : ")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())
for mahsulot,qiymat in mahsulotlar.items():
    print(f"{mahsulot.title()}ning narhi {qiymat} som")

print("Foydalanuvchilar quydagi telefonlarni ishlatadi\n>>>")
for tel in telefonlar.values():
    print(tel.title())

for tel in set(telefonlar.values()):
    print(tel.title())


vazifa

lugat = {
    "integer":"butun son",
    "list":"royxat",
    "tuple":"ozgarmas qiymat",
    "boolean":"mantiqiy qiymat",
    "float":"onlik son",
    "if":"shartni tekshirish aperatori",
    "input":"foydalanuvchidan sorash",
    "for":"bir amalni qayta-qayta bajarish stikli",
    "title":"qiymatlarni bosh xarfini kotta xarifda chiqarish",
    "append":"qiymat qoshish stikli"
}
for k,q in sorted(lugat.items()):
    print(f"{k.title()} - {q.title()}")




print("Dunyo davlatlari :   Davlatlarning poytaxtlari.")
Davlatlar= {
    "aqsh":"washington",
    "italiya":"rim",
    "ozbekiston":"toshkent",
    "korea":"seul",
    "qizgiziston":"dushanbe",
    "qozogiston":"nursulton",
    "rossiya":"maskva",
    "singapur":"kuala-limpur"
}

for d,p in sorted(Davlatlar.items()):
    print(f"{d.upper()} - {p.title()}")

print("Dunyo davlatlari : ")
for davlat in sorted(Davlatlar):
    print(davlat.upper())

print("Davlatlar poytaxti : ")
for poytaxt in sorted(Davlatlar.values()):
    print(poytaxt.title())    
d = input("Qaysi davlatni poytaxtini bilishni istaysiz?\n>>>".lower())
p = Davlatlar.get(d)
if p == None:
    print(f"kechirasiz bizda {d} haqida malumot yo\'q")
else:
    print(f"{d.upper()}ning poytaxti {p.title()} shahri")        


menu = {
    "osh":8000,
    "qozonkabob":10000,
    "lagmon":10000,
    "manti":11000,
    "xonim":12000,
    "shorva":7000,
    "chuchvara":9000,
    "non":2000,
    "somsa":3000,
    "lawash":5000,
    "shakarop":3000
}
print("3 ta taom buyurtma bering\n>>>")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom : ".lower()))
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()}ning narhi {menu[buyurtma]} som")
    else:
        print(f"Kechirasiz bizda {buyutma.title()} yoq!")        

