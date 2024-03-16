gercek_sayi = 6
sayi = gercek_sayi - 1

total = 0
while sayi >= 1:
    if gercek_sayi % sayi == 0:
        total += sayi
    sayi -= 1

if total == gercek_sayi:
    print("Mükemmel sayı")
else:
    print("Mükemmel değil")
