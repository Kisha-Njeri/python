class Employee:
    def __init__(self, name, employee_id, salary, department):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.department = department

    def display_information(self):
        print(f"Employee Name: {self.name} "
              f"ID: {self.employee_id} "
              f"Salary annually: {self.salary * 12} "
              f"Department: {self.department}")

    def calculate_annual_salary(self):
        return self.salary * 12


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department, employees_managed=None):
        super().__init__(name, employee_id, salary, department)
        self.employees_managed = employees_managed if employees_managed is not None else []

    def display_information(self):
        super().display_information()
        print(f"Employees Managed: {[employee.name for employee in self.employees_managed]}")

    def add_employee(self, employee):
        self.employees_managed.append(employee)

    def display_employees_managed(self):
        print("Employees Managed:")
        for employee in self.employees_managed:
            print(f"- {employee.name} (ID: {employee.employee_id})")


class Developer(Employee):
    def __init__(self, name, employee_id, salary, department, programming_languages=None):
        super().__init__(name, employee_id, salary, department)
        self.programming_languages = programming_languages if programming_languages is not None else []

    def display_information(self):
        super().display_information()
        print(f"Programming Languages: {', '.join(self.programming_languages)}")

    def add_programming_language(self, language):
        if language not in self.programming_languages:
            self.programming_languages.append(language)


class Intern(Employee):
    def __init__(self, name, employee_id, salary, department, school_name, graduation_year):
        super().__init__(name, employee_id, salary, department)
        self.school_name = school_name
        self.graduation_year = graduation_year

    def display_information(self):
        super().display_information()
        print(f"School Name: {self.school_name}")
        print(f"Graduation Year: {self.graduation_year}")


# Create instances
manager = Manager("John", 1234, 5000, "Training")
developer = Developer("Maria", 1235, 5000, "IT", ["Python", "ReactJS"])
intern = Intern("Daniella", 1236, 4000, "HR", "New Jersey", 2020)

# Display information
manager.display_information()
print()
developer.display_information()
print()
intern.display_information()
print()

# Add employees to the manager
manager.add_employee(developer)
manager.add_employee(intern)
manager.display_employees_managed()
print()

# Add programming language to developer
developer.add_programming_language("Java")
developer.display_information()
print()

# Calculate and print annual salaries
print(f"{manager.name} Annual Salary: Ksh {manager.calculate_annual_salary()}")
print(f"{developer.name} Annual Salary: Ksh {developer.calculate_annual_salary()}")
print(f"{intern.name} Annual Salary: Ksh {intern.calculate_annual_salary()}")

