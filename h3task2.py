# Homework3
# Task2
# Author: Andrey Maiboroda
# brealxbrealx@gmail.com

# get input string of phone number
phoneNumb = input('Enter your phone number.\n')            

# count length of string 
lenStr = len(phoneNumb)

# get an array from string
pnoneNumbArray = phoneNumb[:lenStr]

while lenStr <= 10: #or lenStr !=0:
    if pnoneNumbArray.isdigit():
       print('Your phone number is',(phoneNumb))
       break
    else: print('Invalid input. Please input only digit symbols.')
    break
else: print('Invalid input. Please do not input more than "10" symbols.')        
