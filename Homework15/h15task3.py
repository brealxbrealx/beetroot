# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework15
# task3

# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain

#If some of the rules' checks returns False, the function should return False and print the \
# reason it failed; otherwise, return the result.


def arg_rules(type_: type, max_length: int, contains: list):
    def wrap(func):
        def chek_args(name):
            if not isinstance(name, str):
                print('type is not string')
                return False            
            if len(name) > max_length:
                print('exceeded lenth of max lenth')
                return False
            for i in contains:
                if i not in name:
                    print('Should contains required elements')
                    return False
            return func(name)
        return chek_args
    return wrap

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'