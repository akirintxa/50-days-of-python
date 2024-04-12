""" PART 1
A String Range
Write a function called string_range that takes a single number 
and returns a string of its range. The string characters should be 
separated by dots(.). For example, if you pass 6 as an argument, 
your function should return "0.1.2.3.4.5." """


def string_range(num):
    result = ''
    for i in range(0, num):
        result = result + str(i) + '.'
    return result


# *** Testing the function ***
print('string_range: ', string_range(6))

""" PART 2
Extra Challenge: Dictionary of Names
You are given a list of names, and you are asked to write a code that 
returns all the names that start with "S." Your code should return 
a dictionary of all the names that start with S and how many times 
they appear in the dictionary. Here is a list below:
names = ["Joseph", "Nathan", "Sasha", "Kelly",
 "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
Your code should return: {"Sasha": 1, "Sera": 2}
 """


def start_with_s(my_list):
    dict_of_s = {}
    for item in my_list:
        if item[0].lower() == 's':
            if item not in dict_of_s:
                dict_of_s[item] = 1
            else:
                dict_of_s[item] += 1
    return dict_of_s


# *** Testing the function ***
print('--- PART 2 ---')
names = ["Joseph", "Nathan", "Sasha", "Kelly",
         "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

print('start_with_s: ', start_with_s(names))
