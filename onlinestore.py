# Input
purchase = float(input("Enter total purchase amount (NPR): "))
loyalty = input("Are you a loyalty member? (yes/no): ").lower()

# Determine purchase discount
if purchase < 1000:
    discount = 0
elif purchase < 5000:
    discount = 0.05
elif purchase < 15000:
    discount = 0.10
else:
    discount = 0.20

# Apply purchase discount
discounted_amount = purchase - (purchase * discount)

# Apply extra loyalty discount
if loyalty == "yes":
    discounted_amount = discounted_amount - (discounted_amount * 0.05)

# Display results
print(f"Original Purchase Amount: NPR {purchase:.2f}")
print(f"Final Payable Amount: NPR {discounted_amount:.2f}")