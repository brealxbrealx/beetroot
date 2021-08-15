# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework4
# task3

# This program that reads an input string and then creates and prints 5 random strings from characters of the input string.
import random 

# get words from user input
string = list(input('Please input your word\n'))

for i in range(0,5):
    string = random.choices(string, k=5)
    print(''.join(string), end=', ')