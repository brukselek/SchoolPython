def obliczIloscKalorii(gramyTluszczu, gramyWegli):
    kalorieTluszczu = gramyTluszczu * 9
    kalorieWegli = gramyWegli * 4

    return kalorieTluszczu, kalorieWegli

def main():
    tluszcze = int(input("Podaj liczbe tluszczow w gramach: "))
    wegle = int(input("Podaj liczbe wegli w gramach: "))

    if(int(tluszcze) and int(wegle)):
        tluszcze, wegle = obliczIloscKalorii(tluszcze, wegle)

        print(f"Spozywasz: {tluszcze:.1f} kcal tluszczu oraz {wegle:.1f} kcal wegli")

main()