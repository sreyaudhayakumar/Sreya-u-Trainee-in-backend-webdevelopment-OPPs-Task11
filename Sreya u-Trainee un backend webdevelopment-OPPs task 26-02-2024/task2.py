# 2)Extend the above solution and find the average expense per employee.
# The calculation must be dynamic, there should be no need for you to manually code each addition
# operations. This can be done by keeping track of the objects being created – in a list (But don’t
# manually append the objects to a list, this must happen when the objects are being created).

class Employee:
    all_employees = []

    def __init__(self, name):
        self.name = name
        self.salary = 0
        self.all_employees.append(self)

    def recent_salary(self, hours):
        self.salary = hours * 200

    def __add__(self, other):
        if isinstance(other, (Employee, PartTimeEmployee)):
            total_salary = self.salary + other.salary
            return total_salary
        else:
            raise TypeError("Unsupported type for addition")

    @classmethod
    def calculate_average_expense(cls):
        total_salary = sum(employee.salary for employee in cls.all_employees)
        average_expense = total_salary / len(cls.all_employees)
        return average_expense


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

average_expense = Employee.calculate_average_expense()
print(f"Average expense per employee: {average_expense}")