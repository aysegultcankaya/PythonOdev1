name=input("Adınız:")

maas=int(input("Maaşınız:"))
zam=int(input("Zam Oranı %:"))

yeniMaas=int(maas+((maas*zam)/100))

print(name, 'güncel maaşınız: ' ,yeniMaas)