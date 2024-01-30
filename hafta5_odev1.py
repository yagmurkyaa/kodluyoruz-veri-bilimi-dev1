#!/usr/bin/env python
# coding: utf-8

# #### Ödev 1
# Kullanıcıdan pi değeri ve yarıçap bilgisi alarak dairenin alanını hesaplayan bir fonksiyon oluşturulur.

# In[1]:


def dairenin_alani_hesapla():
    pi = float(input("Lütfen pi değerini girin: "))
    yaricap = float(input("Lütfen dairenin yarıçapını girin: "))
    alan = pi * (yaricap ** 2)
    return alan

# Fonksiyonu çağırarak dairenin alanını hesapla ve ekrana yazdır
sonuc = dairenin_alani_hesapla()
print(f"Dairenin alanı: {sonuc}")


# #### Ödev 2
# 
# Faktöriyel adında fonksiyon oluşturulur. Döngü kullanarak parametre olarak girilen sayının faktöriyeli hesaplanır. Format metodunu kullanılarak ekrana yazdırılır.

# In[2]:


def faktoriyel_hesapla(sayi):
    faktoriyel = 1
    for i in range(1, sayi + 1):
        faktoriyel *= i
    return faktoriyel

girilen_sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))
sonuc = faktoriyel_hesapla(girilen_sayi)

print("{} sayısının faktöriyeli: {}".format(girilen_sayi, sonuc))


# #### Ödev 3
# Kişinin fonksiyona doğum yılını vererek kaç yaşında olduğunu hesaplayan bir fonksiyon oluşturun. 

# In[3]:


def yas_hesapla(dogum_yili):
    current_year = 2024 
    yas = current_year - dogum_yili
    return yas

dogum_yili_kullanici = int(input("Lütfen doğum yılınızı girin: "))
yas_kullanici = yas_hesapla(dogum_yili_kullanici)

print("Siz {} yaşındasınız.".format(yas_kullanici))


# #### Ödev 4
# 
# Doğum yılı ve isim bilgisi verilen fonksiyon kişinin emekli olup olmadığını söylesin.(Kişi 65 yaşında ise emekli olur.) Burada yaş hesabını yukarıdaki örnekteki fonksiyonu kullanarak yapsın.(Yani fonksiyon içinde fonksiyon kullanmanızı istiyorum :)) Kişi 65 yaşında ya da daha fazlaysa "Emekli oldunuz" yanıtını, 65 yaşından küçükse emekliliğine kaç yıl kaldığını da hesaplayarak "(isim) emekliliğine (yıl) kaldı." yanıtını versin.

# In[4]:


def emeklilik_durumu(isim, dogum_yili):
    def yas_hesapla(dogum_yili):
        current_year = 2024  
        yas = current_year - dogum_yili
        return yas

    yas_kullanici = yas_hesapla(dogum_yili)

    if yas_kullanici >= 65:
        print(f"{isim}, emekli oldunuz.")
    else:
        kalan_yil = 65 - yas_kullanici
        print(f"{isim}, emekliliğinize {kalan_yil} yıl kaldı.")

isim_kullanici = input("Lütfen isminizi girin: ")
dogum_yili_kullanici = int(input("Lütfen doğum yılınızı girin: "))
emeklilik_durumu(isim_kullanici, dogum_yili_kullanici)


# In[ ]:




