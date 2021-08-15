# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework6
# task3

# This program Use a list comprehension to make a list containing tuples (i, j) where \
# `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

# solve without list comprehention
list1 = list(range(1,11))
list2 = [y**2 for y in list1]
list_tuple1 = list(zip(list1,list2))

# solve with list comprehention
list_tuple = [(i, j**2) for i,j in zip(range(1, 11),range(1,11))]

print(list_tuple1)
print(list_tuple)