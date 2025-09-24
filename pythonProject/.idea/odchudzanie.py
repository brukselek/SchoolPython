def obliczanieWagi(waga, okres):
    for i in range(okres):
        waga -= 2
        print(f"Po {i + 1} miesiącach waga wynosi: {waga:.2f} kg")

wagaPoczatkowa = float(input("Podaj wagę początkową (kg): >> "))
okresOdchudzania = int(input("Podaj okres odchudzania (w miesiącach): >> "))

obliczanieWagi(wagaPoczatkowa, okresOdchudzania)
