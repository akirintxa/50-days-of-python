""" PART 1
Write a function called divide_or_square that takes one
argument (a number) and returns the square root of the number if
it is divisible by 5, or its remainder if it is not divisible by 5. For
example, if you pass 10 as an argument, then your function should
return 3.16 as the square root. """

import math


def divide_or_square(num):
    if num % 5 == 0:
        return round(math.sqrt(num), 2)
    return round(num % 5, 2)


# *** Running the function ***
print('--- PART 1 ---')
# 25 is divisible by 5, returns round(sqrt(25), 2) = 5.0
result1 = divide_or_square(25)
print('input: ', 25)
print('divide_or_square: ', result1)  # Output: 5.0

# 12 is not divisible by 5, returns round(12 % 5, 2) = 2.0
result2 = divide_or_square(12)
print('input: ', 12)
print('divide_or_square: ', result2)  # Output: 2.0


""" PART 2
Extra Challenge: Longest Value
Write a function called longest_value that takes a dictionary as 
an argument and returns the first longest value of the dictionary. 
For example, the following dictionary should return "apple" as the 
longest value.
fruits = {'fruit': 'apple', 'color': 'green'} """


def longest_value(dictionary):
    if not dictionary:
        return None
    max_length = max(len(value) for value in dictionary.values())

    for key, value in dictionary.items():
        value_length = len(str(value)) if isinstance(value, str) else 0
        if value_length == max_length:
            return max_length, value

    # No value found with maximum length
    return None


# *** Testing the function ***
print('--- PART 2 ---')
fruits = {'fruit': 'pineapple', 'color': 'yellow', 'size': 'medium'}
print('input: ', fruits)
print('longest_value:', longest_value(fruits))  # Output: (9, 'pineapple')
