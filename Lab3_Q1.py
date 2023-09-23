
employee_salaries = {}

while True:
    name = input("Enter the name of the employee (or 'no' to exit): ")

    if name == 'no':
        break
    salary = input(f"Enter the salary of {name} : ")
    employee_salaries[name]=salary

print("Employee Salaries:" , employee_salaries)
