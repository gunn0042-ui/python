# BMI Calculator

weight = float(input("Enter weight (kg): "))
height_cm = float(input("Enter height (cm): "))

height_m = height_cm / 100
bmi = weight / (height_m ** 2)

print("BMI:", round(bmi, 1))