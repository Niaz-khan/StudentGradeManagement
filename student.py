"""
Create a class `Student` with attributes for name, grades (a list), and methods to add grades, calculate
average, and determine the letter grade.
Implement a function to handle user input for adding grades and calculating the results.
"""


class Student:
    def __init__(self):
        self.st_name = None
        self.st_grades = []
        self.grade = None

    def add_grades(self):
        name = input("enter the name of the student:) ".upper())
        for _ in range(7):
            ob_numbers = input("enter your numbers/(Q to exit):) ".upper())
            if ob_numbers.lower() == "q":
                break
            try:
                self.st_grades.append(int(ob_numbers))
            except Exception as e:
                print("Error:", e)

    def calculate_average(self):
        sum_of_grades = sum(self.st_grades)
        average = sum_of_grades/len(self.st_grades)
        return average

