otam = {"ismi":"teshaboev avazbek", "yoshi":1972,"tugilgan joyi":"margilon shaxar"}
onam = {"ismi":"teshaboeva muattar", "yoshi":1974, "tugilgan joyi":"paxtakor qishlogi"}
opam = {"ismi":"anvarbekova muhayyo", "yoshi":1994, "tugilgan joyi":"margilon shaxar"}
ukam = {"ismi":"anvarbekov azizbek", "yoshi":2000, "tugilgan joyi":"margilon shaxar"}
     
print(f"Otami ismi {otam['ismi'].title()}. Tugilgan yili {otam['yoshi']}-chi yil. Tugilgan joyi {otam['tugilgan joyi'].title()}")
print(f"Onamni ismi{onam['ismi'].title()}. Tugilgan yili {onam['yoshi']}-chi yil. Tugilgan joyi {onam['tugilgan joyi'].title()}")
print(f"Opami ismi {opam['ismi'].title()} Tugilgan yil {opam['yoshi']}-chi yil, Tugilgan joyi {opam['tugilgan joyi'].title()}")
print(f"Ukamni ismi {ukam['ismi'].title()} Tugilgan yili {ukam['yoshi']}-chi yil, tugilgan joyi {ukam['tugilgan joyi'].title()} ")


taomlar = {
    'otam':"osh",
    'onam': "shashlik",
    'opam': "lagmon",
    'ukam': "norin"
}

taom=taomlar['otam']
taom1=taomlar['onam']
taom2=taomlar['opam']
taom3=taomlar['ukam']
print(f"Otamning sevimli taomi {taom}".title())
print(f"Ukamnig sevimli taomi {taom3}")
print(f"Onamning sevimli taomi {taom1}")
print(f"Opamning sevimli taomi {taom2}")




python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}
print(python_izohli_lugati['integer'].title())  
print(python_izohli_lugati['float'].title()) 
print(python_izohli_lugati['string'].title())  
print(python_izohli_lugati['list'].title())  
print(python_izohli_lugati['tuple'].title())   

lugat = input("Istagan sozingizni yozing\n>>>")
print(python_izohli_lugati.get(lugat,"Bunday soz mavjud emas"))


kalit = input("Kalit sozni kiriting\n>>>").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima== None:
    print("Bunday soz mavjud emas")
else:
    print(f"{kalit} sozi {tarjima.lower()} bolip tarjima qilinadi ")
