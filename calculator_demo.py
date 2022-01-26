# Peforms simple calculation.

# using fuctions to set the adding and subtraction when
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def division(num1, num2):
    return num1 / num2

def multiplication(num1, num2):
    return num1 * num2

def modulo(num1, num2):
     return num1 % num2

choose_operator = int(input('Select an operator. 1(+) 2(*) 3(/) 4(-) 5(%)'))

choice_of_first_number = int(input('Enter First Number.'))
choice_of_second_number = int(input('Entewr Second Number.'))


#select inputs the user numbers and then user must choose wheter to 
#divide or subtract etc.

if choose_operator == 1:
    print("The answer to your addition question is.") 
    print((addition)(choice_of_first_number, choice_of_second_number))

elif choose_operator == 2:
    print("The answer to your multiplication question is.") 
    print(multiplication(choice_of_first_number, choice_of_second_number))

elif choose_operator == 3:
    print("The answer to your division question is.") 
    print(division(choice_of_first_number, choice_of_second_number))

elif choose_operator == 4:
    print("The answer to your subtraction question is.") 
    print(subtraction(choice_of_first_number, choice_of_second_number))

elif choose_operator == 5:
    print("The answer to your modulo question is.") 
    print(modulo(choice_of_first_number, choice_of_second_number))

else:
    print("Invalid Input.")

