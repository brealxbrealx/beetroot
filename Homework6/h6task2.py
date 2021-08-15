
# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework6
# task1

# This program function which takes as input two dicts with structure mentioned \
# above, then computes and returns the total price of stock.

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def Total_sum_value (a:dict,b:dict) ->dict:
    total = []
    for i, x in zip(a.values(),b.values()):
        total.append(i*x)
    return sum(total)   

total_sum = Total_sum_value(stock,prices)

print(f'The total price of stock is {total_sum}$')