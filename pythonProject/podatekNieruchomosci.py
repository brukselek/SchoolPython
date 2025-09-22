def liczenieWartosci(wartosc):
    szacowanaWartosc = float(wartosc) * 60/100
    podatek = szacowanaWartosc * 72/10000
    return print(f"Dla szacowanej wartosci: {szacowanaWartosc:.2f} zl, wartosc podatku wynosi: {podatek:.2f}zl")

def main():
    try:
        wartoscNieruchomosci = input("Podaj rzeczywista warosc nieruchomosci: >> ")
        liczenieWartosci(wartoscNieruchomosci)
    except ValueError:
        print("Bledne dane")

main()