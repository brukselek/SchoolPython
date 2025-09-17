R = 0
E = 0
S = 0

R = float(input("Podaj Dlugosc rzedu w metrach: "))

E = float(input("Podaj ilosc miejsca wymaganego przez stelaz w metrach: "))

S = float(input("Podaj odleglosc miedzy krzewami w metrach: "))

if (S > 0):
    V = ( (R - 2*E) / S)

if R > 2*E:
    print(f"Liczba krzewów które zmieszcza sie w rzedzie: {int(V)}")
else:
    print("W winnicy nie zmieszcza sie krzewy :(")
