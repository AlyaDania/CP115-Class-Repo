itemName_1 = input("Enter the name of the first item: ")
itemName_2 = input("Enter the name of the second item: ")
itemName_3 = input("Enter the name of the third item: ")

itemPrice_1 = input("Enter the price of the first item: ")
itemPrice_2 = input("Enter the price of the second item: ")
itemPrice_3 = input("Enter the price of the third item: ")

tax_rate = 0.06
tax_amount = (float(itemPrice_1) + float(itemPrice_2) + float(itemPrice_3)) * tax_rate
subtotal = float(itemPrice_1) + float(itemPrice_2) + float(itemPrice_3)
total = subtotal + tax_amount

print("Subtotal:", subtotal)
print("Tax Amount:", tax_amount)
print("Total:", total)