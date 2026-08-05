weight = int(input())
if weight <= 5:
    totalCharge = 8 * weight
else:
    totalCharge = 8 * 5 + weight - 5 * 6
if totalCharge > 60:
    totalCharge = totalCharge + 10
else:
    totalCharge = totalCharge
print(weight)
print(totalCharge)
