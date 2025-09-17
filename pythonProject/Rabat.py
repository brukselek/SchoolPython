def discount(itemAmount):
    if 10 <= itemAmount <= 19:
        itemDiscount = 10
    elif 20 <= itemAmount <= 49:
        itemDiscount = 20
    elif 50 <= itemAmount <= 99:
        itemDiscount = 30
    elif itemAmount >= 100:
        itemDiscount = 40

    print(f"Wartosc rabatu: {int(itemDiscount)}%")
    price = (itemAmount * 99)
    discountedPrice = (price - (price * itemDiscount / 100))


    print(f"Wartosc zakupow: {discountedPrice}")


itemAmount = int(input("Podaj liczbe sztuk oprogramowania komputerowego jaka chcesz kupic: "))

if itemAmount >= 0:
    print(discount(itemAmount))