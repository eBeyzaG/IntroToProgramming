# DÖNGÜLER - LOOPS

#
#kullanici_tahmini = int(input("Bir sayı tahmin ediniz."))
'''
# while döngüleri
sayi = 10
while True:
    kullanici_tahmini = int(input("Bir sayı tahmin ediniz."))
    if sayi == kullanici_tahmini:
        print("Doğru tahmin!")
        break#döngüleri bitirmek için kullanılır
    else:
        print("Bilemediniz...")

print("Program bitti")   

sayi = 10
kullanici_tahmini = int(input("Bir sayı tahmin ediniz."))

while kullanici_tahmini != sayi:
    print("Bilemediniz...")
    kullanici_tahmini = int(input("Bir sayı tahmin ediniz."))

print("Doğru bildiniz!")   


# 1'den x' e kadar olan sayıları while ile yazdırma
x = 10 #durma noktası
i = 1 #adım
while i < x:
    print(i)
    i += 1 # aynı şey i = i + 1

# FOR DÖNGÜLERİ

# [0:10:2]  0 dahil başla 10'a kadar git 2'şer 2şer [:5:]
#for i in range(100, 0, -1):
#    print(i)

arkadaslar = ["Ahmet", "Ali", "Ayşe", "Melike"]
#arkadaslar[0]
#arkadaslar[1]
#arkadaslar[2]
#arkadaslar[3]
for arkadas in arkadaslar:
    print(arkadas)

i = 0
while i < len(arkadaslar):
    print(arkadaslar[i])
    i += 1


arkadaslarin_yaslari = {
    "Ahmet" : 5,
    "Ali" : 6,
    "Ayşe" : 12
}

for arkadas_isim, yas in arkadaslarin_yaslari.items():
    print("Arkadaşım", arkadas_isim, "'nin yaşı:", yas)

for arkadas_isim in arkadaslarin_yaslari.keys():
    print(arkadas_isim)

for yas in arkadaslarin_yaslari.values():
    print(yas)

okunan_kitaplar = {
    "Sessiz Ev" : 350,
    "Güzel Kitap" : 200,
    "Tutunamayanlar" : 100
}
toplam_sayfa_sayisi = 0

for sayfa_sayisi in okunan_kitaplar.values():
    toplam_sayfa_sayisi = toplam_sayfa_sayisi + sayfa_sayisi
    # aynı şey => toplam_sayfa_sayisi += sayfa_sayisi

# okuduğum kştaplar: sessiz ev, dkcnd, dlskfn
yazi = "Okuduğum kitaplar: "
for kitap_adi in okunan_kitaplar.keys():
    yazi += kitap_adi
    yazi += ", "

print(yazi)
print("Toplam sayfa sayısı:", toplam_sayfa_sayisi)

# faktoriyel hesaplayan program
# 5! = 5 * 4 * 3 * 2 * 1 = 120   

n = int(input("Faktoriyelinin hesaplanmasını istediğiniz sayıyı giriniz."))

sonuc = 1

for i in range(n, 0, -1):
    print(sonuc, "*", i)
    sonuc = sonuc * i
print(sonuc)

yazi = "b4zi h4rfler y4nlış y4zılmış."
#yazi_listesi = ['b', '4', 'z', 'i']
# 4'leri a'ya çevir
#HATA VERİR -> yazi[1] = "a"
#HATA VERMEZ -> yazi_listesi[1] = "a"

sonuc_yazi = ""

for harf in yazi:
    if harf == "4":
        sonuc_yazi += 'a'
    else:
        sonuc_yazi += harf

print(sonuc_yazi)

#iç içe döngüler

n = 5
*
**
***
****
*****

n = 8
for i in range(1, n + 1): #1, 2, 3, 4, 5
    for j in range(i):
        print("*", end= "") #end kısmı satır atlamaMAsı için
    print("")

alisveris_list = [
    ["MEYVELER", "muz", "çilek", "erik"],
    ["SEBZELER", "kabak", "patlıcan", "havuç"],
    ["İÇECEKLER", "su"]
]

for tur_listesi in alisveris_list:
    print(tur_listesi[0])
    for malzeme in tur_listesi[1:]:
        print(malzeme)

sayi_listesi = [7, 5, 3, 65, 23, 67, 23, 22, 44, 53, 57, 88]

for sayi in sayi_listesi:
    if sayi % 2 == 1:
        print(sayi, "tek sayıdır.")
    elif sayi % 2 == 0:
        print(sayi, "çift sayıdır")

yazi = "Merhaba benim adım Beyza. Tanıştığıma memnun oldum."
#cümlede kaç boşluk olduğunu hesaplayan program
bosluk_sayisi = 0

for karakter in yazi:
    if karakter == " ":
        bosluk_sayisi += 1

print("Boşluk sayısı:", bosluk_sayisi)
'''
'''
Fizz Buzz:
0 ile 100 arasındaki sayılar için
Sayı 3 ile bölünüyorsa ekrana “Fizz” yazdır
Sayı 5 ile bölünüyorsa ekrana “Buzz” yazdır
İkisine de bölünüyorsa “Fizz Buzz” yazdır
'''



