# Momo Shop Profit Tracker

cost_price = float(input("Enter cost price per plate: Rs. "))
selling_price = float(input("Enter selling price per plate: Rs. "))
plates_sold = int(input("Enter number of plates sold: "))

total_revenue = selling_price * plates_sold
total_cost = cost_price * plates_sold
total_profit = total_revenue - total_cost
profit_margin = (total_profit / total_revenue) * 100

print("\n----- Profit Report -----")
print(f"Total Revenue: Rs. {total_revenue:.2f}")
print(f"Total Cost: Rs. {total_cost:.2f}")
print(f"Total Profit: Rs. {total_profit:.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")