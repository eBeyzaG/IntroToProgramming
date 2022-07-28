#ÖDEV
#parametre olarak aldığı sayının çift mi tek mi olduğunu string olarak döndüren fonksiyon
'''
def cift_mi_tek_mi(sayi):
    if sayi % 2 == 0:#çift mi
        return "çift"
    else:
        return "tek"

print(cift_mi_tek_mi(8))
'''

#ADAM ASMACA

# 1) Program rastgele bir kelime seçer
# 2) Kullanıcı alfabedeki harflerden harf tahmin eder
# 3) Eğer bu harf kelimede mevcutsa devam eder
#   eğer mevcut değilse tahmin hakkı kaybeder adam asılmaya yaklaşır
# 4) Kullanıcı tüm harfleri doğru tahmin ettiyse o kelime tamamlanmış olur 
# ve kullanıcı kazanır
# 5) kullanıcının tahmin hakkı biter ve kaybeder

import random

#tireler arasına boşluk koyar
def print_tahmin_edilen_kelime(kelime):
    for tire in kelime:
        #her tireden sonra satır atlamaması için end="" yazılır
        print(tire + " ", end="")
    
    #tüm tireleri yazdıktan sonra satır atla
    print("")

#tahmin edilen kelimenin gerçek kelimede hangi konumlarda olduğuna bakar
# ve oralara harf tahminini ekler
# "______", "a", "araba" => "a_a_a"
def tahmini_ekle(tahmini_kelime, harf_tahmini, dogru_kelime):
    #string'ler harf harf değiştirilemediği için önce list'e çevir
    # "______" => ['_','_','_','_','_','_']
    tahmini_kelime_liste = list(tahmini_kelime)
    for index in range(len(dogru_kelime)): #for harf in dogru_kelime 
        if dogru_kelime[index] == harf_tahmini:
            tahmini_kelime_liste[index] = harf_tahmini
    
    # ["a", "_", "a", "_", "a"] -> listeyi stringe geri döndürmek için
    tahmini_kelime = "".join(tahmini_kelime_liste) # "a_a_a"
    return tahmini_kelime

#kullanıcının daha önce söylediği harfleri görebilmesi için
def alfabeyi_bas(soylenen_harfler):
    alfabe = ""
    for harf in "abcçdefgğhıijklmnoöprsştuüvyz":
        if harf in soylenen_harfler:
            alfabe += "_ "
        else:
            alfabe += harf + " "
    
    print(alfabe)



'''
 |
 O
/|\
 |
/ \ 
'''
#global değişken 
adam = [" |", "\n O", "\n/", "|", "\\", "\n |", "\n/", " \\"]
def adam_ciz(yanlis_tahmin_sayisi):
    for i in range(yanlis_tahmin_sayisi):
        print(adam[i], end="")
    
    print("")


MAX_YANLIS_TAHMIN_SAYISI = 7
kelimeler = ["araba", "kütüphane", "yaramaz", "sınıf", "çalışkan"]

print("ADAM ASMACA")
print("------------")

#kelime kelime dön
while True:

    #kelime belirle
    #0 ile kelimeler listesinin tüm indisleri arasında rastgele index belirler
    su_anki_kelime = kelimeler[random.randint(0, len(kelimeler) - 1)]
    
    tahmin_edilen_kelime = ""
    #alt tireleri ekle
    for i in su_anki_kelime:
        tahmin_edilen_kelime += "_"

    #her kelime için tahmin tahmin dön
    kullanici_yanlis_tahmin_sayisi = 0
    kelime_bulundu = False
    soylenen_harfler = []

    while kullanici_yanlis_tahmin_sayisi <= MAX_YANLIS_TAHMIN_SAYISI:
        # program: _____ kullanıcı: _ _ _ _ _
        print_tahmin_edilen_kelime(tahmin_edilen_kelime)
        #tahmin etmediği harflerden oluşan alfabeyi bas
        alfabeyi_bas(soylenen_harfler)
        
        #kullanıcıdan harf al
        #lower: "AbC" => "abc" 
        harf_tahmini = input("Bir harf tahmin ediniz.").lower()
        soylenen_harfler.append(harf_tahmini)

        if harf_tahmini in su_anki_kelime:#harf kelimede var
            print(harf_tahmini, "bu kelimede var!")
            #"_ _ _ _ _" => "A _ A _ A"
            tahmin_edilen_kelime =  tahmini_ekle(tahmin_edilen_kelime, harf_tahmini, su_anki_kelime)
        else:#tahmin edilen harf kelimede yoksa
            print(harf_tahmini, "bu kelimede yok! Geriye kalan tahmin hakkınız:", MAX_YANLIS_TAHMIN_SAYISI - kullanici_yanlis_tahmin_sayisi )
            kullanici_yanlis_tahmin_sayisi += 1
        
        # "ARABA"
        if "_" not in tahmin_edilen_kelime: #kullanıcı kelimeyi buldu
            kelime_bulundu = True
            break
        
        adam_ciz(kullanici_yanlis_tahmin_sayisi)
        print("----------------------------")
    
    
    if kelime_bulundu:
        print("TEBRİKLER!")
    else:
        print("KAYBETTİNİZ!")

    #kullanıcı çıkana kadar programın çalışmasını / döngünün dönmesini sağlar
    secenek = input("1) Tekrar Oyna\n2) Çık")
    if secenek == "2":
        break
