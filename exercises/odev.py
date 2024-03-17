#Oyuncu Görevlendirme Programı

print("Oyuncu Görevlendirme Programi")

ad = input("oyuncunun adi: ")
soyad = input("oyuncunun soyadi: ")
görev = input("oyuncunun gorevi: ")

bilgiler = [ad,soyad,görev]

print("Bilgiler okunuyor...")

print("oyuncunun adi: {}\noyuncunun soyadi: {}\noyuncunun gorevi: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))
      
      
print("Bilgiler Kaydedildi")
######

#Denklemin kökünü bulma kodu
print("DENKLEM KÖKÜ BULMA PROGRAMI")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b**2 - 4 * a * c

x1 = (-b + delta **0.5) / (2*a)
x2 = (-b - delta **0.5) / (2*a)


print("Kök Hesaplaniyor...")


print("Birinci kök: {} \nİkincki kök: {}\n".format(x1,x2))
######

#problem1
print("sayi çarpma motoru")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
sonuç = a*b*c

sayilar = [a,b,c,sonuç]

print("sayilar çarpiliyor...")

print("a:{}\nb:{}\nc:{}\n sonuç:{}\n".format(sayilar[0],sayilar[1],sayilar[2],sayilar[3]))
######

#problem2
print("kütle endeksi hesaplama motoru")

boy = float(input("kişinin boyu:"))
kütle = int(input("kişinin kütlesi:"))



sonuç  = kütle/(boy*boy)

işlemler = [boy,kütle,sonuç]

print ("boy{}\nkütle{}\nsonuç{}\n".format(işlemler[0],işlemler[1],işlemler[2]))
######

#problem3
print("benzin parasi hesaplama motoru")

a = float(input("km başina yaktigi miktar"))
b = int(input("yolun kilometresi"))

sayilar = [a,b]

print("Kaç tl yakti? {}".format(sayilar[0]*sayilar[1]))
######

#problem4
print("Bilgi alma motoru")

ad = input("kişinin adi: ")
soyad = input("kişinin soyadi: ")
numara = input("kişinin numarasi: ")

bilgiler = [ad,soyad,numara]

print("bilgiler okunuyor...")

print("ad: {}\nsoyadi: {}\nnumarasi: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))

#problem5
print("hipotenus hesaplayici")

a = int(input("birinci kenarin uzunluğu santimetre cinsinden"))
b = int(input("ikinci kenarin uzunluğu santimetre cinsinden"))
c = (a*a)+(b*b)

değerler = [a,b, float(c**0.5)]

print("hipotenus hesaplaniyor...")

print("birinci kenar: {}\nikinci kenar: {}\nhipotenus: {}\n".format(değerler[0],değerler[1],değerler[2]))
print("hesaplandi...")
#######

#odevsonu