class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Rs.{amount} deposited into {self.account_number}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Rs.{amount} withdrawn from {self.account_number}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        print(f"{self.name} ({self.account_number}) - Balance: Rs.{self.balance}")


# Given account data
accounts = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai", "A003", 12000),
]

# Create objects
bank_accounts = {}
for name, acc_no, balance in accounts:
    bank_accounts[acc_no] = BankAccount(name, acc_no, balance)

# Perform transactions
bank_accounts["A002"].deposit(3000)
bank_accounts["A003"].withdraw(15000)   # Should fail
bank_accounts["A001"].withdraw(2000)

# Print final balances
print("\nFinal Account Balances:")
for account in bank_accounts.values():
    account.get_balance()