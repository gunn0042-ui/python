# Inventory data
inventory = {
    "rice": {"price": 120, "stock": 20},
    "milk": {"price": 90, "stock": 10},
    "bread": {"price": 60, "stock": 15},
    "eggs": {"price": 15, "stock": 30}
}

# Customer cart
cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}

# Function to process the order
def process_order(inventory, cart):
    grand_total = 0
    bill = []

    for item, quantity in cart.items():
        if item in inventory:
            if inventory[item]["stock"] >= quantity:
                cost = inventory[item]["price"] * quantity
                grand_total += cost
                bill.append((item, quantity, cost))

                # Update stock
                inventory[item]["stock"] -= quantity
            else:
                print(f"Sorry, not enough stock for {item}")
        else:
            print(f"{item} is not available in inventory.")

    # Print bill
    print("---- Bill ----")
    for item, quantity, cost in bill:
        print(f"{item} x{quantity} = NPR {cost}")

    print(f"Grand Total: NPR {grand_total}")
    print("--------------")

    # Print updated inventory
    print("Updated stock:")
    for item in inventory:
        print(f"{item} = {inventory[item]['stock']}")

# Call the function
process_order(inventory, cart)