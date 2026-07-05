Current_units=int(input("Enter the current units consumed: "))
previous_units=int(input("Enter the previous units consumed: "))
units_consumed = Current_units - previous_units
print(f"Units consumed: {units_consumed}")
total_amount=units_consumed*13
print(f"Total amount to be paid: {total_amount}")
