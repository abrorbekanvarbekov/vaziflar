isimlar=[]
n=1
print("Yaqin dostlaring'iz ro'yhatini tuzamiz :")
while True:
    ism=input(f"{n}-chi dostingizni ismini kiriting >>>")
    isimlar.append(ism.title())
    javop=input("Yana isim qoshasizmi?  Ha/Yoq >>>")
    if javop=='yoq':
        break
    else:
        n+=1
print('Dostlaringiz royhati : ')
for ism in isimlar:
    print(ism.title())

print("while yordamida lugat toldirish")
dostlar={}
ishora=True
n=1
while ishora:
    ism=input(f"{n}-chi dostingizni ismini kiriting >>>")
    yosh=int(input(f"{ism.title()}ning yoshini kiriitng >>>"))
    dostlar[ism]=yosh
    n+=1
    javop=input("Yana dostingzni qoshasizmi? Ha/Yoq >>>")
    if javop =='yoq':
        ishora=False


print("Dostlaringiz royhati :")
for ism,yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")

print("while yordamida lugat toldirish")
dostlar={}
#ishora=True
n=1
while True:
    ism=input(f"{n}-chi dostingizni ismini kiriting >>>")
    if ism=='stop':
        break
    yosh=int(input(f"{ism.title()}ning yoshini kiriitng >>>"))
    dostlar[ism]=yosh
    n+=1
    #javop=input("Yana dostingzni qoshasizmi? Ha/Yoq >>>")
    #if ism=='stop':
   #    ishora=False


print("Dostlaringiz royhati :")
for ism,yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")


cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia','audi']
while 'audi' in cars:
    cars.remove('audi')
print(cars)

talabalar = ['hasan', 'husan', 'olim', 'botir']
baholangan_tlar={}
while talabalar:
    talaba=talabalar.pop()
    baho=input(f"{talaba.title()}ning bahosini kiriitng >>>")
    print(f"{talaba.title()} baholandi")
    baholangan_tlar[talaba]=baho
for ism,baho in baholangan_tlar.items():
    print(f"{ism.title()}ning bahosi : {baho}")


print("Buyurtma qabul qilamiz :")

mahsulotlar=[]
n=1
while True:
    mahsulot=input(f"{n}-chi mahsulotni kiriting >>>")
    if mahsulot=='stop':
        break
    else: 
     mahsulotlar.append(mahsulot.title())

print("Mahsulotlar royhati :")
for mahsulot in mahsulotlar:
    print(mahsulot.title())




print("e-bozor mahsulotlarni royhatini tuzamiz:")
e_bozor={}
n=1

while True:
    mahsulot=input(f"{n}-chi mahsulotni nomini kiriting>>>")
    if mahsulot=='stop':
        break
    narh=int(input(f"{mahsulot.title()}ning narhini kiriting >>>"))
    e_bozor[mahsulot]=int(narh)
    n+=1

  

print("E-bozor mahsulotlar royhati:")
for mahsulot,narh in e_bozor.items():
    print(f"{mahsulot.title()}ning narhi : {narh} so'm.")



buyurtmalar = []
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000,
               'un':30000,
               'shakar':25000,
               'kartoshka':15000,
               }
karzinka={}
while True:
    mahsulot=input("Mahsulot nomini kiriting>>>")
    if mahsulot=='stop':
        break
    buyurtmalar.append(mahsulot)
    buyurtma=buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh=mahsulotlar[buyurtma]
        karzinka[buyurtma]=narh
        print(f"{buyurtma.title()}ning narhi {narh}")
    else:
        print(f"Bizda {buyurtma.title()} yoq")

print("Dokonimizda bor mahsulotlar:")
for mahsulot,narh in karzinka.items():
    print(f"{mahsulot.title()}ning narhi : {narh} so'm")

        