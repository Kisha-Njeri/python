class watu:
    def __init__(self, jina, miaka):
        self.jina = jina
        self.miaka = miaka

    def kuonyesha(self):
        print(self.jina, self.miaka)


people = watu("Paul Ogutu", 24)
people.kuonyesha()

people2 = watu('Omwami', 56)
people2.kuonyesha()

people3 = watu('Titus', 54)
people3.kuonyesha()

people4 = watu("Agustyne", 15)
people4.kuonyesha()


class fruits:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def display(self):
        print(self.name, self.colour)


f1 = fruits("oranges", "orange")
f1.display()
f2 = fruits("mango", "yellow")
f2.display()
f3 = fruits("ovacado", "green")
f3.display()
