# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework7
# task3
# Create a function called make_operation, which takes in a simple arithmetic operator as a first \
# parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) \
# as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:
# For example:
# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42

def callmake_operation(operator: str, *numbers: int) -> int:
    
    if operator == '+':
        prev_val = 0
        for number in numbers:
            prev_val = prev_val + number
        return prev_val    
      
    if operator == '-':
        prev_val = 0
        length = len(numbers)
        for i in range(0, length):
            element = numbers[i]
            if i == 0:
                prev_val = element 
                continue       
            prev_val = prev_val - element
        return prev_val      

    if operator == '*':
        prev_val = 1
        for number in numbers:
            prev_val = prev_val * number
        return prev_val       
     

print(callmake_operation('+', 7, 7,2))
print(callmake_operation('-',7,7,2))
print(callmake_operation('*',7,7,2))
