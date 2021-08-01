
# Homework2
# Task3
# Author: Andrey Maiboroda
# brealxbrealx@gmail.com

# this program is printing a message whith variables 'name' and the 'current day' of the week variables 

from datetime import datetime
# Declare variables
name = 'andriy'
current_day = datetime.now()
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Index using weekday int value.
day = current_day.weekday()

# declare third variables
output = ('\nGood day ' + name + '! ' + days[day] + ' is a perfect day to learn some python.\n')

# print string through the third variables
print(output)

# print string whith '.format' method of formating
print('Good day {0}! {1} is a perfect day to learn some python.\n'.format(name,days[day]))

# print string whith 'f' method of formating and using built-in string methods 'capitalize' and 'upper'
print (f'Good day {(name.capitalize())}! {days[day].upper()} is a perfect day to learn some python.\n')
