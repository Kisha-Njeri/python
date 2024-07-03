# arithmetic operators
x = 34
y = 6


print(f"Addition operator {x + y}")
print(f"subtraction operator {x - y}")
print(f"division operator {x / y}")
print(f"multiplication operator {x * y}")
print(f"remainder operator {x % y}")

# comparison operator
print(f"{x} is not equal to {y}", x != y)
print(f"{x} is equal to {y}", x == y)
print(f"is {x} greater than {y} ", x > y)
print(f"is {x} less than {y} ", x < y)
print(f"is {x} greater than or equals to {y} ", x >= y)
print(f"is {x} less than or equals to {y} ", x <= y)

# logic operators
# these are ;and,or and not
a = 45
print("is this statement true?", a > 54 and a < 24)
print("any one statement is true", a > 34 or a < 24)
# print() not??
print("Each statement is true and then return false and viceversa:",(not (a>54 and a<45)))
