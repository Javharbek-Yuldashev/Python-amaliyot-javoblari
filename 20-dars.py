# def oraliq(min,max,qadam=1):
#     """2 son oralig'ini "qadam" bo'yicha qaytaruvchi funksiya"""
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar

# print(oraliq(2,10))
# print(oraliq(2,10,3))

# 1

# def foydalonuvch_info(ism,familya,tugilgan_yil,tugilgan_joy,email=None,telefon = None):
#     """Foydalanuvchi haqida ma'lumot qaytaruvchi funksiya"""
#     foydalanuvchi = {'ism':ism,
#                       'familya':familya,
#                       'tugilgan_yil':tugilgan_yil,
#                       'tugilgan_joy':tugilgan_joy,
#                       'yosh':2020-tugilgan_yil,
#                       'email':email,
#                       'telefon':telefon}
#     return foydalanuvchi 
    
# foydalanuvchi_1 = foydalonuvch_info('Javharbek', 'Yuldashev', 2001, 'langar', \
#                                     'yuldashevjavharbek@gmail.com','+99899 609 85 84')
# foydalanuvchi_2 = foydalonuvch_info("Asror", "G'ofuurov", 1991, "farg\'ona")
# print(foydalanuvchi_1)
# print(foydalanuvchi_2)

# # 2

# mijozlar = []
# while True:
#     print("\nQuyidagi ma'umotlarni kiriting:")
#     ism=input("Ism: ")
#     familya=input("Familya: ")
#     tugilgan_yil=int(input("Tug'ilgan yilingiz: "))
#     tugilgan_joy=input("Tug'ilgan joy: ")
#     email=input("Emailingiz: ")
#     telefon=input("Telefon raqamingiz: ")

#     mijozlar.append(foydalonuvch_info(ism,familya,tugilgan_yil,tugilgan_joy,email,telefon))

#     javob = input('Yana foydalanuvchi kiritmoqchimisiz (yes/no): ')
#     if javob == 'no':
#         break
# print("\nFoydalanuvchilar haqida ma'lumot: ")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism']} {mijoz['familya']}, {mijoz['tugilgan_yil']}-yilda \
#   {mijoz['tugilgan_joy'].title()}da tug'ilgfan. \nEmail: {mijoz['email']} \
#   Telefon: {mijoz['telefon']}")

# 3

# def kattasini_chiqar(x,y,z):
#     """ 3 ta sondan kattasini chiqaruvchi funksiya """
#     max=x
#     if y>max:
#         max=y
#     if z>max:
#         max=z
   
#     return max

# print(kattasini_chiqar(16,17,18))

# 4

# def aylana_hisobla(radius):
#     """Aylaning radiusini qabul qilib olib, uning radiusini, 
#     diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya"""
#     PI = 3.14159
#     aylana = {"Radius":radius,
#               "Diametr":2*radius,
#               "Uzunligi":2*PI*radius,
#               "Yuzi":PI*radius**2}
#     return aylana
# print(aylana_hisobla(3))

# 5

# def tub_sonlar_topish(min,max):
#     """Berilgan sonlar oralig'idagi tub sonlarni topish funksiyasi"""
#     tub_sonlar=[]
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub=False
#         elif (n==2):
#             tub=True
#         else:
#             for x in range(2,n):
#                 if (n%x==0):
#                     tub=False
#         if tub:
#             tub_sonlar.append(n)      
#     return tub_sonlar

# print(tub_sonlar_topish(2,100))
    
# 6

def fibonachi_son_topish(son):
    """Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya"""
    fibonachi_son=[]
    for x in range(son):
        if x==0 or x==1:
            fibonachi_son.append(1)
        else:
            fibonachi_son.append(fibonachi_son[x-1]+fibonachi_son[x-2])
    return fibonachi_son

print(fibonachi_son_topish(4))
    
    
    
    
    
    
    
    