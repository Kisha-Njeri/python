class students:
    #constructor
    def __init__(self,first_name,last_name):
        self.first_name =first_name
        self.last_name =last_name

#method
    def display(self):
       print(self.first_name,self.last_name)
#object
my_student=students("Mary",'Smith')
my_student.display()
my_student2=students("Tamara","Omwami")
my_student2.display()
my_student3=students("Samantha","Iteso")
my_student3.display()
# my_student4.display()
my_student4=students("paul","Onyango")
my_student2.display()
