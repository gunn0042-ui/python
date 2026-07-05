names = []
marks = []

for i in range(20):
    name = input("Enter student name: ")
    mark = int(input("Enter marks: "))

    names.append(name)
    marks.append(mark)

print("\n---------------- REPORT CARD ----------------")
print("Name\t\tMarks\t\tResult")
print("---------------------------------------------")

for i in range(20):
    if marks[i] >= 90:
        result = "Distinction"
    elif marks[i] >= 75:
        result = "First Division"
    elif marks[i] >= 60:
        result = "Second Division"
    elif marks[i] >= 50:
        result = "Third Division"
    elif marks[i] >= 35:
        result = "Pass"
    else:
        result = "Fail"

    print(names[i], "\t\t", marks[i], "\t\t", result)