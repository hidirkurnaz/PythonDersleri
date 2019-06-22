try:
    telefon_numarası = input(" pls tel no gir : ")
    print("tel no : ", int ("telefon_numarası"))
except ValueError:
    print("işlem hatası ")
    print("sayı gir dedik ")