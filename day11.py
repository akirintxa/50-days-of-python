""" Are They Equal?
Write a function called equal_strings. The function takes 
two strings as arguments and compares them. If the strings 
are equal (if they have the same characters and have equal 
length), it should return True; if they are not, it should 
return False. For example, "love" and "evol" should 
return True """


def equal_strings(str1, str2):
    is_present = False
    if len(str1) == len(str2) and len(str1) != 0:
        for letter in str1:
            if letter in str2:
                is_present = True
            else:
                return False
    return is_present


# *** Testing the function ***
print('equal_strings: ', equal_strings('love', 'evol'))

""" PART 2
Extra Challenge: Swap Values
Write a function called swap_values. This function takes 
a list of numbers and swaps the first element with the last 
element. For example, if you pass [2, 4, 67, 7] as a 
argument, your function should return.
[7, 4, 67, 2]. """


def swap_values(num_list):
    swap_list = num_list.copy() #así no se pierde el orden en la lista original
    if len(num_list) > 2:
        first_num = num_list[0]
        last_num = num_list[-1]
        swap_list[0] = last_num
        swap_list[-1] = first_num
    return swap_list


# *** Testing the function ***
print('--- PART 2 ---')
lista = [2, 4, 67, 7]
print('lista original: ', lista)
print('swap_values: ', swap_values(lista))
print('lista original: ', lista)
