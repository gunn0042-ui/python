# NEA Electricity Unit Cost

previous = float(input("Enter previous meter reading: "))
current = float(input("Enter current meter reading: "))

rate = 12          # Cost per unit (example)
service_charge = 50  # Fixed monthly charge

units = current - previous
bill = (units * rate) + service_charge

print("Units Consumed:", units)
print("Total Bill: Rs.", format(bill, ".2f"))