# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework15
# task1

#Write a decorator that prints a function with arguments passed to it.

#OTE! It should print the function, not the result of its execution!



def logger(func):
    def print_decor(*args):
        print(f'"{func.__name__}" function called with {args} arguments.')
    return print_decor

 

@logger
def add(x, y):
    return x + y

 

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

square_all(4,5)    
add(4,6)