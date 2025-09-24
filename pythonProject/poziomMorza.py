podniesieniePoziomu = 1.6
poziomOceanu = 0;

def oceanu(liczbaLat):
    i = 0
    poziomOceanu = 0
    while (i <= int(liczbaLat)):
        poziomOceanu = podniesieniePoziomu * i
        print(f"Po {i} latach poziom oceanu podniesie sie o: {poziomOceanu:.2f} mm")
        i += 1

ileLat = float(input("Ile lat podniesienia oceanu chcesz policzyc? >>  " ))
print("Ocean podniesie sie o: ")

oceanu(ileLat)
