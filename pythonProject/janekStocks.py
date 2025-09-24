print("Janek kupil 2000 akcji")
stockCost = 40
provision = float(3/100)
amount = 2000

janekStockCost = float(stockCost * amount)
paidProvisionOfBoughtStocks = float(stockCost * amount * provision)

print("Janek kupil akcje za: ", janekStockCost, " i zaplacil: ", paidProvisionOfBoughtStocks, " brokerowi")

soldCost = float(42.75)
provisionOfSoldStocks = float(3/100)

paidProvisionOfSoldStocks = float(soldCost * provisionOfSoldStocks * amount)

janekSoldStock = float(soldCost * amount)
print(f"Janek sprzedal akcje za: {janekSoldStock:.2f} i zaplacil brokerowi: {paidProvisionOfSoldStocks:.2f}")



totalIncome = float( (janekSoldStock - paidProvisionOfBoughtStocks) - (janekStockCost + paidProvisionOfSoldStocks) )
if(totalIncome > 0):
    print(f"Przychod Janka: {totalIncome:.2f} zl")
else:
    print(f"Janek stracil:  {totalIncome:.2f} zl")
