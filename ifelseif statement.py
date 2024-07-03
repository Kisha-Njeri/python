marks=int(input("Enter Marks:"))

if marks>=79 and marks<=100:
    print("You have an A")

elif marks>=60 and marks<=78:
    print("You have a B")

elif marks>=40 and marks <=60:
    print("You have a C")

elif marks>=0 and marks<=40:
    print("You have failed")

else:
    print("Wrong input,check your marks")

