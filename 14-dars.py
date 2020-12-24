# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:34:03 2020

@author: OsiyoComputers™
"""

# 1

# men = {"ism familya":"javharbek yuldashev","yil":2001,"viloyat":"farg'ona"}
# print(f"Men, {men['ism familya'].title()}, {men['yil']}-yilda {men['viloyat'].title()} viloyatida tug'ilganman")

# 2

# ovqatlar = {'otam':'bosma', 'onam':'osh', 'opam':'shashlik', 'singlim':'lavash', "man":'manti'}
# print(f"Otamning sevimli taomi: {ovqatlar['otam'].title()}")
# print(f"Onamning sevimli taomi: {ovqatlar['onam'].title()}")
# print(f"O\'ziming sevimli taomim: {ovqatlar['man'].title()}")

# 3

atamalar = {
    "str":"matn",
    "int":"butun son", 
    "float":"o'nlik son", 
    "for":"uchun", 
    "in":"da", 
    "if":"agar", 
    "else":"aks holda",
    "list":"ro'yhat",
    "tuple":"o'zgarmas",
    "function":"funksiya",
    "dictonary":"lug'at"
    }

# a)
atama = input("Kalit so'z kiriting: ").lower()
print(atamalar.get(atama,"Bunday atama mavjud emas"))

# b)
atama = input("Kalit so'z kiriting: ").lower()
tarjima = atamalar.get(atama)
if tarjima == None:
    print("Bunday atama mavjud emas")
else:
    print(f"{atama.title()} atamasining tarjimasi - {tarjima}")












