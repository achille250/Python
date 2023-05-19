


price=input('Enter charge of the food')
#calculate an amount of 18% tip
tip=float(price)*18/100
#calculate an amount of 7% sales tax
sales=float(price)*7/100
#Grand total
total=float(tip)+float(price)+float(sales)
print("TIP :" + str(tip))
print("SALES TAX :" + str (sales))
print("Grand Total: " +str(total))
