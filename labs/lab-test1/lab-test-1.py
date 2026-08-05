weight = int(input())
if weight >= 5:
    totalCharge = 8 * weight
else:
    totalCharge = 6 * weight
if totalCharge > 60:
    totalCharge = totalCharge + 10
print(weight)
print(totalCharge)
