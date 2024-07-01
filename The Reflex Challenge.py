import random
from datetime import date
import time
import keyboard


def main():
    print("""Welcome to the Reflex Challenge!
The rules are to press any random key on the keyboard as fast as you can""")
    
    userinfo = []
    
    name = input("Enter username: ")
    try:
        grad_year = input("What year did you graduate? ")

    except ValueError:
        print("Please input a valid number.")




    userinfo.append(name)
    userinfo.append(grad_year)



main()


def roundCounter():

    count = 0  

    def increment_round():
        nonlocal count  
        count += 1
        return count
    
    return increment_round  


round_func = roundCounter()


print(round_func())  # Output: 1
print(round_func())  # Output: 2
print(round_func())  # Output: 3

roundCounter()






gameStart = input("Press anything to start: ")