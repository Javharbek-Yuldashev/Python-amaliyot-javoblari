# 1

# def kopaytir(*sonlar):
#     """Kiritilgan sonlar ko'paytmasini hisoblovchi funksiya"""
#     kopaytma=1
#     for son in sonlar:
#         kopaytma*=son
#     return kopaytma

# print(kopaytir(2,3,4))
# print(kopaytir(2,3,4,5))
# print(kopaytir(2))

# 2

def talaba_info(ism, familya, **malumotlar):
    """Talaba haqidagi ma'lumotlarni lug'at ko'rinishida chiqrib beruvchi funksiya"""
    malumotlar['ism']=ism
    malumotlar['familya']=familya
    return malumotlar

talaba1 = talaba_info('Javharbek', 'Yuldashev', t_yili=2001, t_joy="Farg'ona")
talaba2 = talaba_info("Abdusattor", "Is'hoqov", t_yili=1995, t_joy="Andijon", yoshi=2021-1995)

print(talaba1)
print(talaba2)





