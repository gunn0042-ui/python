# Input
balance = float(input("Enter your current account balance (NPR): "))
daily_withdrawn = float(input("Enter amount already withdrawn today (NPR): "))
amount = float(input("Enter withdrawal amount (NPR): "))

# Daily withdrawal limit
daily_limit = 50000

# Validation
if amount % 500 != 0:
    print("Invalid amount. Must be a multiple of NPR 500.")

elif amount > balance:
    print("Insufficient balance.")

elif daily_withdrawn + amount > daily_limit:
    print("Daily withdrawal limit reached.")

else:
    balance -= amount
    print("Withdrawal successful.")
    print(f"Your current balance after withdrawal: NPR {balance:.2f}")