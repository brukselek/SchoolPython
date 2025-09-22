def zamianaNaMile(liczbaKm):
    liczbaMile = liczbaKm * 0.6214
    return liczbaMile

def main():
    while True:
        try:
            iloscKilometrow = float(input("Podaj liczbe kilometrow, a program obliczy ile to mili: >> "))
            wynik = zamianaNaMile(iloscKilometrow)
            break
        except ValueError:
            print("Bledne dane")
    print(f"Liczba mili: {wynik:.2f}")

main()
