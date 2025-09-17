def obliczanieSzeregu():
    suma = 0
    b = 30
    for i in range(1, 31):
        suma += i/b
        b -= 1
    print(suma)

obliczanieSzeregu()