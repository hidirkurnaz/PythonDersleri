try:
    sayi1 = int(input("pls bölünecek sayiyiy gir:"))
    sayi2 = int(input("ols böleni git : "))
    sonuc = sayi1 / sayi2


    print("işlem sonucu: ", sonuc )
except ValueError as exp :
    print("işlem hatası:", exp )
else:
    try:
        print ( sayi1 / sayi2 )
    except ZeroDivisionError :
        print("satı sıfır değerine bölünemez kral")