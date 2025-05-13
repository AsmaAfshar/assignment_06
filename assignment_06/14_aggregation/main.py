#Create a class Department and a class Employee. Use aggregation by having a Department object store 
# a reference to an Employee object that exists independently of it.


class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        
        
    def __str__(self):
        return f"{self.name}, {self.position}"
    
class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []
        
        
    def add_employee(self , employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
        else:
            print("Only Employee instances can be added.")
            
    def list_employees(self):
        print(f"Employees in {self.dept_name} Department")
        for emp in self.employees:
            print(emp)
# create employee instance
emp1 = Employee("Ali", 25, "Software Engineer")
emp2 = Employee("Kamran", 30, "Data Analyst")
emp3 = Employee("Rabia", 27, "Frontend Developer")

# creating a department instance
dept = Department("IT")

# Adding employees to the department
dept.add_employee(emp1)
dept.add_employee(emp2)
dept.add_employee(emp3)


# listing employeees in the department
dept.list_employees()

        
        