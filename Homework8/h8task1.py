# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework8
# task1

# Write a function called oops that explicitly raises an IndexError \
# exception when called. Then write another function that calls oops inside a try/except state­ment to catch the error. What happens if\
#  you change oops to raise KeyError instead of IndexError?


def oops():
    
    raise IndexError
    


def oops_inside():
    
    try:
        oops()
    except Exception: 
        print('Exception!!!!')


oops_inside()
