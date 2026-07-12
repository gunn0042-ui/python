# Dashain Bonus Calculator

salary = float(input("Enter monthly basic salary: "))

bonus = salary
deduction_rate = 10  # 10% deduction (example)

deduction = bonus * deduction_rate / 100
take_home = bonus - deduction

print("Dashain Bonus: Rs.", bonus)
print("Deduction: Rs.", deduction)
print("Take-home Bonus: Rs.", take_home)