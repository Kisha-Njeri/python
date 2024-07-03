try:
#code that might raise an exception
   result = 1 / 0
except ZeroDivisionError as e:
    print(f"An error has occurred: {0}")
finally:
    print(f"This will always be executed")