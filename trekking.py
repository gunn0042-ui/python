print("===== Trekking Permit Cost Calculator =====")

# Input
trekkers = int(input("Enter number of trekkers: "))
tims_fee = float(input("Enter TIMS fee per person (NPR): "))
acap_fee = float(input("Enter ACAP fee per person (NPR): "))

# Calculation
permit_cost_per_person = tims_fee + acap_fee
total_cost = permit_cost_per_person * trekkers
service_charge = total_cost * 0.05
grand_total = total_cost + service_charge
average_cost = grand_total / trekkers

# Output
print("\n===== Result =====")
print(f"Permit Cost (Before Service Charge): NPR {total_cost:.2f}")
print(f"Agency Service Charge (5%): NPR {service_charge:.2f}")
print(f"Grand Total Cost: NPR {grand_total:.2f}")
print(f"Average Cost Per Person: NPR {average_cost:.2f}")