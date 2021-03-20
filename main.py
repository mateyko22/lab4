# Zad1
# liczby = [x for x in range(1,101) if x % 4 == 0]
# plik = open("liczby.txt","w+")
# liczby = str(liczby)
# plik.writelines(liczby)
# plik.close()

# Zad2
# plik = open("liczby.txt","r")
# print(plik.read())
# plik.close()

# Zad3
# with open("liczby.txt","r+") as plik:
#     plik.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n"
#                "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,\n"
#                "when an unknown printer took a galley of type and scrambled it to make \n"
#                "a type specimen book.")
#     for linia in plik:
#         print(linia, end="")

# Zad4
class NaZakupy:
    nazwa_produktu = ""
    ilosc = 2
    jednostka_miary = 3
    cena_jed = 4