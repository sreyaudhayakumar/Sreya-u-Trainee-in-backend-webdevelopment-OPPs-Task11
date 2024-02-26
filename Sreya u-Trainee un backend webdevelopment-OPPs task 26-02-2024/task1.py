# 1)Create a class Employee with name and salary attributes.
# The salary must be calculated and should be initialized to zero.
# Create a method to calculate the salary by taking the no of hours worked and multiply it by 200.You
# can give no of hours to the method as an argument.
# Now create a child class PartTimeEmployee by inheriting the Employee class, and by using method
# overriding (create salary calculation method in this class also with the same name)
# get the salary of part time employee by multiplying no of hours worked by 150.
# Create 3 objects for each class.
# Now implement '+' operator overloading and find the total salary expense for keeping those
# employees by adding up the objects together.
# Eg:
# e1 = Employee(name="John")
# e1.update_salary(hours=6)
# e2 = Employee(name="Robin")
# e2.update_salary(hours=8)
# e3 = PartTimeEmployee(name="Jake")
# e3.update_salary(hours=8)
# # The below line should work.
# total_expense = e1 + e2 + e3

class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0
        
    def recent_salary(self, hours):
        self.salary = hours * 200

    def __add__(self, other):
        if isinstance(other, Employee):
            total_salary = self.salary + other.salary
            return total_salary
        else:
            raise TypeError("Unsupported type for addition")


class PartTimeEmployee(Employee):
    def recent_salary(self, hours):
        self.salary = hours * 150


hours_e1 = int(input("Enter hours worked by employee 1: "))
hours_e2 = int(input("Enter hours worked by employee 2: "))
hours_e3 = int(input("Enter hours worked by part-time employee 3: "))

employee1 = Employee(name="Athira S")
employee1.recent_salary(hours=hours_e1)

employee2 = Employee(name="Jinsha S")
employee2.recent_salary(hours=hours_e2)

employee3 = PartTimeEmployee(name="Shilpa S")
employee3.recent_salary(hours=hours_e3)

total_expense = employee1 + employee2 + employee3.salary  
print(f"Total expense: {total_expense}")

