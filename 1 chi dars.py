

mahsulotlar = ["katishka","bodiring","olma","gilos","uzum","anjir","orik"]
savat = []
for n in range(5):
    savat.append(input(f"savatga {n+1}-chi mahsulotlarni qoshing :"))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"{mahsulot} mahsuloti savatga qoshildi")

    else:
         print(f"bizda {mahsulot} yoq!") 
     


