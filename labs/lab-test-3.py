monthly_usage = float(input())
discount = 0

if monthly_usage < 50:
    discount = 0
elif monthly_usage <= 100:
    discount = 5
else:
    discount = 20
amount_of_the_bill = monthly_usage - (monthly_usage * (discount / 100))
print(f"The amount of the bill to be paid is: {amount_of_the_bill}")