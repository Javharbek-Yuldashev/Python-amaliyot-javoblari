# 1

# def katta_harfda_yoz(matn):
#     """Ro'yxat ichidagi har bir matnni bosh harf bilan yozib chiqruvchi funksiya"""
#     yangi_matn=[]
#     while matn:
#         katta_matn = (matn.pop()).title()
#         yangi_matn.append(katta_matn)
#     return yangi_matn

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = katta_harfda_yoz(ismlar[:])
# print(ismlar)
# print(yangi_ismlar)

# 1*

# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#     return matnlar

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)

# 2

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
print(talabalar)


























