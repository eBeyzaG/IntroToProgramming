'''
Fizz Buzz:
0 ile 100 arasındaki sayılar için
Sayı 3 ile bölünüyorsa ekrana “Fizz” yazdır
Sayı 5 ile bölünüyorsa ekrana “Buzz” yazdır
İkisine de bölünüyorsa “Fizz Buzz” yazdır


for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "Fizz Buzz")
    elif i % 3 == 0: #3 ile bölünebilir
        print(i, "Fizz")
    elif i % 5 == 0: #5 ile bölünebilir
        print(i, "Buzz")
    else: 
        print(i)
'''
# KÜTÜPHANE SİSTEMİ

#kullanıcı = kütüphane görevlisi
#ÖZELLİKLER
# - yeni kitap ekle
# - kitapları listele
# - kitap düzenle
# - kitap sil

# kütüphane : dictionary key: kitap ID value: dictionary{kitapadi: , yazar:, sayfaSayisi, yayınevi }

kitap_ID = 4
kutuphane = {
    1 : {
        "kitapAdi" : "Simyacı",
        "yazarlar" : ["Paulo Coelho", "James A"],
        "sayfaSayisi" : 184,
        "yayınevi" : "Can Yayınevi"
    },
    2 : {
        "kitapAdi" : "Fareler ve İnsanlar",
        "yazarlar" : ["John Steinback"],
        "sayfaSayisi" : 111,
        "yayınevi" : "Sel Yayıncılık"
    },
    3  : {
        "kitapAdi" : "Simyacı",
        "yazarlar" : ["John "],
        "sayfaSayisi" : 131,
        "yayınevi" : "Sel Yayıncılık"
    }
}
while True:
    islem_no = input("Hoş Geldiniz. Hangi işlemi yapmak istersiniz?\n" +
        "1) Yeni Kitap Ekle\n" +
        "2) Kitapları Listele\n" +
        "3) Kitap Düzenle\n" +
        "4) Kitap Sil\n" +
        "5) Kitap Adıyla ID Bul\n"
        "6) Çıkış\n"
    )
    if islem_no == "1": #yeni kitap ekle
        kitap_adi = input("Kitap adını giriniz\n")
        yazarlar = input("Yazarları virgül ',' ile ayırarak giriniz\n")
        yazarlarListesi = yazarlar.split(",")
        #split metodu verilen karakterden bölerek list oluşturur "a,b,c" => ["a","b","c"]
        sayfaSayisi = int(input("Sayfa sayısını giriniz\n"))
        yayinevi = input("Yayınevini giriniz\n")

        kutuphane[kitap_ID] = {
            "kitapAdi" : kitap_adi,
            "yazarlar" : yazarlarListesi,
            "sayfaSayisi" : sayfaSayisi,
            "yayınevi" : yayinevi
        }
        kitap_ID += 1
        print("Kitap başarıyla eklendi.")

    elif islem_no == "2": #kitapları listele
        for id, kitap in kutuphane.items():
            print("ID:", id)
            print("Kitabın Adı:", kitap["kitapAdi"])
            print("Yazarlar:")
            for yazar in kitap["yazarlar"]:
                print("-", yazar)
            print("Sayfa Sayısı:", kitap["sayfaSayisi"])
            print("Yayınevi:", kitap["yayınevi"])
            print("------------------------------------")

    elif islem_no == "3": #kitap düzenle
        duzenlenecek_kitap_id = int(input("Düzenlemek istediğiniz kitabın ID'sini  giriniz."))
        
        # a = [0, 1, 2, 3] if 1 in a:

        #bu id'ye sahip bir kitap yoksa hata
        if duzenlenecek_kitap_id not in kutuphane:
            print(duzenlenecek_kitap_id, "ID'sine sahip bir kitap bulunmamaktadır.")
            continue

        #kitabı düzenle 
        # kitabın değiştirilen özelliklerini kullanıcıdan al       
        kitap_adi = input("Kitap adını giriniz\n")
        yazarlar = input("Yazarları virgül ',' ile ayırarak giriniz\n")
        yazarlarListesi = yazarlar.split(",")
        sayfaSayisi = int(input("Sayfa sayısını giriniz\n"))
        yayinevi = input("Yayınevini giriniz\n")

        #dict'i güncelle
        kutuphane.update({
            duzenlenecek_kitap_id : {
                "kitapAdi" : kitap_adi,
                "yazarlar": yazarlarListesi,
                "sayfaSayisi": sayfaSayisi,
                "yayınevi": yayinevi

            }
        })
        print(duzenlenecek_kitap_id," ID'li kitabın bilgileri güncellendi.")
    elif islem_no == "4": #kitap sil:
        silinecek_kitap_id = int(input("Silmek istediğiniz kitabın ID'sini giriniz\n"))

        if silinecek_kitap_id not in kutuphane:
            print(silinecek_kitap_id, "ID'sine sahip kitap bulunumamaktadır.")
            continue

        #sil
        kutuphane.pop(silinecek_kitap_id)
        print("Kitap başarıyla silindi.")
    elif islem_no == "5": #kitap adı ile id bul
        
        aranan_kitap_adi = input("Aradığınız kitabın adını giriniz\n")
        kitap_bulundu_mu = False

        for id, kitap in kutuphane.items():
            if kitap["kitapAdi"] == aranan_kitap_adi:
                print("ID:", id)
                print("Kitap Adı", kitap["kitapAdi"])
                print("Yazarlar:\n")
                for yazar in kitap["yazarlar"]:
                    print("-", yazar)
                print("Sayfa Sayısı:", kitap["sayfaSayisi"])
                print("Yayınevi:", kitap["yayınevi"])
                kitap_bulundu_mu = True
        
        if not kitap_bulundu_mu: #kitap listede yoksa
            print(aranan_kitap_adi, "ismine sahip bir kitap bulunamadı.")
    
    
    elif islem_no == "6": #çıkış
        break
    else:
        print("Hatalı işlem seçtiniz.")