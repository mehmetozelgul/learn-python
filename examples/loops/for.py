sayi = 6

total = 0
for bolen in range(1,6):
    if sayi % bolen == 0:
        total += bolen

if total == sayi:
    print("Mükemmel sayı")
else:
    print("Mükemmel değil")