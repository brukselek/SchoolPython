def suma():
    suma = 0;
    podanaLiczba = 0;
    for i in range(1,11):
        while True:
            try:
                podanaLiczba = int(input("Wprowadz liczbe: >> "))
                suma += podanaLiczba
                break
            except ValueError:
                print("Blednie podana dana. Sprobuj ponownie: ")
    print("Suma podanych liczbe: ", suma)

suma()