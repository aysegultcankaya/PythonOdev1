sayi=input('Bir sayı giriniz:')
try:
    int(sayi)
except ValueError:
    print("Girdiğiniz ifade sayı değildir.")
    quit()

tersSayi=sayi[::-1]

if tersSayi ==sayi:
    print ("Girdiğininiz sayı palindrom sayıdır.")
else:
       print ("Girdiğininiz sayı palindrom sayı değildir.")