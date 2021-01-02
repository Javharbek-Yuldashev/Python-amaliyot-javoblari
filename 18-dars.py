# 1

# buyurtmalar = []
# n = 1
# while True:
#     savol = f"{n}- buyurtmani kiriting: "
#     buyurtma = input(savol)
#     buyurtmalar.append(buyurtma)
#     ishora = (input("Yana buyurtma qo'shishni xohlaysizmi (ha\yo'q): ")).lower()
#     if ishora != "yo'q":
#         n +=1
#     else:
#         break
# print("\nSizning buyurmalaringiz:")
# for buyurtma1 in buyurtmalar:
#     print(buyurtma1.title())

# 2

# ebozor = {}
# n = 1
# while True:
#     mahsulot = input(f"{n}- mahsulotingizni kiriting: ")
#     narx = input(f"{mahsulot.title()}ning narxini kiriting: ")
#     ebozor[mahsulot] = int(narx)
#     ishora = (input("Yana mahsulot qo'shishni xohlaysizmi (ha\yo'q): ")).lower()
#     if ishora == "ha":
#         n +=1
#     else:
#         break
# for mahsulot, narx in ebozor.items():
#     print(f"{mahsulot.title()}ning narxi {narx} so'm")

# 3

# buyurtmalar = ['Olma', 'Suv', 'Sut', 'Anor', 'Nok']
# ebozor =  {'Olma': 8000, 'Nok': 16000, 'Mandarin': 45000, 'Anor': 20000, 'Sabzi': 3000, 'Karam': 5000}
# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in ebozor:
#          narx = ebozor[buyurtma]
#          print(f"{buyurtma.title()}ning narxi {narx} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma.lower()} mavjud emas")

















