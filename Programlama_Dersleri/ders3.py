# ((x^2 / 3) + 9 - 2x ) * 4

#x = int(input("x değerini giriniz")) 
#sonuc = int(((x ** 2) / 3 + 9 - 2 * x) * 4)
#print("Sonucunuz:", sonuc)

# LIST'ler

# içi boş liste tanımlamak
#alisveris_listesi = []
#print(alisveris_listesi)

#alisveris_listesi = ["muz", "kabak", "patlıcan"]
#print(alisveris_listesi)

#tek_sayilar_listesi = [1, 3, 5, 7, 9]
#kesirli_sayilar_listesi = [0.5, 1.5, 2.0]
#print(kesirli_sayilar_listesi)
#print("tek sayılar:", tek_sayilar_listesi)

#karisik_liste = ["bu bi string", 5, 3.2]
#print(karisik_liste)

#List'ler üzerinde uygulanabilecek fonksiyonlar


# listeye yeni eleman eklemek
#menu_listesi = []
#print(menu_listesi)
#menu_listesi.append("çorba")
#menu_listesi.append("ekmek")
#menu_listesi.append("sufle")
#print(menu_listesi)
#print(menu_listesi[2])

#liste elemanlarına erişme
#sinif_listesi = ["Ayşe", "Kemal", "Fatma", "Melike", "Ali", "Hasan"]
#print("Listenin 2. elemanı:", sinif_listesi[1])
#print("Listenin son elemanı:", sinif_listesi[5])
#print("Listenin son elemanı:", sinif_listesi[-1])
#print("Listenin sondan ikinci elemanı:", sinif_listesi[-2])

# belirli bir index'e yeni eleman eklemek
#sinif_listesi.insert(2, "Beyza")
#print(sinif_listesi)

# eleman silmek için
#sinif_listesi.remove("Beyza")
#print(sinif_listesi)

# farklı fonksiyonlar
#print("Listedeki toplam eleman sayısı:", len(sinif_listesi))
#print("Son eleman:", sinif_listesi[len(sinif_listesi) - 1])
#print("Listedeki Ayşe sayısı:", sinif_listesi.count("Ayşe"))
#sinif_listesi.sort()
#print(sinif_listesi)

#slice operator + - * :
#sinif_listesi = ["Ayşe", "Kemal", "Fatma", "Melike", "Ali", "Hasan"]
# başlangıç indexi (listeye dahil): bitiş indexi (listeye dahil DEĞİL)
#kemal fatma melike:
#print(sinif_listesi[1:4])
#ilk elemandan başlandığı zaman 0 yazılmasına gerek yok
#son elemanda bitirildiği zaman son eleman indexinin yazılmasına gerek yok
#print(sinif_listesi[:])
#print("son üç eleman:", sinif_listesi[-3:])

#sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print("tek sayılar:", sayilar[0:10:2])
# başlangıç indexi (listeye dahil) : bitiş indexi (listeye dahil DEĞİL) : adım boyutu
#print("çift sayılar:", sayilar[1::2])
#print("üçün katları:", sayilar[2::3])

#eleman değiştirme
#sinif_listesi = ["Ayşe", "Kemal", "Fatma", "Melike", "Ali", "Hasan"]
#fatmanin_indexi = sinif_listesi.index("Fatma")
#sinif_listesi[fatmanin_indexi] = "Fatıma"
#print(sinif_listesi)

# liste listesi
#alisveris_listesi = [
#    ["muz", "elma"],
#    ["kabak", "havuç"],
#    ["meyve suyu"]
#]

# DICTIONARY

#boş bir dictionary oluşturmak
rehber_dict = {}

rehber_dict = {
    "Beyza" : "05366463477",
    "Ayşe" : "8947598376"
}
#print(rehber_dict)

# elemana erişmek
#print(rehber_dict["Ayşe"])

# yeni key-value çifti eklemek
#rehber_dict["Ahmet"] = "762354736"
#rehber_dict.update({"Fatma" : "6546456"})

#değer güncellemek
#rehber_dict["Beyza"] = "43539834"
#print(rehber_dict)

# eleman silmek
#rehber_dict.pop("Ayşe")
#print(rehber_dict)

#print(rehber_dict.keys())
#print(rehber_dict.values())

#örnek

#sayi_dict = {
#    1 : "bir",
#    2 : "iki",
#    3 : "#üç"
#}
#print(sayi_dict)
#sayi_dict[4] = "dört"
#sayi_dict.update({5 : "beş"})
#print(sayi_dict)

#örnek

#isimler = {
#    "a" : ["Ayşe", "Ali", "Amine"],
#    "b" : ["Beyza", "Beliz", "Bahadır"],
#    "c" : ["Cengiz"] 
#}
#print(isimler["b"][0:2])

# alışveriş dictionary'si
# meyveler: muz, armut
# sebzeler: kabak, havuç
# içecekler: su

#alisveris_dict = {
#    "meyveler" : ["muz", "armut"],
#    "sebzeler" : ["kabak", "havuç"],
#    "içecekler" : ["su"]
#}
#print(alisveris_dict["sebzeler"])


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
'''






