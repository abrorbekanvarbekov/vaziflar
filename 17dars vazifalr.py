print("Kiritilgan raqamni kvadratini hisoplab beradigan dastur")
savol="Istagan sonni kiriting"
savol+="Dasturni toxtatish uchun (stop) dep kiriting "

qiymat=''
while qiymat!='exit':
    qiymat=input(savol)
    if qiymat!='exit':
        print(float(qiymat)**2)
print("Dastur tugadi.")        

 
ism=input("Ismingizni nima?>>")
yosh=f"Salom {ism.title()} Yoshingiz nechida?>>"
yosh=input(yosh)
boy="Boyingiz mechi?"
boy=input(boy)

print("1 da 10 gacha bolgan sonlarni kvadratini aniqlovchi dastur")
sonlar=list(range(1,11))
for son in sonlar:
    if son ==7:
        break
    print(f"{son}ning kvadrati {son**2}ga teng")
son=1
while son<=5:
    
    print(son)
    son+=1

print("kiritilgan sonni kvadratini chiqarip beradigan dastur")

qiymat=''
while qiymat!="exit":
    qiymat=input("Istagan sonni kiriting")
    if qiymat!="exit":
        print(float(qiymat)**2)
print("dastur tugadi")        
qiymat=True
while qiymat:
    qiymat=input("Istalgan sonni kiriting>> ")
    if qiymat=='exit':
        break
    else:
        print(float(qiymat)**2)
print("dastur yakunlandi")        

sonlar=list(range(1,11))
for son in sonlar:
    if son ==7:
        break
    else:
        print(f"{son}ning kvadrati {son**2}ga teng")


kitoplar=''
while kitoplar!='toxta':
    

    kitoplar=input("Yaxshi korgan kitoplarizi kiriting>> ")
    if kitoplar!='toxta':
        
        print(kitoplar)
    else:
        print("dastur tamom".upper())




savol="Yoshingizni kiriting :"

while True:
    qiymat=input(savol)
    if  qiymat== 'exit' or qiymat=='quit':
        
     break
    yosh=int(qiymat)

    if yosh<7:
        narh=2000
    elif 7<=yosh<=18:
        narh=3000
    elif 18<=yosh<=65:
        narh=10000
    else:
        narh=0
    if narh==0:
        print(f"{yosh} yoshlilarga kirish bepul")
    else:
        print(f"chipta narhi {yosh} yoshlilarga {narh}so'm")                


            


savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = int(input(savol))
    if qiymat<0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")

kitoplar=("Yaxshi korgan kitoplaringizni kiriting>>")
kitop=[]
savol=""
while savol!='stop':
    savol=input(kitoplar)
    if savol!='stop':
        print(savol.title())
    else:
        print("Dastur tamom")    

savol=("Yaxshi korgan kitoplarizi kiriting>>")
kitoplar=True
while kitoplar:
    qiymat=input(savol)
    if qiymat=='stop':
        kitoplar=False
    else:
        print(qiymat.upper())
print("dastur yakunlandi")       

while True:
    qiymat=input(savol)
    if qiymat=='stop':
        break
    else:
        print(qiymat)
print("dastur yakunlandi".upper())

print("Muzey kirish chipta narhlari: ")

savol=("Yoshingizni kiriting>>>")
qiymat=''
while qiymat!='stop'or qiymat!='quit':
    qiymat=int(input(savol))
    if str(qiymat)!='stop'or str(qiymat)!='quit':
        
        yosh=qiymat



    

    if yosh<7:
        narh=2000
    if 7<yosh<18:
        narh=3000
    if 18<yosh<65:
        narh=10000
    if yosh>65:
        print("sizga kirish bepul")
    else:
        print(f"Chipta narhi {narh}")
        
        
print("Dastur yakunlandi")





