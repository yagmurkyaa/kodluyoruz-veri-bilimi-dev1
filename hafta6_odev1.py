#!/usr/bin/env python
# coding: utf-8

# ### Ödev 1
# 
# Bir sözlük oluşturulur ve bu sözlükte öğrencilerin isimleri ve Matematik, Fizik, Kimya notları tutulur. Kullanıcıdan isim ve ders ismi(Matematik, Fizik, Kimya) istenir ve bu bilgilere göre çıktı verilir.

# In[1]:



ogrenciler = {
    "yağmur": {"Matematik": 90, "Fizik": 85, "Kimya": 70},
    "beyza": {"Matematik": 95, "Fizik": 80, "Kimya": 75},
    "aleyna": {"Matematik": 85, "Fizik": 75, "Kimya": 80}
}


ogrenci_isim = input("Öğrenci adını giriniz (yağmur, beyza, aleyna): ")
ders_isim = input("Ders adını giriniz (Matematik, Fizik, Kimya): ")

if ogrenci_isim in ogrenciler and ders_isim in ogrenciler[ogrenci_isim]:
    notu = ogrenciler[ogrenci_isim][ders_isim]
    print(f"{ogrenci_isim.capitalize()} öğrencisinin {ders_isim} dersinden aldığı not: {notu}")
else:
    print("Hatalı giriş! Lütfen geçerli bir öğrenci adı ve ders adı giriniz.")


# ### Ödev 2
# 
# Sözlük üzerinde değerleri değiştirme, yeni değer ekleme, kullanıcıya ulaşmak istediği bilgileri sorma gibi uygulamalar yapın.

# In[ ]:


ogrenciler = {
    "yağmur": {"Matematik": 90, "Fizik": 85, "Kimya": 70},
    "beyza": {"Matematik": 95, "Fizik": 80, "Kimya": 75},
    "aleyna": {"Matematik": 85, "Fizik": 75, "Kimya": 80}
}

def degerleri_degistir():
    ogrenci = input("Bilgilerini değiştirmek istediğiniz öğrencinin adını giriniz: ")
    if ogrenci in ogrenciler:
        print(f"{ogrenci.capitalize()} öğrencisinin mevcut bilgileri: {ogrenciler[ogrenci]}")
        ders = input("Değerini değiştirmek istediğiniz dersin adını giriniz: ")
        if ders in ogrenciler[ogrenci]:
            yeni_not = int(input(f"Yeni {ders} notunu giriniz: "))
            ogrenciler[ogrenci][ders] = yeni_not
            print(f"{ogrenci.capitalize()} öğrencisinin {ders} dersi notu güncellendi.")
        else:
            print("Hatalı giriş! Lütfen geçerli bir ders adı giriniz.")
    else:
        print("Hatalı giriş! Bu isimde bir öğrenci bulunmamaktadır.")

def yeni_deger_ekle():
    ogrenci = input("Yeni öğrencinin adını giriniz: ")
    if ogrenci not in ogrenciler:
        ogrenci_bilgileri = {}
        for ders in ["Matematik", "Fizik", "Kimya"]:
            notu = int(input(f"{ders} notunu giriniz: "))
            ogrenci_bilgileri[ders] = notu
        ogrenciler[ogrenci] = ogrenci_bilgileri
        print(f"{ogrenci.capitalize()} öğrencisinin bilgileri eklendi.")
    else:
        print("Hatalı giriş! Bu isimde bir öğrenci zaten bulunmaktadır.")

def bilgi_istegi():
    ogrenci = input("Bilgi almak istediğiniz öğrencinin adını giriniz: ")
    if ogrenci in ogrenciler:
        ders = input("Hangi dersin notunu öğrenmek istiyorsunuz? (Matematik, Fizik, Kimya): ")
        if ders in ogrenciler[ogrenci]:
            print(f"{ogrenci.capitalize()} öğrencisinin {ders} dersi notu: {ogrenciler[ogrenci][ders]}")
        else:
            print("Hatalı giriş! Bu öğrencinin belirttiğiniz dersine ait bir not bulunmamaktadır.")
    else:
        print("Hatalı giriş! Bu isimde bir öğrenci bulunmamaktadır.")


while True:
    print("\n1. Öğrenci bilgilerini değiştirme")
    print("2. Yeni öğrenci ve bilgileri ekleme")
    print("3. Bilgi isteği")
    print("4. Çıkış")
    secim = input("Lütfen yapmak istediğiniz işlemi seçiniz (1/2/3/4): ")

    if secim == "1":
        degerleri_degistir()
    elif secim == "2":
        yeni_deger_ekle()
    elif secim == "3":
        bilgi_istegi()
    elif secim == "4":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Hatalı giriş! Lütfen geçerli bir seçenek giriniz.")


# In[ ]:




