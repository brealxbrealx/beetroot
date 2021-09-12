# Author: Andrey Maiboroda
# brealxbrealx@gmail.com
# Homework15
# task2

#Write a decorator that takes a list of stop words and\
#  replaces them with * inside the decorated function


def stop_words(words: list):
    def check_func(func):
        def replace(name):
            x = func(name)
            for word in words:
                x = x.replace(word, '*')
            return x
        return replace
    return check_func
    

 

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
     return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

