# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework5
# task2
# this program Generate 2 lists with the length of 10 with random integers from 1 to 10, \
# and make a third list containing the common integers between the 2 initial lists without any duplicates.

import random

# generate 2 lists in range 10 with 10 index 
list_first = random.choices(range(10), k=10)
list_second = random.choices(range(10), k=10)

# print 2 lists 
print('First list',(list_first))
print('Second list',(list_second))

# declare third list which store common int between 2 lists
list_third = list(set(list_first)&set(list_second))

list_third.sort()

print('The common integers between the 2 initial lists without any duplicates is',(list_third))