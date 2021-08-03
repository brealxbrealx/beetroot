# Homework3
# Task3
# Author: Andrey Maiboroda
# brealxbrealx@gmail.com

# this program compares the values ​​of two variables and returns True or False

# that function is compares array value of two variables and return True
def IsEqualVariables (a,b):
    a = a[:].upper()
    b = b[:].upper()
    if a == b:
        return True
    else:
        return False

# set default variables of name 
name = 'andriy'

# get variables of name from user
yourName = input('Input your name, please.\n')          

# Use function to compare variables and get result of True or False
c = IsEqualVariables(name,yourName)

# print result
print(c)

# another way of logic of program      
if name[:].upper() == yourName[:].upper():
    print(True)
else: print(False)