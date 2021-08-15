# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework7
# task2

#Create a function called make_country, which takes in a country’s name and capital as parameters. Then create a \
# dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. Make the function print out the \
# values of the dictionary to make sure that it works as intended.
#'name': name, 'capital': capital


country_name = input('Enter country name\n')
capital_name = input('Enter capital name\n')

def country_dict(countrys_name, capitals_name) ->str:
    dict_country = {'name':countrys_name,'capital':capitals_name}
    print(dict_country)

country_dict(country_name,capital_name)
