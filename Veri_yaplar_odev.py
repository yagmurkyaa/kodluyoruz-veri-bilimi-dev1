#!/usr/bin/env python
# coding: utf-8

# # 1
# x = 3 ----> floata çevirelim. Çevirdikten sonra beri tipinide yazdıralım.
# 
# y = 4.5 -----> integere çevirelim. Çevirdikten sonra beri tipinide yazdıralım.
# 
# z = "8" -----> integera çevirelim. Çevirdikten sonra beri tipinide yazdıralım.
# 
# a = "12" -----> floata çevirelim. Çevirdikten sonra beri tipinide yazdıralım.
# 
# b = "46.8" ------> integera çevirelim. Çevirdikten sonra beri tipinide yazdıralım.

# In[9]:


x=3


# In[10]:


x=float(x)


# In[11]:


print(x)


# In[12]:


print(type(x))


# In[13]:


y=4.5


# In[14]:


y=int(y)


# In[15]:


print(y)


# In[16]:


print(type(y))


# In[17]:


z="8"


# In[18]:


z=int(z)


# In[19]:


print(z)


# In[20]:


print(type(z))


# In[21]:


a="12"


# In[22]:


a=float(a)


# In[23]:


print(a)


# In[24]:


print(type(a))


# In[25]:


b="46.8"


# In[26]:


b=int(float(b))


# In[27]:


print(b)


# In[28]:


print(type(b))


# # 2 
# İsimlerden oluşan üç değişkene yaş değerleri atanır. Belirlenen üç değişken birbiriyle karşılaştırma operatörleri ile karşılaştırılır. Bu karşılaştırmalara mantıksal operatörler de eklenir.

# In[29]:


ali_yasi = 25
ayse_yasi = 30
mehmet_yasi = 28


# In[30]:


25==30


# In[31]:


28==30


# In[33]:


25!=30


# In[34]:


28>25


# In[35]:


30>=25


# In[36]:


25 <28 and 30> 25


# In[37]:


28 < 25 or 30 < 28


# In[38]:


not ((30 < 25 ) or (28> 25))


# # 3
# Kullanıcıdan iki değer girmesini istenir. Girilen değerlerin toplama, çıkarma, çarpma, bölme sonuçlarını yazdırılır.

# In[8]:


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

# In[14]:


isim = input("Adınız:")


# In[15]:


isim


# In[1]:


age = input("Yaşiniz: ")
print(age)


# In[2]:


sehir= input ("sehriniz: ")
print(sehir)


# In[3]:


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

# In[4]:


atolye_adı = "Hi-Kod Veri Bilimi Atölyesi"


# In[5]:


print(atolye_adı)


# In[6]:


atolye_adı = "Hi-Kod Veri Bilimi Atölyesi"


kelimeler = atolye_adı.split()


kelime1, kelime2, kelime3, kelime4 = kelimeler

print("1. Kelime:", kelime1)
print("2. Kelime:", kelime2)
print("3. Kelime:", kelime3)
print("4. Kelime:", kelime4)


# In[7]:


atolye_adı = "Hi-Kod Veri Bilimi Atölyesi"

buyuk_harf_atolye_adı = atolye_adı.upper()

print(buyuk_harf_atolye_adı)


# In[8]:


atolye_adı = "Hi-Kod Veri Bilimi Atölyesi"


kucuk_harf_atolye_adı = atolye_adı.lower()


print(kucuk_harf_atolye_adı)


# In[9]:


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


# In[ ]:




