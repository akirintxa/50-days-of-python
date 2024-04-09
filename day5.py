""" PART 1 
My Discount
Create a function called my_discount. The function takes no 
arguments but asks the user to input the price and the discount
(percentage) of the product. Once the user inputs the price and 
discount, it calculates the price after the discount. The function 
should return the price after the discount. For example, if the user 
enters 150 as the price and 15% as the discount, your function 
should return 127.5. """


def my_discount():
    price = int(input('Indica el precio del producto: '))
    discount = int(input('Indica el descuento a aplicar: '))
    return price*(1-discount/100)


# *** Testing the function ***
print('calculate discount: ', my_discount())

""" PART 2
Extra Challenge: Tuple of Student Sex
You work for a school, and your boss wants to know how many 
female and male students are enrolled in the school. The school has 
saved the students on a list. Your task is to write a code that will 
count how many males and females are in the list. Here is a list 
below:
students = ['Male', 'Female', 'female', 'male', 'male', 'male',
'female', 'male', 'Female', 'Male', 'Female', 'Male', 
'female']
Your code should return a list of tuples. The list above should 
return: [("Male", 7), ("female", 6)]
 """


def count_sex(str_list):
    male = 0
    female = 0
    final_count = []
    for item in str_list:
        if item.lower() == "male":
            male += 1
        elif item.lower() == "female":
            female += 1
    final_count.append(('Male', male))
    final_count.append(('Female', female))
    return final_count


# *** Testing the function ***
print('--- PART 2 ---')
students = ['Male', 'Female', 'female', 'male', 'male', 'male',
            'female', 'male', 'Female', 'Male', 'Female', 'Male',
            'female']

print('count_sex: ', count_sex(students))
