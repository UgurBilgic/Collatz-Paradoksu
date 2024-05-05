print("Sıfırdan büyük herhangi bir tam sayı girmeniz durumunda girilen sayı çift ise 2'ye böler tek ise 3 ile çarpıp 1 ekler. Buna Collatz paradoxu denir ve girilen her bir sayının sonucu 1 olacaktır")

sayi = int(input("Bir tamsayı giriniz: "))
30

while(sayi>1):
    if sayi % 2 == 0:
        print(sayi," / 2 = ",sayi / 2)
        sayi=sayi / 2

    elif sayi % 2 == 1:
        print("(",sayi," * 3) +1 = ",(sayi *3)+1)
        sayi=(sayi *3)+1

print ("Sonuc: ",sayi)