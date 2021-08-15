# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework7
# task1

# Create a simple function called favorite_movie, which takes a string containing the \
# name of your favorite movie. The function should then print “My favorite movie is named {name}”.

def Favorite_movie (Name_mov:str) ->str:
    print(f'My favorite movie is named "{Name_mov}"')

Name_movi = input('Enter the name of your favorite movie\n')

Favorite_movie(Name_movi)