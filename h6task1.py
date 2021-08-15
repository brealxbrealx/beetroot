# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework6
# task1

# This program has some sentence (a string) on input and returns a dict containing all \
# unique words as keys and the number of occurrences as values. 



string_input = input('Please, enter your sentence: ')

# split every word on our string on item of list
string_input = string_input.split()

# declare dict
my_dict = {}

for i in string_input:
    my_dict[i] = my_dict.get(i,0)+1
    
print(my_dict)
