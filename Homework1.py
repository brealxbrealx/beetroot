'''
homework.py
* Author: Andrey Maiboroda
* brealxbrealx@gmail.com
'''
# This is program from task2 which use 'print' function

# Declaring variables
N = 'Maiboroda'
LN = 'Andrey'

# Using 'print' function with default params "sep" and "end"
print('Last Name','Name')
print(N,LN,'\n')

# Using 'print' functions with changed prams "sep" and "end"
print('Last Name','Name',sep='\t',end='\n'*2)
print(N,LN,sep='\t')
print('\n')

# This is program from task3 which printing capital letters “O” and “H”, made from “#” symbols
# Printing capital letters “O”
print('#########\n#\t#\n#\t#\n#\t#\n#########')
# Printing capital letters “H”
print('\n#\t#\n#\t#\n#########\n#\t#\n#\t#')