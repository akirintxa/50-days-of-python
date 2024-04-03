""" PART 1
Strings to Integers
Write a function called convert_add that takes a list of strings 
as an argument, converts them to integers, and sums the list. For 
example, ["1", "3", "5"] should be converted to [1, 3, 5] and 
summed to 9. """
import random
import time


def convert_add(str_list):
    total = 0
    for item in str_list:
        total = total + int(item)
    return total


# *** Testing the function ***
print('--- PART 1 ---')
my_list = ["1", "3", "5"]
print('input: ', my_list)
print('convert_add: ', convert_add(my_list))  # Output: 9


""" PART 2
Extra Challenge: Duplicate Names
Write a function called check_duplicates that takes a list of 
strings as an argument. The function should check if the list has 
any duplicates. If there are duplicates, the function should return 
a list of duplicates. If there are no duplicates, the function should 
return "no duplicates." For example, the list of fruits below 
should return ["apple", "banana"], and the list of names
should return "no duplicates."
fruits = ['apple', 'orange', 'banana', 'apple', 'banana']
names = ['Yoda', 'Moses', 'Joshua', 'Mark'] """

# Con doble bucle - ineficiente


def check_duplicates1(str_list):
    duplicated_items = []
    for i in range(len(str_list)):
        for j in range(len(str_list)):
            if i != j:
                if str_list[i] == str_list[j] and str_list[i] not in duplicated_items:
                    duplicated_items.append(str_list[i])
    if duplicated_items == []:
        return "no duplicates"
    else:
        return duplicated_items

# Con lista auxiliar


def check_duplicates2(str_list):
    duplicated_items = []
    unique_items = []

    for item in str_list:
        if item in unique_items and item not in duplicated_items:
            duplicated_items.append(item)
        else:
            unique_items.append(item)

    if duplicated_items == []:
        return "no duplicates"
    else:
        return duplicated_items


# *** Testing the function ***
print('--- PART 2 ---')
fruits = ['apple', 'orange', 'banana', 'apple', 'banana']
print('input: ', fruits)
print('check_duplicates2: ', check_duplicates2(
    fruits))  # Output: [apple, banana]

numbers = [1, 3, 5, 6, 3, 5, 8, 9, 3]
print('input: ', numbers)
print('check_duplicates2: ', check_duplicates2(numbers))  # Output: [3,5]

cars = ['ford', 'toyota']
print('input: ', cars)
print('check_duplicates2: ', check_duplicates2(cars))  # Output: no duplicates
