class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / 5

    def grade(self):
        avg = self.average()

        if avg >= 80:
            return "A"
        elif avg >= 65:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        avg = self.average()

        if avg >= 40:
            result = "Pass"
        else:
            result = "Fail"

        print("Name:", self.name)
        print("Average:", round(avg, 2))
        print("Grade:", self.grade())
        print("Result:", result)
        print()


# Create student objects
s1 = Student("Aarav", [78, 85, 60, 90, 72])
s2 = Student("Sita", [45, 50, 38, 60, 55])
s3 = Student("Bishal", [30, 25, 40, 35, 28])
s4 = Student("Priya", [90, 88, 95, 92, 87])

# Display reports
s1.display()
s2.display()
s3.display()
s4.display()