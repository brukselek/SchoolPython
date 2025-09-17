def silniaLiczby(n):
    silnia = 1
    for i in range(n):
        silnia *= i + 1
        print(f"Silnia liczby {i + 1}: {silnia}")


n = input("Prosze podaj liczbe calkowita: >> ")

if(type(n) != int or n > 0 ):
    print("Blednie podane dane")
else:
    silniaLiczby(n)
