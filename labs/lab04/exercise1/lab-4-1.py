kWh = int(input())
if kWh <= 100:
    totalBill = 0.3 * kWh
else:
    if kWh >= 101 and kWh < 200:
        totalBill = 100 * 0.3 + kWh - 100 * 0.5
    else:
        totalBill = 100 * 0.3 + 100 * 0.5 + kWh - 200 * 0.75
print(totalBill)
