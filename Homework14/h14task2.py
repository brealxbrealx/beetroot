# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework14
# task2
#Write a Python program to access a function inside a function (Tips: use function, \
# which returns another function)


def add(n):
    def nested_add(x):
        return x + n
    return nested_add

a = add(2)

print(a(2))