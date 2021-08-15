# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework10
# task1
# Make a class called Person. Make the __init__() method take firstname, lastname, and age as \
# parameters and add them as attributes. Make another method called talk() which makes prints a\
# greeting from the person containing, for example like this: “Hello, my name is Carl Johnson and\
# I’m 26 years old”.


class Person:
    def __init__(self, firstname, lastname, age) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def display_person(self):
        print(f"Hello my name {self.lastname} {self.firstname} and I'm {self.age} old.")   

Person1 = Person('Johnson','Carl',26)
        
Person1.display_person()        
