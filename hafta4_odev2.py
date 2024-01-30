
# **Ödev-1:** Kullanıcıdan maaş bilgisini istenir ve bu bilgiye göre maaşından ne kadar vergi kesileceğini hesaplanır. Kullanıcının geliri;
# 
# 1. 10000 ve altındaysa maaşından %5 kesinti olur.
# 2. 25000 ve altındaysa maaşından %10 kesinti olur.
# 3. 45000 ve altındaysa maaşından %25 kesinti olur.
# 4. Diğer koşullarda %30 kesinti olur.
# 
# Bu durumlara göre kullanıcının yeni maaşı yazdırılır.

maas = float(input("Maaşınızı giriniz: "))

# Vergi oranlarını belirlenmesi
if maas <= 10000:
    vergi_orani = 0.05
elif maas <= 25000:
    vergi_orani = 0.10
elif maas <= 45000:
    vergi_orani = 0.25
else:
    vergi_orani = 0.30

# Vergi hesaplanır ve yeni maaşı bulunur
kesilecek_vergi = maas * vergi_orani
yeni_maas = maas - kesilecek_vergi

# Sonucu yazdır
print("Maaşınızdan kesilen vergi:" , kesilecek_vergi)
print("Yeni maaşınız: " ,  yeni_maas)


# **Ödev-2:** Kullanıcıdan kullanıcı adı ve şifre oluşturmasını istenir. Şifrenin uzunluğu altı haneye ulaşmışsa hesabınız oluşturuldu mesajı alınır, altı haneden azsa altı haneli şifre oluşturması gerektiğinin mesajı alınır. *(Sadece koşul kullanılması yeterli.)*

# Kullanıcıdan kullanıcı adı ve şifre bilgilerini al
kullanici_adi = input("Kullanıcı adınızı giriniz: ")
sifre = input("Şifrenizi belirleyiniz: ")

# Şifre uzunluğunu kontrol et
if len(sifre) >= 6:
    print("Hesabınız oluşturuldu!")
else:
    print("Şifreniz en az altı karakter uzunluğunda olmalıdır. Lütfen geçerli bir şifre belirleyiniz.")


# **Ödev-3:** Bir önceki örnek geliştirilir.
# 
# 1. Kullanıcı girdiği şifre 5 ve 10 hane arasında olmak zorunda.
# 2. Eğer bu koşula uyuyorsa "Hesabınız oluşturuldu." mesajı alır.
# 3. Koşulu sağlamıyorsa "Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!" uyarısı alır.
# 4. Bunu oluştururken kullanıcı istediğimiz şartlarda şifre oluşturana kadar sormaya devam eder


while True:
    # Kullanıcıdan kullanıcı adı ve şifre bilgisini al
    kullanici_adi= input( "Lütfen kullanıcı adı giriniz: ")
    sifre = input("Lütfen şifrenizi belirleyiniz (5-10 karakter arası): ")

    # Şifre uzunluğunu kontrol et
    if 5 <= len(sifre) <= 10:
        print("Hesabınız oluşturuldu!")
        break  # Doğru şifre girildiyse döngüden çık
    else:
        print("Lütfen girdiğiniz şifre 5 haneden az, 10 haneden fazla olmasın! Tekrar deneyiniz.")


# **Ödev-4:** Kullanıcıdan isim ve şifre isteyeceğiz ve şifre girişi için üç hak verilir.
# 
# 1. Eğer önceden tanımlı şifre ile kullanıcıdan gelen şifre aynıysa "Giriş yapıldı." yazar.
# 2. Şifre girişi yanlışsa "Yanlış şifre girildi!" uyarısı verilsin ve üç yanlış denemede program biter.
# 3. Tercihe göre kalan hak bilgisi verilir.

# Önceden tanımlı kullanıcı adı ve şifre
dogru_kullanici_adi = "kullanici"
dogru_sifre = "sifre123"

hak_sayisi = 3

while hak_sayisi > 0:
    # Kullanıcıdan isim ve şifre istenir
    kullanici_adi = input("Kullanıcı adınızı giriniz: ")
    sifre = input("Şifrenizi giriniz: ")

    # Şifre kontrolü
    if kullanici_adi == dogru_kullanici_adi and sifre == dogru_sifre:
        print("Giriş yapıldı.")
        break
    else:
        hak_sayisi -= 1
        if hak_sayisi > 0:
            print(f"Yanlış şifre girildi! Kalan hakkınız: {hak_sayisi}")
        else:
            print("Üç kez yanlış şifre girişi yapıldı. Program sonlandırılıyor.")
