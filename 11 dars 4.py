maxsulotlar=["olma","orik","shaftoli","gilos","non","pamidir","tarvuz","banan","uzum","anjir"]
savat=[]
for n in range(5):
    savat.append(input(f"savatga {n+1}-chi mahsulotni kiriting>>>"))
for mahsulot in savat:
        if mahsulot in maxsulotlar:
            print(f"dokonimizda {mahsulot} bor")
        else:
            print(f"dokonimizda {mahsulot} yoq")    