
def bahola(isimlar):
    baholar={}
    while isimlar:
        ism=isimlar.pop()
        baho=input(f'{ism.title()}ning bahosni kiriting >>>')
        baholar[ism]=baho
    return baholar
        
oquvchilar=['abror','eldor','said','xabi','azizbek']
baholar=bahola(oquvchilar[:])
#print(baholar)

print("O'quvchilar bahosi royxati:")
for ism,baho in baholar.items():
    print(f"{ism.title()}ning bahosi : {baho}")




def katta_harfqil(matnlar):
    #matnlar=matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()
    return matnlar


ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar=katta_harfqil(ismlar[:])
print(yangi_ismlar)
print(ismlar)


def bahola(isimlar):
    baholar={}
    for ism in isimlar:
        baho=input(f"{ism.title()}ning bahosini kiriitng >>>")
        baholar[ism]=baho
    return baholar
        
oquvchilar=['abror','eldor','said','xabi','azizbek']
baholar=bahola(oquvchilar)
#print(baholar)

print("O'quvchilar bahosi royxati:")
for ism,baho in baholar.items():
    print(f"{ism.title()}ning bahosi : {baho}")

