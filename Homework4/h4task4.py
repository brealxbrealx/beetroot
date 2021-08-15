# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework4
# task4

# This program asks the answer for a mathematical expression, checks whether the user is right or wrong,\
# and then responds with a message accordingly.

import random
import calc

def getFloatInput(text):
    while True:
        userInput = input(text)
        try:
            result = float(userInput)
            return result
        except:
            print('Your input is not valid. Only numbers accepted.')   

# get variable "a" in range 1-10
a = random.randint(1, 9)

# get variable "a" in range 1-10
b = random.randint(1, 9)

# declare list whith math symbols 
math = ['+','-','*','/']

# get varieble with random math symbol
c = random.choice(math)

# proclaim the condition of the program
print(f'Please enter wright answer to math function\n"{a} {c} {b}"?')

user_answer = 0 
result_func = 0

# call the function of calculating variables depending on the selected mathematical action
if c == '+':
    result_func = calc.add(a,b)
elif c == '-':
     result_func = calc.sub(a,b)
elif c == '*':
    result_func =  calc.mult(a,b)
elif c == '/':
     result_func = calc.div(a,b)
     print('Hint: for the division function, provide the answer with rounding up to 2 decimal places)') 

# the logic of comparing the user's answer with the correct answer
while True:
    user_answer = getFloatInput('Your answer?\n') 
    if (round(result_func, 2)) == (round(user_answer, 2)):
        print('You have good math. Congratulations, you gave the right answer.')
        break
    else:
        print('You need to do more math. The answer is incorrect, try again.')