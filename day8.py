""" Odd and Even
Write a function called odd_even that has one parameter and 
takes a list of numbers as an argument. The function returns the 
difference between the largest even number in the list and the 
smallest odd number in the list. For example, if you pass [1, 2, 4,
6] as an argument, the function should return 6 - 1= 5. """


def odd_even(int_list):
    odd_numbers = []
    even_numbers = []
    for number in int_list:
        if number % 2 == 0:
            even_numbers.append(number)
        elif number != 0:
            odd_numbers.append(number)
    max_even = max(even_numbers)
    min_odd = min(odd_numbers)
    return max_even - min_odd


numbers = [7, 2, 8, 4, 6, 0]
print(odd_even(numbers))


""" PART 2
Extra Challenge: List of Prime Numbers
Write a function called prime_numbers. This function asks the
user to enter a number (an integer) as an argument and returns a 
list of all the prime numbers within its range. For example, if the 
user enters 10, your code should return [2, 3, 5, 7] as prime 
numbers """


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def prime_numbers(top):
    primes = []
    if top <= 1:
        return None
    for number in range(2, top + 1):
        if is_prime(number):
            primes.append(number)
    return primes


# *** Testing the function ***
print('--- PART 2 ---')
data = int(input('Introduzca el tope: '))
print('prime_numbers: ', prime_numbers(data))
