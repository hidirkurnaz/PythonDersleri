#HATA MESAJI

try:
    sayi = int(input("lütfen sadece sayısal veri giriniz :"))
    print("gelen sayı", sayi)
except ValueError :
    print( "ValueError")
except ZeroDivisionError :
    print("ZeroDivisionError")
except:
    print("hata")



    try:
        sayi = int(input("lütfen sadece sayısal veri giriniz :"))
        print("gelen sayı", sayi)
        sayi = sayi / 0
        print("işlem bitti")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except:
        print("hata")



try:
        sayi = int(input("lütfen sadece sayısal veri giriniz :"))
        print("gelen sayı", sayi)
        sayi = sayi / 0
        print("işlem bitti")
except ValueError as ex :
        print("ValueError")
except ZeroDivisionError as ex :
        print("ZeroDivisionError")
except Exception as ex:
        print("hata")