""" PART 1
Write a function called register_check that checks how many 
students are in school. The function takes a dictionary as an 
argument. If the student is in school, the dictionary says "yes." If 
the student is not in school, the dictionary says "no." Your function 
should return the number of students in school. Using the 
dictionary below, your function should return 3. 
register = {'Michael': 'yes', 'John': 'no',
            'Peter': 'yes', 'Mary':'yes'}
"""


def register_check(dictionary):
    registered = 0
    for key, value in dictionary.items():
        if value == 'yes':
            registered += 1
    return registered


# *** Testing the function ***
print('--- PART 1 ---')
register = {'Michael': 'yes', 'John': 'no',
            'Peter': 'yes', 'Mary': 'yes'}
print('input: ', register)
print('register_check: ', register_check(register))  # Output: 3


""" PART 2
Extra Challenge: Lowercase Names
 
names = ["kerry", "dickson", "John", "Mary", 
 "carol", "Rose", "adam"]
You are given a list of names above. This list is made up of names 
with lowercase and uppercase letters. Your task is to write a 
code that will return a tuple of all the names in the list that only
have lowercase letters. Your tuple should have names sorted 
alphabetically in descending order. Using the list above, your code 
should return:
('kerry', 'dickson', 'carol', 'adam') """


def only_lowercase(str_list):
    lower_items = []
    for item in str_list:
        if item == item.lower():
            lower_items.append(item)
    lower_tuple = tuple(lower_items)
    return lower_tuple


# *** Testing the function ***
print('--- PART 2 ---')

names = ["kerry", "dickson", "John", "Mary",
         "carol", "roSe", "adam"]
print('input: ', names)
# Output: ('kerry', 'dickson', 'carol', 'adam')
print('only_lowercase: ', only_lowercase(names))
