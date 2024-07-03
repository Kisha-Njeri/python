class Animal:
    def speak(self):
        print('Animal is speaking')
class Dog(Animal):
    def bark(self):
        print("A dog is barking")
class Cat(Animal):
    def meow(self):
        print("Cats meow")
class cow(Animal):
    def moo(self):
        print("cows moo")

d=Dog()
d.bark()
c=Cat()
c.meow()
d.speak()
c2=cow()
c2.moo()