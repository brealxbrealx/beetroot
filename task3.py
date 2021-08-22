# Homework2
# Task3
# Author: Andrey Maiboroda
# brealxbrealx@gmail.com

# this program is printing a message whith variables 'name' and the 'current day' of the week variables 

import calc
from inputUtils import getFloatInput, getMathSymbolInput

print('Choose two numbers and a math opertor(+,-,*,/,**,%,//) to calculate them ')
   
a = getFloatInput('First number ')
b = getFloatInput('Second numder ')
c = getMathSymbolInput('math opertor ')

# Use math function to calculate result
if c == '+':
    calc.add(a,b)
elif c == '-':
    calc.sub(a,b)
elif c == '*':
    calc.mult(a,b)
elif c == '/':
    calc.div(a,b)
elif c == '**':
    calc.exp(a,b)
elif c == '%':
    calc.mod(a,b)
elif c == '//':
    calc.fdiv(a,b)
