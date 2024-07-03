def myfunction():
    print("This is my function")
myfunction()

def addtwonumbers():
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print(f"The sum of {num1} and {num2} is {num1+num2}")
addtwonumbers()

def calculator():
    print("Welcome!")

    # num1=x
    # num2=y
    # function add two numbers
    def add(x, y):
        return x + y

        # function subtract two numbers

    def subtract(x, y):
        return x - y

        # function multiply two numbers

    def multiply(x, y):
        return x * y

        # function divide two numbers

    def div(x, y):
        return x / y

    print("Select operation")
    print("1.addition")
    print(" 2.subtract ")
    print(" 3.division ")
    print("4.multiply")

    while True:
        choice = input("enter choice(1/2/3/4):")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number:"))
                num2 = float(input("Enter first number:"))
            except ValueError:
                print("Invalid input")
                continue
    if choice == '1':
        print(num1, '+', num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, '-', num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, '/', num2, "=", div(num1, num2))
    elif choice == '4':
        print(num1, '*', num2, "=", multiply(num1, num2))

        next_calculation = input("Let's do next calculation?(yes/no?):")
    if next_calculation == 'no':
        breakpoint()
    else:
        print("Invalid input")
        calculator()