def przyrost(ilosc, przyrost, dni):
    iloscOrganizmow = float(ilosc)
    for i in range(dni):
        iloscOrganizmow *= 1 + float(przyrost) / 100
        print(f"Ilosc organizmow w dniu {i + 1}: {iloscOrganizmow:.2f}")

liczbaOrganizmow = input("Podaj liczbe organizmow: >> ")
dziennyPrzyrost = input("Podaj dzienny przyrost wyrazony procentowo: >> ")
liczbaDni = int(input("Podaj liczbe dni przez ktora sie beda namnazac: >> "))


przyrost(liczbaOrganizmow, dziennyPrzyrost, liczbaDni)