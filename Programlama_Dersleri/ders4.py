'''
Ödev
{“yazar1”: [“kitap1”, “kitap2”], “yazar2”: [”kitap1”]} yapısında bir dictionary oluştur.

Ahmet Hamdi Tanpınar: 
	Mahur Beste
	Huzur
	Sahnenin Dışındakiler
	Saatleri Ayarlama Enstitüsü
Orhan Pamuk:
	Sessiz Ev
	Beyaz Kale
Oğuz Atay:
	Tutunamayanlar
	Tehlikeli Oyunlar


yazarlar_dict = {
    "Ahmet Hamdi Tanpınar" : [
        "Mahur Beste",
        "Huzur",
        "Sahnenin Dışındakiler",
        "Saatleri Ayarlama Enstitüsü"
    ],
    "Orhan Pamuk" : [
        "Sessiz Ev",
	    "Beyaz Kale"
    ],
    "Oğuz Atay" : [
        "Tutunamayanlar",
	    "Tehlikeli Oyunlar"
    ]
}
print(yazarlar_dict["Oğuz Atay"])
'''
'''
# IF ELSE İFADELERİ

a = 7
# boolean değişken
aBesMi = False

if aBesMi:
    print("a sayısı 5'tir.")
else:
    print("a sayısı 5 değildir.")

print("Merhaba")


isim = input("İsminizi giriniz.")

# elif = else if
if isim == "beyza":
    print("Merhaba Beyza")
    print("Tanıştığıma memnun oldum.")
elif isim == "ayşe":
    print("Merhaba Ayşe")
    print("Ayşe çok güzel bir isim.")
elif isim == "ahmet":
    print("Merhaba Ahmet")
else:
    print("Merhaba")

# İFADE BİRLEŞTİRME

#yaşa göre sınıflandırma
# 0-3 => bebek
# 3-15 => çocuk
# 15-30 => genç
# 30- => yetişkin

yas = int(input("Yaşınızı giriniz."))

if 0 <= yas and yas <= 3:
    print("Bebek")
elif 3 < yas and yas <= 15:
    print("Çocuk")
elif 15 < yas and yas <= 30:
    print("Genç")
elif 30 < yas:
    print("Yetişkin")
else: 
    print("Hatalı yaş girdiniz.")


#kullanıcıdan isim alınır
#ilk harfi a ya da e olanlar bildir
#ilk harfi b ve de ikinci harfi e olanlara bildir

# "beyza" = ['b', 'e', 'y', 'z', 'a']

kullanici_ismi = input("Adınızı giriniz.")

if kullanici_ismi[0] == "a" or kullanici_ismi[0] == "e":
    print("İsminiz a ya da e ile başlıyor")

if kullanici_ismi[0] == "b" and kullanici_ismi[1] == "e":
    print("İsminiz 'be' ile başlıyor")


# nested if

musteri_istegi = input("içecek mi istersiniz yiyecek mi?")

if musteri_istegi == "içecek":
    musteri_icecegi = input("kola mı isterseniz ayran mı?")
    if musteri_icecegi == "kola":
        print("Kolanız hemen geliyor.")
    elif musteri_icecegi == "ayran":
        print("Ayranınız hemen geliyor.")
    else:
        print("Menümüzde böyle bir içecek bulunmamaktadır.")
elif musteri_istegi == "yiyecek":
    musteri_yiyecegi = input("makarna mı isteriniz çorba mı yoksa ikisi de mi?")
    if musteri_yiyecegi == "makarna":
        print("Makarnanız hemen geliyor.")
    elif musteri_yiyecegi == "çorba":
        print("Çorbanız hemen geliyor.")
    elif musteri_yiyecegi == "ikisi de":
        print("Çorba ve makarnanız geliyor.")
    else:
        print("Menümüzde böyle bir yiyecek yoktur.")
else:
    print("Menümüzde sadece yiyecek ve içecek mevcuttur.")


#sayi tahmini
# gerçek sayi = 7
# kullanıcıdan sayı al
# eşit mi daha mı büyük daha mı küçük kontrol et

gercek_sayi = 7
kullanici_tahmini = int(input("Tahmininizi giriniz."))

if kullanici_tahmini == gercek_sayi:
    print("Tebrikler doğru bildiniz!")
elif kullanici_tahmini > gercek_sayi:
    print("Daha büyük bir sayı tahmin ettiniz... Gerçek sayı:", gercek_sayi)
else:
    print("Daha küçük bir sayı tahmin ettiniz... Gerçek sayı:", gercek_sayi)
'''
# kullanıcıdan iki sayi al
# kullanıcıya işlem seçtir
# seçilen işlemi yap ve sonucu bastır

sayi_1 = float(input("İlk sayınızı giriniz"))
sayi_2 = float(input("İkinci sayınızı giriniz."))
islem_no = int(input("Yapmak istediğiniz işlemi seçiniz.\n1) Toplama\n2) Çıkarma\n3) Çarpma\n4) Bölme\n5) Mod alma"))

if islem_no == 1: #toplama
    sonuc = sayi_1 + sayi_2
    print(sayi_1, "+", sayi_2, "=", sonuc)
elif islem_no == 2: #çıkarma
    sonuc = sayi_1 - sayi_2
    print(sayi_1, "-", sayi_2, "=", sonuc)
elif islem_no == 3: #çarpma
    sonuc = sayi_1 * sayi_2
    print(sayi_1, "*", sayi_2, "=", sonuc)
elif islem_no == 4: #bölme
    sonuc = sayi_1 / sayi_2
    print(sayi_1, "/", sayi_2, "=", sonuc )
elif islem_no == 5: #mod alma
    sonuc = sayi_1 % sayi_2
    print(sayi_1, "%", sayi_2, "=", sonuc)
else:
    print("Hatalı işlem seçtiniz.")


#ÖDEV
# BÖLME VE MOD ALMA ÖZELLİKLERİNİ EKLEYİN hatalı durumları da kontrol edin