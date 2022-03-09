def toliq_ism_yasa(ism,familiya,otasining_ismi=None):
    """Toliq ism yasovchi funksiya"""
    if otasining_ismi:
       toliq_ism=f"Foydalanuvchi {ism} {familiya} {otasining_ismi}"
    else:
        toliq_ism=f"Foydalanuvchi {ism} {familiya}"
    return toliq_ism.title()

talaba1=toliq_ism_yasa('abror','anvarbekov','avazbek ogli')
talaba2=toliq_ism_yasa('eldor','mahmudov')
print(talaba1)
print(talaba2)


def avto_info(kompaniyasi,model,rangi,yili,korobka,narhi=None):
    avtolar={
        'kompaniya':kompaniyasi,
        'model':model,
        'rang':rangi,
        'yil':yili,
        'korobka':korobka,
        'narh':narhi
    }
    return avtolar

avto1=avto_info('hyundai','sonata','qizil',2021,'avtomat',20000)
avto2=avto_info('Gm','nexia','qora',2018,'avtomat',)
#print(avto1)
avtolar=[avto1,avto2]

for avto in avtolar:
    if avto['narh']:
        narh=avto['narh']
    else:
        narh="Nomalum"
    print(f"{avto['rang']} {avto['model']} {avto['yil']} {avto['narh']}")

def oraliq(min,max,qadam=None):
    sonlar=[]
    while min<max:
        sonlar.append(min)
        min+=1
    return sonlar
print(oraliq(1,101))
                  

def avto_info(kompaniyasi,model,rangi,yili,korobka,narhi=None):
    avtolar={
        'kompaniya':kompaniyasi,
        'model':model,
        'rang':rangi,
        'yil':yili,
        'korobka':korobka,
        'narh':narhi
    }
    return avtolar

print("Sayitimizdagi avtolar ro'yxatini shakillantiramiz")
avtolar=[]
while True:
    print("\nQuydagi malumotlanrni kiriting!")
    kompaniya=input("Avto kompaniyasini kirting>>>")
    model=input("Avto modelini kiriting>>>")
    rangi=input("Avto rangini kiriting>>>")
    yili=input("Avto yilini kiriting>>>")
    korobka=input("Avto korobkasini kiriting>>>")
    narh=input("Avto narhini kiriting>>>>")
    avtolar.append(avto_info(kompaniya,model,rangi,yili,korobka,narh))
    javop=input("Yana avto qoshasizmi? Ha/Yoq>>>")
    if javop=='yoq':
        break


print("Sayitimizdagi avtolar royxati:")
for avto in avtolar:
    if avto['narh']:
        narh=avto['narh']
    else:
        narh="Nomalum"
    print(f"{avto['rang'].title()} {avto['model'].title()} {avto['yil']}-chi yil Narhi: {avto['narh']}")


def malumot_saqla(ism,familiya,t_yil,t_joy,e_manzil=None,tel_nomer=None):
    info={
        'ism':ism,
        'familiya':familiya,
        't_yil':t_yil,
        't_joy':t_joy,
        'e_manzil':e_manzil,
        'tel_nomer':tel_nomer
    }
    return info

print("Mizjozlar haqidagi malumotlarni kiriting")
mijozlar=[]
while True:
    ism=input("Ismi?>> ")
    familiya=input("Familiyasi?>> ")
    t_yil=input("Tugilgan yili?>> ")
    t_joy=input("Tugilgan joyi?>> ")
    e_manzil=input("E_manzili?>> ")
    tel_nomer=input("Tel nomeri?>> ")
    mijozlar.append(malumot_saqla(ism,familiya,t_yil,t_joy,e_manzil,tel_nomer))
    javop=input("Yana malumot kiritasizmi? ha/yoq >> ")
    if javop=='yoq':
        break
print("Mijozlar:")
for mijoz in mijozlar:
    print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}\
 \n{mijoz['t_yil']} da tugilgan, Telefon nomeri: {mijoz['tel_nomer']}")

def malumot_saqla(ism,familiya,t_yil,t_joy,e_manzil=None,tel_nomer=None):
    info={
        'ism':ism,
        'familiya':familiya,
        't_yil':t_yil,
        't_joy':t_joy,
        'e_manzil':e_manzil,
        'tel_nomer':tel_nomer
    }
    return info


malumot1=malumot_saqla('abror','anvarbekov',1997,'ozbekiston','1aabror@gmail.com')
malumot2=malumot_saqla('eldor','mahmudov',1998,'ozbekiston',)
malumotlar=[malumot1,malumot2]

for malumot in malumotlar:
    if malumot['e_manzil'] or malumot['tel_nomer']:
        e_manzil=malumot['e_manzil']
        tel_nomer=malumot['tel_nomer']
    else:
        e_manzil="Mavjud emas"
        tel_nomer="Mavjud emas"
    print(f"{malumot['ism'].title()} {malumot['familiya'].title()}\n{malumot['t_yil']}-chi yil\
 \ntugilgan joyi :{malumot['t_joy'].title()}\
 \ne_manzili :{malumot['e_manzil']}\nTel nomeri: {malumot['tel_nomer']}"



def kattasi(x,y,z):
    max=x
    if y>=max:
        max=y
    if z>=max:
        max=z
    return max

print(kattasi(50,33,56,44))

