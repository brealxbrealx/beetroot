# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework5
# task3
# this program make a list that contains all integers from 1 to 100, then find all integers from the list that \
# are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

from random import randint

# generate list whith 100 integrs
list_numbers = list(range(1,101))

# declare list which store our results
numbers = []

x = 0
while x < len(list_numbers):
    if (list_numbers[x]%7) == 0 and (list_numbers[x]%5) != 0:
       numbers.append(list_numbers[x])
    else:
        pass
    x += 1  

print(numbers)