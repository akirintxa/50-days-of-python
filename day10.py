""" Hide my Password
Write a function called hide_password that takes no
parameters. The function takes an input (a password) from a user
and returns a hidden password. For example, if the user enters
"hello" as a password, the function should return "****" as a
password and tell the user that the password is 4 characters
long. """


def hide_password():
    passw = input('Contraseña: ')
    hidden_passw = '*'*len(passw)
    print(f"{hidden_passw} the password is {len(passw)} characters long.")


hide_password()

""" PART 2
Extra Challenge: A Thousand Separator
Your new company has a list of figures saved in a database. The 
issue is that these numbers have no separator. The numbers are 
saved in a list in the following format: 
[1000000, 2356989, 2354672, 9878098].
You have been asked to write a code that will convert each of the 
numbers in the list into a string. Your code should then add a 
comma to each number as a thousand separator for 
readability. When you run your code on the above list, your output 
should be:
[ '1,000,000', '2,356,989', '2,354,672', '9,878,098']
Write a function called convert_numbers that will take 
one argument, the list of numbers above """


def convert_numbers(num_list):
    # Paso 1: Crear una lista vacía para almacenar los números formateados
    numeros_formateados = []

    # Paso 2: Iterar sobre cada número en la lista original
    for numero in num_list:
        # Paso 3: Convertir el número a una cadena y revertirlo para facilitar la inserción de comas
        numero_str = str(numero)[::-1]

        # Paso 4: Inicializar una cadena vacía para almacenar el número formateado con comas
        numero_formateado = ""

        # Paso 5: Iterar sobre cada dígito del número y agregar comas cada tres dígitos
        for i in range(len(numero_str)):
            if i % 3 == 0 and i != 0:
                numero_formateado += ","
            numero_formateado += numero_str[i]

        # Paso 6: Revertir nuevamente el número formateado para que esté en el orden correcto
        numero_formateado = numero_formateado[::-1]

        # Paso 7: Agregar el número formateado a la lista de números formateados
        numeros_formateados.append(numero_formateado)

    # Paso 8: Retornar la lista de números formateados
    return numeros_formateados


# *** Testing the function ***
print('--- PART 2 ---')
lista = [1000000, 23569891287, 2354672, 9878098]
print('convert_numbers: ', convert_numbers(lista))
