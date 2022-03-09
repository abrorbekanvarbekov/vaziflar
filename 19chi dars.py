# def salom_ber():
#     """salom beradigan funksiya"""
#     print("Assalomu alekum")
# salom_ber()


# def salom_ber(ism):
#     """foydalanuvchi ismini sorap salom beradigan funksiya"""
#     print(f"Assalom alekum {ism}")
# salom_ber('abror')

# def toliq_ism(ism,familya):
#     """Toliq isimni chiqaradigan funksiya"""
#     print( f"\nFoydalanuvchini ismi :{ism.title()}\nFoydalanuvchini familyasi :{familya.title()}")
# toliq_ism('abror','anvarbekov')
# toliq_ism('said','matmusaev')

# def yosh_hisopla(ism,t_yil):
#     """Foydalanuvchini ismini va yoshini hisoplab beruvchi funksiya"""
#     print(f"Foydalanuvching ismi :{ism.title()} {2022-t_yil} yoshda")
# yosh_hisopla('abror',1997)
# yosh_hisopla('said',1998)


#    ## vazifalar:
# def ism_yosh(ism,yosh):
#     print(f"Foydalanuvchini ismi :{ism.title()} {2022-yosh}-chi yilda tugulgan")
# ism_yosh('abror',25)
# ism_yosh('said',24)


# def kvadrati_kub_hisopla(kavadrat,kub):
#     """Sonlarni kvadratini va kubini hisoplaydigan funksiya"""
#     print(f"{kavadrat} ning kvadrati :{kavadrat**2} ga teng\n{kub} ning kubi :{kub**3}ga teng")
# kvadrati_kub_hisopla(5,7)


# def juft_toqson_aniqla(son1):
#     """Sonlarni juft yoki toqligini aniqlaydi"""
    
#     if son1%2:
#         print(f"{son1} toq son ")
#     else:
#         print(f"{son1} juft son")
# juft_toqson_aniqla(5)
# juft_toqson_aniqla(21)

# def kattsonni_chiqar(son1,son2):
#     """Sonlarni kottasini chiqaruvchi funksiya"""
#     if son1<son2:
#         print(f"{son1}<{son2}")
#     elif son1>son2:
#         print(f"{son1}>{son2}")
#     else:
#         print(f"{son1}={son2}")
# kattsonni_chiqar(24,65)
# kattsonni_chiqar(1223*2, 48*2)
# kattsonni_chiqar(44,44)

# def daraja(x,y):
#     """x ni y- darajaga oshiruvchi funksiya"""
#     print(f"{x} ning {y}-chi darajasi {x**y} ga teng")
# daraja(5,2)
# daraja(10,5)

# def bolinish_alomatlari(son):
#     """soni 2 ,3,4,5....10 gacha qoldiqsiz bolinishini aniqlaydigan funksiya"""
#     for n in range(2,11):
#         if not son% n:
#             print(f"{son} soni {n} soniga qoldiqsiz bolinadi ")
# bolinish_alomatlari(40)
# bolinish_alomatlari(56*45)

