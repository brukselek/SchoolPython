def spalanieKalorii(ileMinutBiegania):
    spalanieNaBiezni = 4.2

    liczbaSpalonychKalorii = spalanieNaBiezni * ileMinutBiegania

    print(f"Liczba spalonych kalorii: {liczbaSpalonychKalorii:.2f}")

ileMinutNaBiezni = input("Ile minut biegasz na biezni?: >> ")

try:
    ileMinutNaBiezni = int(ileMinutNaBiezni)
    spalanieKalorii(ileMinutNaBiezni)
except ValueError:
    print("Nie podano liczby calkowitej")

