calculations = []

def add(a, b):
    calculations.append(a + b)
    print('The result is: ', a + b)

def subtract(a, b):
    calculations.append(a - b)
    print('The result is: ', a - b)

def multiply(a, b):
    calculations.append(a * b)
    print('The result is: ', a * b)

def divide(a, b):
    try:
        calculations.append(a / b)
        print('The result is: ', a / b)
    except ZeroDivisionError:
        print('Error: Division by zero is not allowed.')

def show_history():
    print('Here are the calculations you have done so far:')
    for i, result in enumerate(calculations):
        print(f'{i+1}. {result}')

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))

    if operation == '+':
        add(number_1, number_2)
    elif operation == '-':
        subtract(number_1, number_2)
    elif operation == '*':
        multiply(number_1, number_2)
    elif operation == '/':
        divide(number_1, number_2)
    else:
        print('You have not typed a valid operator, please run the program again.')

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

def welcome():
    print('''
Welcome to Calculator
''')

welcome()
calculate()
again()
show_history()
