""" Write a function called user_name that generates a 
username from the user’s email. The code should ask the user 
to input an email, and the code should return everything 
before the @ sign as their user name. For example, if someone 
enters ben@gmail.com, the code should return ben as their 
user name. """


def user_name():
    email = input('Introduzca su email: ')
    for i in range(0, len(email)):
        if email[i] == '@':
            return email[:i]
    return None


# *** Testing the function ***
print('user_name:', user_name())


""" Extra Challenge: Zero Both Ends
Write a function called zeroed code that takes a list of 
numbers as an argument. The code should zero (0) the first 
and last number in the list. For example, if the input is [2, 5, 
7, 8, 9], your code should return [0, 5, 7, 8, 0] """


def zeroed(int_list):
    int_list[0] = 0
    int_list[-1] = 0
    return int_list


# *** Testing the function ***
print('--- PART 2 ---')
numbers = [2, 5, 7, 8, 9]
print('zeroed: ', zeroed(numbers))
