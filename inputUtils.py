
# Author: Andrey Maiboroda
# brealxbrealx@gmail.com

# this program whit function that checks ащк valid input variables
def getFloatInput(text):
    while True:
        userInput = input(text)
        try:
            result = float(userInput)
            return result
        except:
            print('Your input is not valid. Only numbers accepted.')   

def getMathSymbolInput(text):
    while True:
        userInput = input(text)
        if userInput in ['+','-','*','/','**','%','//']:
            return userInput
        else:
            print('Your input is not valid. Math opertor must be in range (+, -, *, /, **,%, //), try again.') 