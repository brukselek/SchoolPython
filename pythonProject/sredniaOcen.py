def ocenyZeSprawdzianu():
    grades = []
    for i in range(5):
        ocena = input(f"Podaj ocene z {i+1} sprawdzianu: >> ")
        if(int(ocena) >= 1 and int(ocena) <= 6 ):
            grades.append(int(ocena))
        else:
            print("Blednie podana ocena, nie zostanie uwzgledniona")
    return grades

def calcAverage(grades):
    if grades:
        average = sum(grades) / len(grades)
        print(f"Srednia sprawdzianu: {average:.2f}")

oceny = ocenyZeSprawdzianu()
calcAverage(oceny)
