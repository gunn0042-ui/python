print("===== Employee Salary Calculator =====")

employee = input("Enter employee name: ")

hours = float(input("Enter working hours: "))
rate = float(input("Enter hourly rate: "))

gross_salary = hours * rate

deduction = float(input("Enter deductions: "))

bonus = input("Special occasion bonus? (yes/no): ").lower()

if bonus == "yes":
    bonus_amount = float(input("Enter bonus amount: "))
else:
    bonus_amount = 0

final_salary = gross_salary - deduction + bonus_amount

print("\n======= Salary Slip =======")
print("Employee Name :", employee)
print("Gross Salary  :", gross_salary)
print("Deductions    :", deduction)
print("Bonus         :", bonus_amount)
print("Final Salary  :", final_salary)
print("===========================")