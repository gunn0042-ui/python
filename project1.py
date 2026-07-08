vat = 0.13   # 13%
total = 0

print("==== Supermarket Billing System ====")

while True:
    item = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))

    subtotal = price * quantity
    total += subtotal

    choice = input("Do you want to add more items? (yes/no): ").lower()

    if choice == "no":
        break

vat_amount = total * vat
total_with_vat = total + vat_amount

print("\n=== Bill Summary ===")
print("Total Amount: Rs", total)
print("VAT (13%): Rs", vat_amount)
print("Final Bill Amount: Rs", total_with_vat)