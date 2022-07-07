# DEĞİŞKENLER
# değişken tanımla
# 1) isim ver
# - sayı ile başlamasın
# - büyük küçük harfe duyarlı
# - tr karater içermesin
# tercihen
# - mantıklı

# string veri tipinde isim adında bir değişken tanımladık
#isim = "Beyza"
# + burada kelimeleri birleştirir
#print("Hello " + isim)

#kullanıcıdan ismini al ve ekrana yazdır
#kullanici_adi = input("Adınız nedir?")
#print("Hoş geldin " + kullanici_adi)

#int tam sayı
#sayi = 5
#print(sayi * 2)
#print(type(sayi))

#float
#kesirli_sayi = 5.3
#print(kesirli_sayi + 5)

#print("y = (3x^2 - 5x) / (6 + 2x)")
#x = 6
#print((3 * (x ** 2) - (5 * x)) // (6 + 2 * x))

#mod alma
#mod_alinacak_sayi = 7
#bolen = 5
#print(mod_alinacak_sayi % bolen)

#isim = "Beyza"
#yas = 23
#boy = 1.70
#en_sevilen_yemek = "pizza"

#print("Merhaba ben " + isim +". " + str(yas) + " yaşındayım. " + str(boy) + " boyundayım. En sevdiğim yemek " + en_sevilen_yemek + ".")

#kullanıcıdan yaşını alıp 5 yıl sonraki
#yaşını hesaplayan program

#"kullancıdan gelen veriler"
#string: "5"
#int : 5
#su_anki_yas = input("Kaç yaşındasınız?") 
#su_anki_yas = int(su_anki_yas)
#bes_yil_sonraki_yas = su_anki_yas + 5
#print("5 yıl sonra " + str(bes_yil_sonraki_yas)  + " yaşında olacaksınız.")
#print("5 yıl sonra", bes_yil_sonraki_yas, "yaşında olacaksınız.")

# UYGULAMA - ÇEVİRİCİ
# kullanıcıdan metre olarak aldığı değeri kilometreye
# çeviren uygulama

#metre_degeri = input("Metre değerinizi giriniz.\n")
#metre_degeri = float(metre_degeri)
#km_degeri = metre_degeri / 1000
#print(km_degeri, "KM")

# print(float(input("M'ye çevirmek istediğiniz değeri giriniz.")) * 1000, "M")


'''
"Adınız nedir?" "Beyza"
"Kaç yaşındasınız?" "23"
"Boyunuz kaç?" "1.70"
"En sevdiğiniz yemek nedir?" "pizza"

"Merhaba ben Beyza. Yaşım 23. Boyum 1.70. En sevdiğim yemek pizza.
'''

isim = input("Adınız nedir?")
yas = int(input("Kaç yaşındasınız?"))
boy = float(input("Boyunuz kaç?"))
en_sevdigi_yemek = input("En sevdiğiniz yemek nedir?")

#print("Merhaba benim adım", isim)
#print(yas, "yaşındayım.")
#print(boy, "boyundayım.")
#print("En sevdiğim yemek ", en_sevdigi_yemek)
print("Merhaba benim adım", isim, "\n" ,yas, "yaşındayım.", "\n" ,boy, "boyundayım.","\n" , "En sevdiğim yemek ", en_sevdigi_yemek )


