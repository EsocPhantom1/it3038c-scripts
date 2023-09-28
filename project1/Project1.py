#Lisa, T (2021) How To Make a Calculator Program in Python 3 (Version 2) [Computer Program], https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3

def welcome():
    print('''
Welcome to Calculator
''')

# Don’t forget to call the function
welcome()

def calculate():
    while True:
        operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
% for modulo
C to clear
Enter 'exit' to quit.
''')

        if operation == 'exit':
            print('See you later.')
            break

        if operation == 'C':
            continue #start new calculation

        try:
            number_1 = float(input('Please enter the first number: '))
            number_2 = float(input('Please enter the second number: '))
        except ValueError:
            print('Invalid input. Please enter valid numbers.')
            continue

        if operation == '+':
            print('{} + {} = '.format(number_1, number_2))
            print(number_1 + number_2)

        elif operation == '-':
            print('{} - {} = '.format(number_1, number_2))
            print(number_1 - number_2)

        elif operation == '*':
            print('{} * {} = '.format(number_1, number_2))
            print(number_1 * number_2)

        elif operation == '/':
            if number_2 == 0:
                print("Error! Division by zero is not allowed.")
            else:
                print('{} / {} = '.format(number_1, number_2))
                print(number_1 / number_2)

        elif operation == '**':
            print('{} ** {} = '.format(number_1, number_2))
            print(number_1 ** number_2)

        elif operation == '%':
            if number_2 == 0:
                print("Error! Modulo by zero is not allowed.")
            else:
                print('{} % {} = '.format(number_1, number_2))
                print(number_1 % number_2)

        else:
            print('You have not typed a valid operator.')

# Call the calculate function to start the calculator
calculate()
