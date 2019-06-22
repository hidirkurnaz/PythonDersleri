# Programcı hataları (error)
# program kusurları (bug)
# istisnalar (exceptions) indirirken veya setup sırasında pil bitmesi gibi
# mantıksal hatalar ( yanlış yazımlar gibi)


print("sad")


telefon_numarası = input(" lütfen telefon numarası giriniz : ")
print("telefon numaranız : ", int(telefon_numarası))



try:
    telefon_numarası = input(" lütfen telefon numarası giriniz : ")
    print("telefon numaranız : ", int(telefon_numarası))
except:
    print("işlem hatası : ")