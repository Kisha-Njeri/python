class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_name(self):
        print(f"My name is {self.first_name} {self.last_name} and I am {self.age} years old")


class Student(Person):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)


mystudent = Student("John", "Muya", 24)
mystudent.print_name()
mystudent2=Student("Naomi","Kuria",20)
mystudent2.print_name()
mystudent3=Student("Mary","Odhiambo",23 )
mystudent3.print_name()
mystudent4=Student("Lincoln","Were",22)
mystudent4.print_name()