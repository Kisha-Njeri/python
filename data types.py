a = 3
b = 45.8
c = "eMobilis"
d = True
e = False
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
str = "Welcome to coding"
str2 = " at eMobilis Training Institute"

print(str[0:4])  #slicing
print(str[5])
print(str + str2)  #concatenation

majina = ["Eric", "Mercy", "Kisha", "John"]
print(type(majina))
print(f"My name is {majina[0]}")  #lists use box brackets
majina[0] = "Emmanuel"
print(majina[0])
print(majina)  #mutable data structure that supports change

matunda = ("Banana", "Mangoes", "Berries", "Oranges")
print(f"I love eating {matunda[2]}")  #tuple
print(matunda)
# matunda[2]="Pineapples"#tuple doesn't support change
# print(matunda[2])

magari = {"Toyota", "Mercedes", "Isuzu", "Tesla", "Porsche"}  #set
print(type(magari))
print(magari)  #sets don't have indexes

dictionary = {"Age": 20, "salary": 100000, "gender": "male", "name": "John"}
print(type(dictionary))
#contains a key and value
print(f"The employee's age is {dictionary['Age']}" )
print (f"His salary is {dictionary['salary']}")
print(f"The employee is {dictionary['gender']}")
print(f"His name is {dictionary['name']}")
