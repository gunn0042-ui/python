print("===== Foreign Remittance Converter =====")

# Input
usd = float(input("Enter USD amount sent: "))
exchange_rate = float(input("Enter current exchange rate (1 USD to NPR): "))
service_fee_percent = float(input("Enter service fee percentage: "))

# Calculation
converted_amount = usd * exchange_rate
fee = converted_amount * (service_fee_percent / 100)
final_amount = converted_amount - fee

# Output
print("\n===== Result =====")
print(f"Converted Amount: NPR {converted_amount:.2f}")
print(f"Service Fee: NPR {fee:.2f}")
print(f"Final Amount Received: NPR {final_amount:.2f}")