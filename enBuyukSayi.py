sayi1=int(input("Birinci sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))
sayi3=int(input("Üçüncü sayıyı giriniz: "))

if sayi1>=sayi2 and sayi1>=sayi3:
    buyukSayi=sayi1
elif sayi2>=sayi3 and sayi2>=sayi1:
    buyukSayi=sayi2
else:
   buyukSayi = sayi3

print("En büyük olan sayı:", buyukSayi)



     
     
    
