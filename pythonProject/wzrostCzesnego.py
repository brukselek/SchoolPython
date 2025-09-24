def obliczCzesne(ileLat):
    wzrostCzesnego = float(103/100)
    czesne = 8000

    for i in range(ileLat):
        czesne *= wzrostCzesnego
        print(f"Po {i + 1} latach czesne bedzie wynosic: {czesne:.2f}")


naIleLat = int(input("Na ile lat obliczyc czesne? >> "))
obliczCzesne(naIleLat)