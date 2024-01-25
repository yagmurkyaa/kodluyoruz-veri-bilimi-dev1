#!/usr/bin/env python
# coding: utf-8

Soru 1
# x = 3 ----> floata çevirelim. Çevirdikten sonra veri tipinide yazdıralım.
# 
# y = 4.5 -----> integere çevirelim. Çevirdikten sonra veri tipinide yazdıralım.
# 
# z = "8" -----> integera çevirelim. Çevirdikten sonra veri tipinide yazdıralım.
# 
# a = "12" -----> floata çevirelim. Çevirdikten sonra veri tipinide yazdıralım.
# 
# b = "46.8" ------> integera çevirelim. Çevirdikten sonra veri tipini de yazdıralım.

# In[9]:


x=3
x=float(x)
print(x)
print(type(x))

y=4.5
y=int(y)
print(y)
print(type(y))

z="8"
z=int(z)
print(z)
print(type(z))

a="12"
a=float(a)
print(a)
print(type(a))

b="46.8"
b=int(float(b))
print(b)
print(type(b))


# # 2 
# İsimlerden oluşan üç değişkene yaş değerleri atanır. Belirlenen üç değişken birbiriyle karşılaştırma operatörleri ile karşılaştırılır. Bu karşılaştırmalara mantıksal operatörler de eklenir.


ali_yasi = 25
ayse_yasi = 30
mehmet_yasi = 28

25==30
28==30
if ali_yasi < ayse_yasi:
    print(True)
else:
    print(False)
if ayseyasi < 35:
    print(True)
25!=30
28>25
30>=25

25 <28 and 30> 25
28 < 25 or 30 < 28
not ((30 < 25 ) or (28> 25))


# # 3
# Kullanıcıdan iki değer girmesini istenir. Girilen değerlerin toplama, çıkarma, çarpma, bölme sonuçlarını yazdırılır.


sayi1 = int(input("1. Sayıyı giriniz = "))
sayi2 = int(input("1. Sayıyı giriniz = "))

toplama = sayi1+sayi2
print(toplama)
cikarma = sayi1-sayi2
print(cikarma)
carpma= sayi1*sayi2
print(carpma)
if sayi2 != 0:  # Bölen sıfır olmamalı
    bolum = sayi1 / sayi2
    print(f"{sayi1} / {sayi2} = {bolum}")
else:
    print("Bölme işlemi için ikinci sayı sıfır olamaz.")


# # 4
# Kullanıcıdan isim, yaş, şehir ve meslek bilgilerini istenir ve cevaplarını yazdırılır.

isim = input("Adınız:")
isim

age = input("Yaşiniz: ")
print(age)

sehir= input ("sehriniz: ")
print(sehir)

meslek= input("mesleginiz: ")
print(meslek)


# # 5
# "Hi-Kod Veri Bilimi Atölyesi" ifadesini bir değişkene tanımlanır.
# 
# 
#  1. İfadedeki her bir kelimeyi ("Hi-Kod", "Veri", "Bilimi", "Atölyesi") değişken içinden seçilir. 
#  2. İfadeyi hepsini büyük harf olacak hale çevrilir. ("HI-KOD VERİ BİLİMİ ATÖLYESİ") 
#  3. İfadeyi hepsini küçük harf olacak hale çevrilir.("hi-kod veri bilimi atölyesi") 
# 
# "0123456789" ifadesindeki yalnızca çift sayıları ve yalnızca tek sayıları seçilir. ("02468", "13579")



atolye_ismi = "Hi-Kod Veri Bilimi Atölyesi"
print(atolye_ismi)

#1.ifadedeki her bir kelime değişken içinden seçilir.

atolye_ismi = "Hi-Kod Veri Bilimi Atölyesi"
kelimeler = atolye_ismi.split()

# 2.ifadedeki harflerin hepsini büyük harfe çevir

atolye_ismi = "Hi-Kod Veri Bilimi Atölyesi"
buyuk_harf_atolye_ismi = atolye_ismi.upper()
print(buyuk_harf_atolye_ismi)

# 3.ifadedeki harflerin hepsini küçük harfe çevir.

atolye_ismi = "Hi-Kod Veri Bilimi Atölyesi"
kucuk_harf_atolye_ismi = atolye_ismi.lower()
print(kucuk_harf_atolye_ismi)

# "0123456789" ifadesindeki yalnızca çift sayıları ve yalnızca tek sayıları seçilir. ("02468", "13579")

sayi_ifadesi = "0123456789"

cift_sayilar = ""
tek_sayilar = ""

for rakam in sayi_ifadesi:
    if int(rakam) % 2 == 0:
        cift_sayilar += rakam
    else:
        tek_sayilar += rakam

print("Çift Sayılar:", cift_sayilar)
print("Tek Sayılar:", tek_sayilar)


