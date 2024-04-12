""" PART 1
Biggest Odd Number
Create a function called biggest_odd that takes a string of 
numbers as an argument and returns the biggest odd number in 
the string. For example, if you pass "23569" as an argument, your 
function should return 9. Use list comprehension. """


def biggest_odd(number_str):
    max_odd_number = 0
    for i in number_str:
        if int(i) % 2 != 0 and int(i) > max_odd_number:
            max_odd_number = int(i)
    return max_odd_number


def biggest_odd2(number_str):
    max_odd = max(int(i) for i in number_str if int(i) % 2 != 0)
    return max_odd if max_odd != float('-inf') else 0


# *** Testing the function ***
# print('biggest_odd: ', biggest_odd('2344569'))
print('biggest_odd2: ', biggest_odd2('312739'))


""" PART 2
Extra Challenge: Zeros to the End
Write a function called zeros_last. This function takes a list as an 
argument. If a list has zeros (0), it will move them to the end of the 
list and maintain the order of the other numbers in the list. If there 
are no zeros in the list, the function should return the original list,
sorted in ascending order. For example, if you pass [1, 4, 6, 0, 7, 
0, 9] as an argument, your code should return [1, 4, 6, 9, 0, 0]. 
If you pass [2, 1, 4, 7, 6] as your argument, your code should 
return [1, 2, 4, 6, 7] """


def zeros_last(number_list):
    non_zeros = []
    zeros = []
    for num in number_list:
        if num != 0:
            non_zeros.append(num)
        elif num == 0:
            zeros.append(num)

    if len(zeros) == 0:
        non_zeros.sort()
    return non_zeros + zeros


# *** Testing the function ***
print('--- PART 2 ---')
numbers1 = [4, 1, 6, 0, 7, 0, 9]
numbers2 = [2, 1, 4, 7, 6]
print('zeros_last: ', zeros_last(numbers1))
print('zeros_last: ', zeros_last(numbers2))
