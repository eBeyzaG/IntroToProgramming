def x_sil_ve_ekrana_yaz(x_li_yazi):
    print("Fonksiyona girildi.")
    duzenlenmis_yazi = ""
    for karakter in x_li_yazi:
        if not karakter == "x":
            duzenlenmis_yazi += karakter
    print(duzenlenmis_yazi)

#txt = "Pazardanx xelma aldımx."
#txt2 = "xBugün çokx güzxel bir gün."
#x_sil_ve_ekrana_yaz(txt2)

#faktoriyel alan fonksiyon
def faktoriyel(sayi):
    sonuc = 1
    for i in range(1, sayi + 1):
        sonuc *= i
    return sonuc

#sayi = 8
#faktoriyel_sonuc = faktoriyel(sayi)
#print(sayi, "! =", faktoriyel_sonuc)

def merhaba_de():
    print("Merhaba")
    print("Tanıştğıma memnun oldum")
    while True:
        pass


def urun_var_mi(urun_adi, alisveris_dictionary):
    urun_bulundu_mu = False

    for urun_turu, urun_listesi in alisveris_dictionary.items():
        if urun_adi in urun_listesi:
            urun_bulundu_mu = True
    
    return urun_bulundu_mu

        

alisveris_dict = {
    "meyveler" : ["muz", "çilek"],
    "sebzeler" : ["kabak", "patlıcan"]
}

#parametre isimleri verilmediğinde argümanlar sıralı verilmek zorundadır
#sonuc = urun_var_mi("muz", alisveris_dict)

#sırasız argüman vermek için, parametre isimleri yazılmak zorunaddır
#sonuc = urun_var_mi(alisveris_dictionary=alisveris_dict, urun_adi="muz")

#sonuc = urun_var_mi("çikolata", alisveris_dict)
#if sonuc:
#    print("Bu ürün listede mevcut")
#else:
#    print("Bu ürün listede mevcut değil")


#verilen sayı listesini toplayarak sonucu döndürür

#varsayılan değeri olmayan parametreler varsayılan değeri olan parametrelere göre
#daha önce yazılır
def sayilari_topla(sayilar, ilk_deger=0):

    for sayi in sayilar:
        ilk_deger += sayi
    
    return ilk_deger

#sayi_listesi = [1, 2, 3]
#sonuc = sayilari_topla(sayi_listesi)
#print(sonuc)

def sayilari_topla(sayi_listesi):
    sonuc = 0
    for sayi in sayi_listesi:
        sonuc += sayi
    return sonuc

def ortalama_hesapla(sayi_listesi):
    #sayilari topla
    sayilar_toplami = sayilari_topla(sayi_listesi)

    return sayilar_toplami / len(sayi_listesi)

#sayilar = [1, 3, 5, 7]
#print(ortalama_hesapla(sayilar)) 
'''
sayi = 10

def sayi_bastir():
    sayi = 5 
    print("fonksiyondaki sayı:", sayi)


print("normal sayı", sayi)
sayi_bastir()
sayi = 15
print("normal sayi", sayi)
sayi_bastir()


def degistir(a):
    a += 5
    print("fonksiyon:", a)

b = 7 
degistir(b)
print(b)

def liste_degistir(liste):
    liste.append(4)

b = [1, 2, 3]
liste_degistir(b)
print(b)

'''

#UYGULAMA
#kullanıcıdan isim alsın (fonksiyonda değil)
# bu ismi kullanarak "merhaba isim" yazan fonksiyon
def merhaba_de(isim):
    print("Merhaba", isim)


#isim = input("İsminizi giriniz.")
#merhaba_de(isim)

#listedeki en büyük elemanı döndüren fonksiyon
#parametre: sayi listesi
#return değeri: en büyük sayi

def en_buyuk_deger_bul(sayi_listesi):
    #listenin başından sonuna kadar tüm sayıları gez
    # o ana kadarki en büyük sayıyı sakla
    # eğer ki elimdeki sayıdan daha büyük bir sayı çıkarsa
    # en büyük elemanı güncelle

    en_buyuk_sayi = sayi_listesi[0]
    for sayi in sayi_listesi:
        if en_buyuk_sayi < sayi:
            en_buyuk_sayi = sayi
    return en_buyuk_sayi

sayilar = [12, 43, 65, 78, 100]
print(en_buyuk_deger_bul(sayilar))