# 1

# python_izohli_lugat = {
#     "integer":"Butun son",
#     "float":"o'nlik son",
#     "string":"matn",
#     "list":"ro'yhat",
#     "dictionary":"lug'at",
#     "tuple":"o'zgarmas",
#     "boolean":"mantiqiy qiymat",
#     "for":"uchun",
#     "if":"agar",
#     "in":"ichida"
#     }

# for k, v in sorted(python_izohli_lugat.items()):
#     print(f"{k.title()} - {v}")

# 2

# davlat_poytaxt = {
#     "Uzbekistan":"Tashkent", 
#     "AQSh":"Vashington", 
#     "Rossiya":"Moskva", 
#     "Germaniya":"Berlin", 
#     "Yaponya0":"Tokio"}

# print("\n")
# print("Davlatlar ro'yxati:")
# for davlat in sorted(davlat_poytaxt.keys()):
#     print(f"{davlat.title()}")
# print("\n")
# print("Davlatlar poytaxti:")
# for poytaxt in sorted(davlat_poytaxt.values()):
#     print(poytaxt.title())

# davlat = input("Davlat nomini kiriting: ")
# if davlat in davlat_poytaxt.keys():
#     print(f"{davlat.title()}ning poytaxti - {davlat_poytaxt[davlat]}")
# else:
#     print("Bizda bunday ma'lumot yo'q")

# 3

menu = {
        "osh":20000, 
        "sho'rva":10000, 
        "chuchvara":15000, 
        "manti":4000, 
        "somsa":6000,
        "lag'mon":15000,
        "beshtekst":25000,
        "xonim":5000,
        "pirajok":25000,
        "shashlik":15000
        }

print("3 ta taom kiriting:")
taom_1 = input("1-toam: ") 
taom_1 = taom_1.lower()
taom_2 = input("2-taom: ")
taom_2 = taom_2.lower()
taom_3 = input("3-taom: ")
taom_3 = taom_3.lower()

if taom_1.lower() in menu.keys():
    print(f"{taom_1.title()}ning narxi - {menu[taom_1]} so'm")
else:
    print(f"Kechirasiz, bizda {taom_1.lower()} yo'q'")
if taom_2.lower() in menu.keys():
    print(f"{taom_2.title()}ning narxi - {menu[taom_2]} so'm")
else:
    print(f"Kechirasiz, bizda {taom_2.lower()} yo'q'")
if taom_3.lower() in menu.keys():
    print(f"{taom_3.title()}ning narxi - {menu[taom_3]} so'm")
else:
    print(f"Kechirasiz, bizda {taom_3.lower()} yo'q'")
















