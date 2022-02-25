mahsulotlar=["olma","orik","shaftoli","gilos","non","pamidir","tarvuz","banan","uzum","anjir","un","guruch","bodiring"]
savat=[]
b_mahsulot=[]
y_mahsulot=[]
for n in range(5):
    savat.append(input(f"Savatga {n+1}-chi mahsulotni kiriting>>>"))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        b_mahsulot.append(mahsulot)
    else:
        y_mahsulot.append(mahsulot)

if y_mahsulot:
    print(f"bizda quydagi mahsulotlar yoq:")
    for mahsulot in y_mahsulot:
        print(mahsulot)
else:
    print("Bizda hamma mahsulot bor")        
