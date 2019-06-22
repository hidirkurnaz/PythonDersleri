try:
    sayi1 = int(input("ltfn birinci sayiyi giriniz : "))
    sayi2= int(input("ltfn ikinci sayiyii girinz : "))
    toplam= sayi1 + sayi2
    fark= sayi1 -  sayi2
    bolum= sayi1 / sayi2
    carpim= sayi1 * sayi2
    print( "sayıların toplamı:", toplam,
          "\nsayıların farkı:", fark,
          "\n bölümü:", bolum,
          "\nçarpımı:", carpim )
except ValueError :
    print("value hatası")
except ZeroDivisionError :
    print("zero div hatassı:")
except FileExistsError :
    print("File exist hatası")
except:
    print("git yenisini yaz")
#iki hatayı aynı anda çalıştırmak için;
except ( ValueError , SyntaxError ) :
