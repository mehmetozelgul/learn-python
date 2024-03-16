# print("Merhaba mehmet")

def selam_ver(isim, soyisim):
    print("Merhaba,", isim, soyisim)

def topla(sayi1, sayi2):
    print("Sonuç: ", sayi1+sayi2)

def cikar(sayi1, sayi2):
    print("Sonuç: ", sayi1-sayi2)

def carpma(sayi1, sayi2):
    print("Sonuç: ", sayi1*sayi2)

def sayilari_al():
    selam_ver("Mehmet", "ÖZELGÜL")
    ilk_sayi = int(input("Ilk sayi: "))
    ikinci_sayi = int(input("Ikıncı sayi: "))

    islem = input("Yapmak istediğiniz işlemi seçiniz: ")
    if islem == "+":
        topla(ilk_sayi,ikinci_sayi)
    elif islem == "-":
        cikar(ilk_sayi,ikinci_sayi)
    elif islem == "*":
        carpma(ilk_sayi,ikinci_sayi)
    else:
        print("BİLİNMEYEN İŞLEM")

sayilari_al()



