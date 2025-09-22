def kineticEnergy(objectMass, objectSpeed):
    energia = float(objectMass) * float(objectSpeed)**2
    return 1/2 * energia

def main():
    weight = input("Podaj mase obiektu w kg: >> ")
    speed = input("Podaj predkosc w m/s: >> ")

    print(f"Energia kinetyczna ciala wynosi: {kineticEnergy(weight, speed)}")

main()