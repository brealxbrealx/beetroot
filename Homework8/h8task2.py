# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework8
# task2

# Write a function that takes in two numbers from the user via input(), call the numbers a and b, \
# and then returns the value of squared a divided by b, construct a try-except block which raises \
# an exception if the two values given by the input function were not numbers, and if value b was zero \
# (cannot divide by zero).

def getFloatInput1():
    while True:    
        try: 
            a = float(input('Enter first number.\n'))
            b = float(input('Enter second number.\n'))
            return print(a**2/b)        
        
        except ValueError:
            print('Your input is not valid. Only numbers accepted.')
        
        except ZeroDivisionError:
            print('Your input is not valid. Your "second number" = 0. Cannot divide by zero!!!.')

(getFloatInput1())    