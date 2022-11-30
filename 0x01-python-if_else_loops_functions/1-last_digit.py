#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
    lastdigit = number % 10
    print(f"last digit of {number} is {lastdigit} and is greater than 5")
if number == 0:
    lastdigit = number % 10
    print(f"last digit of {number} is {lastdigit} and is 0")
if number < 6 & number != 0:
    lastdigit = number % -10
    print(f"last digit of {number} is {number} and is less than 6 and not 0")
