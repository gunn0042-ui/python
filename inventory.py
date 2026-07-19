inventory = [
    {"item": "Rice", "stock": 5, "threshold": 10},
    {"item": "Eggs", "stock": 24, "threshold": 12},
    {"item": "Milk", "stock": 3, "threshold": 6},
    {"item": "Bread", "stock": 8, "threshold": 5},
    {"item": "Chicken", "stock": 0, "threshold": 4},
    {"item": "Cooking Oil", "stock": 2, "threshold": 3},
]

# Counter for items that need restocking
restock_count = 0

# Check each item in inventory
for product in inventory:
    if product["stock"] < product["threshold"]:
        print(f"Restock Alert: {product['item']} (Stock: {product['stock']})")
        restock_count += 1

# Display total items needing restock
print("\nTotal items that need restocking:", restock_count)