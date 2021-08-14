# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework5
# task1
# this program get the largest number from a list of random numbers with the length of 10

import random

# get random list of 10 items in range 10000
numbers = random.choices(range(10000), k=10)

# use the "max()" methods of list and print a largest number
print(f'The largest number from a list of {numbers} ''is',max(numbers))
