class cars:
    def __init__(self, model, YOM, type, color):
        self.model = model
        self.YOM = YOM
        self.type = type
        self.color = color

    def display(self):
        print(f"My dream car is {self.model} manufactured in {self.YOM} ,being a {self.type} which is {self.color} in color")


c1 = cars("Isuzu", 2004, "Double-cabin", "red")
c1.display()
c2 = cars("Toyota", 2012, "Convertible", "blue")
c2.display()
c3 = cars("Volks Wagen", 1995, "pick-up", "black")
c3.display()
c4 = cars("BMW", 2003, "SUV", "grey")
c4.display()
c5=cars("Kia",2004,"4*4","white")
c5.display()

class urembo:
    def __init__(self,type,application):
        self.type=type
        self.application=application

    def display(self):
       print("self.type,self.application")

M1=urembo("Primer","face")
M1.display()
M2=urembo("lotion","face and body")
M2.display()