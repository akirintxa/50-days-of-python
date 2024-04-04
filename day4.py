""" Only Floats
Write a function called only_floats, which has two parameters, 
a and b, and returns 2 if both arguments are floats, 1 if only one 
argument is a float, and 0 if neither argument is a float. If you 
pass (12.1, 23) as an argument, your function should return 1.
"""


def only_floats(a, b):
    if type(a) == float and type(b) == float:
        return 2
    elif type(a) == float or type(b) == float:
        return 1
    else:
        return 0


# *** Testing the function ***
print('--- PART 1 ---')
print('only_floats(1.0, 2.0): ', only_floats(1.0, 2.0))
print('only_floats(1.0, 2): ', only_floats(1.0, 2))
print('only_floats(1, 2.0): ', only_floats(1, 2.0))
print('only_floats(1, 2):', only_floats(1, 2))

""" PART 2
Extra Challenge: Index of the Longest Word
Write a function called word_index that takes one argument, a 
list of strings, and returns the index of the longest word in the list. 
If there is no longest word (if all the strings are of the same length), 
the function should return zero (0). For example, the first list below 
should return 2.
words1 = ["Hate", "remorse", "vengeance"]
 And this list below, should return zero (0)
words2 = ["Love", "Hate"] """


def word_index(str_list):
    max_index = None
    max_length = 0

    for index, value in enumerate(str_list):
        current_length = len(value)
        if current_length > max_length:
            max_length = current_length
            max_index = index
        elif current_length == max_length:
            return None
    return max_index

# Without using enumerate


def word_index2(str_list):
    max_index = None
    max_length = 0

    for i in range(0, len(str_list)):
        current_length = len(str_list[i])
        if current_length > max_length:
            max_length = current_length
            max_index = i
        elif current_length == max_length:
            return None
    return max_index


# *** Testing the function ***
print('--- PART 2 ---')
words1 = ["Hate", "remorse", "vengeance", "remorse2211"]
print('word_index(str_list): ', word_index(words1))
print('word_index2(str_list): ', word_index2(words1))
