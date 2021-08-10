# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework4
# task1

# this program generate random number from 1-10, and sent back the result of the user input via a print statement.

# this function is checks valid input from user on an integer and range
def getFloatInput(text):
    while True:
        userInput = input(text)
        try:
            result = int(userInput)
            if result in range(1,11):
                return result
            else:
                print('Sorry, your number not in randge 1-10. Try againe')        
        except:
            print('Your input is not valid. Only numbers accepted.')

import random

# generate rendom number from range 1-10
randNumber = random.randint(1,10)

userNumber = print('Try to guess the hidden number from 1 to 10. Input your number, please.')

while userNumber != randNumber:
    userNumber = getFloatInput('')
    if userNumber > randNumber:
        print('Try to input a LOWER number. The hidden number is less than yours.')
    elif userNumber < randNumber:
        print('Try to input a GREATER number. The hidden number is greater than yours.')    
else:
    print(f'Congratulations, you got it, the hidden number was {randNumber}')           
 