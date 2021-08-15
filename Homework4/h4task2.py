# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework4
# task2

# This program get input from user his 'name' and 'age', and than and then congratulations on the phrase whith age on the next year

# get input from user his name
myName = input('Your name?\n')

# get input from user his age as integer
myAge = int(input('Your age?\n'))

# print greeting phrase whith age on the next year
print(f'Hello, {myName}, on your next birthday you’ll be',(myAge+1),'years')