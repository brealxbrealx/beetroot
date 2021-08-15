# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework9
# task1
# this program that creates a new output file called myfile.txt and writes the string "Hello file world!" in it

string = input('Hello file world!')

with open('myfile.txt', 'w') as myfile:
     my_string = myfile.write(string)