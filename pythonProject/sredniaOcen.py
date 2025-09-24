def main():
    score = []
    for i in range(5):
        wynik = input(f"Podaj wynik z {i+1} sprawdzianu: >> ")
        if(int(wynik) >= 0 and int(wynik) <= 100 ):
            score.append(int(wynik))
        else:
            print("Blednie podany wynik, nie zostanie uwzgledniona")
    return score

def determineGrade(wynik):
    if(wynik > 90 and wynik <= 100):
        return 6
    elif(wynik > 80 and wynik <= 90):
        return 5
    elif(wynik > 70 and wynik <= 89):
        return 4
    elif(wynik > 70 and wynik <= 79):
        return 3
    elif(wynik >= 60 and wynik <= 69):
        return 2
    else:
        return 1

def calcAverage(grades):
    if grades:
        average = sum(grades) / len(grades)
        print(f"Srednia sprawdzianu: {average:.2f}")

wyniki = main()
oceny = []

for wynik in wyniki:
    ocena = determineGrade(wynik)
    oceny.append(ocena)
    print(f"Wynik: {wynik} => Ocena: {ocena}")

calcAverage(oceny)
