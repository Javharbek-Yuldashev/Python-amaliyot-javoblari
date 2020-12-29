# 1

# shaxs1 = {"ism":"Abu Abdulloh Muhammad ibn Ismoil", "tyil":810, "tjoy":"buxoro", "yil":"60", 
#           "asarlar":["Al-jome' as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag'ir"]}
# shaxs2 = {"ism":"Abdulla Qodiriy", "tyil":1894, "tjoy":"toshkent", "yil":"44",
#           "asarlar":["O'tkan kunlar", "Mehrobdan Chayon", "Obid ketmon"]}
# shaxs3 = {"ism":"Erkin Vohidov", "tyil":1936, "tjoy":"farg'ona", "yil":"80",
#           "asarlar":["Tong nafasi", "Qo'shiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"]}
# shaxs4 = {"ism":"Alisher Navoiy", "tyil":1441, "tjoy":"xirot", "yil":"60",
#           "asarlar":["Xamsa", "Lison ut-Tayr", "Mahbub ul-Qulub", "Munojot"]}

# shaxslar = [shaxs1, shaxs2, shaxs3, shaxs4]

# for shaxs in shaxslar:
#     # print(f"{shaxs['ism'].title()} {shaxs['tyil']}-yilda {shaxs['tjoy'].title()}da tavollud topgan. "
#     #       f"{shaxs['yil']} umr ko'rgan.")
#       print(f"{shaxs['ism'].title()}ning mashxur asarlari: ")
#       for asar in shaxs['asarlar']:
#           print(asar)

# 2

# kinolar = {
#            "Ali":["Terminator","Rambo","Titanik"],
#            "Vali":["Tenet", "Inception", "Installer"],
#            "Hasan":["Abdullajon","Bomba","Shaytanat"],
#            "Huasn":["Tanka","Jems Bond","John Wick"]
#            }
           
# for ism, kino in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for film in kino:
#         print(film)

# 3

davlatlar = {
    "O'zbekiston":{"poytaxt":"Toshkent",
                   "hudud":448978,
                   "aholisi":33-000-000,
                   "pul":"so'm"
                   },
    "Rassiya":{"poytaxt":"Maskva",
                   "hudud":17098246,
                   "aholisi":144-000-000,
                   "pul":"rubl"
                   },
    "AQSh":{"poytaxt":"Vashington",
                   "hudud":448978,
                   "aholisi":327-000-000,
                   "pul":"dollar"
                   },
    "Malayziya":{"poytaxt":"Kuala-Lumpur",
                   "hudud":329750,
                   "aholisi":25-000-000,
                   "pul":"rinngit"
                   }, 
            }

# for davlat, info in davlatlar.items():
#     print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}",
#           f"\nHududi: {info['hudud']} kv.km",
#           f"\nAholisi: {info['aholisi']}",
#           f"\nPul birligi: {info['pul']}") 
 
davlat = input("Davlat nomi kiriting: ")    
if davlat in davlatlar.keys():
    info = davlatlar[davlat]
    print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}",
           f"\nHududi: {info['hudud']} kv.km",
           f"\nAholisi: {info['aholisi']}",
           f"\nPul birligi: {info['pul']}") 
else:
    print('Bizda bu davlat haqida ma\'lumot yo\'q') 
    







