budzetMiesieczny = input("Podaj swoj miesieczny budzet: >> ")

ileWydatkow = input("Ile masz wydatkow w tym miesiacu: >> ")

try:
    wydatek = 0
    sumaWydatkow = 0
    for i in range(int(ileWydatkow)):
        wydatek = input(f"Podaj koszt {i + 1} wydateku: >> ")
        sumaWydatkow += int(wydatek)
except ValueError:
    print("Ilosc wydatkow musi byc liczba calkowita")

if int(sumaWydatkow) < int(budzetMiesieczny):
    print("Miescisz sie w budzecie")
else:
    print("Nie miescisz sie w budzecie")