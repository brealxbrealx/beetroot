# Homework3
# Task1
# Author: Andrey Maiboroda
# brealxbrealx@gmail.com

# this program print strin from user input with firs two and las two charakters

# get input string from user
string = input('Enter your string with more than 2 symbols\n')

# count length of indelenStr string
lenStr = len(string)

if lenStr < 2:
    print('Empty String')
else:   
    # get index of first symbols of string
    firstSymd = lenStr-lenStr+2
   
    # get index of first symbols of string
    lastSymb = (lenStr-lenStr)-2

    # get a segment from the first two characters of the array
    firstArray = string[:firstSymd]

    # get a segment from the first two characters of the array
    lastArray = string[lastSymb:]

    # print output string
    print(firstArray+lastArray)