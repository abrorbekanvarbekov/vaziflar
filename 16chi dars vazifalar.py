car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }
cars= [car0,car1,car2]  
for car in cars:
    print(f"{car['model'].title()} "
          f"{car['rang'].title()}rang "
          f"{car['yil']}-chi yil, "
          f"{car['narh']}$ "
          f"{car['km']} km yurgan "
          f"{car['korobka'].title()}")      
car=car2
print(f"{car['model'].title()} "
f"{car['yil']}-chi yil "
f"{car['rang']}rang "
f"{car['narh']}$ "
f"{car['km']} km yurgan "
f"Korobka {car['korobka'].title()} ")

print(cars[0]['model'].title())

malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
for n in range(10):
    new_car = { # har bir yangi mashina uchun lug'at yaratamiz
        'model':'malibu',
        'rang':None, # rangi noaniq
        'yil':2020,
        'narh':None, # narhi belgilanmagan
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car)
for malibu in malibus[:3]:
    malibu['rang']='qizil'
for malibu in malibus[3:6]:
    malibu['rang']='qora'
for malibu in malibus[6:]:
    malibu['rang']='qora'
    malibu['korobka']='mexan'
for malibu in malibus:
    if malibu['korobka']=='avto':
       malibu['narh']=30000
    else:
        malibu['narh']=25000 
for malibu in malibus:
    print(malibu)                              
            
dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }
for ism,tillar in dasturchilar.items():
    print(f"\n {ism.title()} quydagi dasturlash tillarini biladi: ",end='')
    for til in tillar:
        print(f"{til.upper()}", end='')


hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }

for ism, info in hamkasblar.items():
    print(f"{ism.title()} {info['familiya'].title()}"
    f"{info['tyil']}-chi yilda tugulgan.\n"
    "Quydagi dasturlash tillarini biladi: ")
    for til in info['tillar']:
        print(til.upper())


buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
           'tyil':810,
           'vyil':870,
           'tjoy':'Buxoro',
           'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
           }

qodiriy = {'ism':'Abdulla Qodiriy',
           'tyil':1894,
           'vyil':1938,
           'tjoy':'Toshkent',
           'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
           }

vohidov = {'ism':'Erkin Vohidov',
           'tyil':1936,
           'vyil':2016,
           'tjoy':"Farg'ona",
           'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
           }

navoiy = {'ism':'Alisher Navoiy',
           'tyil':1441,
           'vyil':1501,
           'tjoy':"Xirot",
           'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
           }
b_shaxslar=[buxoriy,qodiriy,navoiy,vohidov]

for shaxs in b_shaxslar:
    umir =shaxs['vyil']-shaxs['tyil']
    print(f"{shaxs['ism'].title()} {shaxs['tyil']}-chi yil\
 {shaxs['tjoy'].title()}da tavallud topgan.\
 {umir} yil umir korgan.\nQuydagi asarlarni yozgan:")
    for asar in shaxs['asarlar']:
        print(asar.title())



#  2 chi usuli
    
    ism=shaxs['ism']
    tyil=shaxs['tyil']
    vyil=shaxs['vyil']
    tjoy=shaxs['tjoy']
    print(f"{ism.title()} {tyil}-chi yil {tjoy.title()}da tavallud topgan.\
 {vyil-tyil} yil umir korgan.\nQuydagi asarlarni yozgan:")
    for asar in shaxs['asarlar']:
        print(asar.title())


ismlar=input("Ismingizni kiriting>>>")
kinolar=[]
for n in range(3):

    kinolar.append(input(f"{ismlar.title()} {n+1}-chi sevimli kinoyizi kiriting."))
print(f"{ismlar.title()}ning sevimli kinolari: ")   
for kino in kinolar:
    print(kino.title())



kinolar={
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }

for ism,kino in kinolar.items():
    print(f"{ism.title()}ning sevimli kinolari: ")
    for kino in kino:
        print(kino.title())
    



davlatlar={
    'ozbekiston':{
        'poytaxti':'toshkent',
        'hududi':'448978kv.km',
        'aholisi':'33000000',
        'pul birligi':'som'
     },
     'rossiya':{
         'poytaxt':'maskva',
         'hududi':'1798246 kv.km',
         'aholisi':144000000,
         'pul birligi':'rubl'
     },
     'aqsh':{
         'poytaxti':'vashington',
         'hududi':'9631418 kv.km',
         'aholisi':327000000,
         'pul birligi':'dollar'
     }
      }
davlat=input("Davlat nomini kiriting>>")
if davlat in davlatlar:
    info=davlatlar[davlat]
    print(f"\n{davlat.title()} poytaxti {info['poytaxti']}\
           \n{info['hududi']} \n{info['aholisi']} mln nafar \
          \nPul birligi: {info['pul birligi']}")
else:
    print("Kechirasiz bizda bunday malumot yoq")


