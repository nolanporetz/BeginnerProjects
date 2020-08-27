opening = """
Welcome to the Armstrong Number Test!\n\n
An Armstrong Number is an integer that is equal to the sum\n
of its own digits raised to the power of the number of digits.\n\n
We can represent this with the 3 digit number 'xyz' \n
raised to the power of n (which equals 3 since xyz is 3 digits):\n
x^3 + y^3 + z^3 = xyz \n\n
Similarly, a 5 digit number 'abxyz' would have an n of 5. \n
For abxyz to be an armstrong number, the following equation would hold true: \n
a^5 + b^5 + x^5 +y^5 + z^5 = abxyz. \n\n
A real example, 153:\n
1^3 + 5^3 + 3^3 = 153\n\n
Now try it yourself! (Note: all single digit numbers are armstrong numbers.)
"""

print(opening)

while True:
    def lance():
        if n == 5:
            return armstrong_five()
        elif n == 4:
            return armstrong_four()
        elif n == 3:
            return armstrong_three()
        elif n == 2:
            return armstrong_two()
        elif n == 1:
            return armstrong_one()
        else:
            print('Make sure you type a number and it has no more than 5 digits.')


    def armstrong_five():
        print('You have entered a valid, 5-digit number.  Here are your results: ')
        print('n = ', n)
        a = int(user_input[0])
        print('a = ', a)
        b = int(user_input[1])
        print('b = ', b)
        x = int(user_input[2])
        print('x = ', x)
        y = int(user_input[3])
        print('y = ', y)
        z = int(user_input[4])
        print('z = ', z)
        equation_5 = a ** n + b ** n + x ** n + y ** n + z ** n
        print('Equation = a^n + b^n + x^n + y^n + z^n = ?')
        print(a, '^', n, '+', b, '^', n, '+', x, '^', n, '+', y, '^', n, '+', z, '^', n, '= ?')
        print(a ** n, '+', b ** n, '+', x ** n, '+', y ** n, '+', z ** n, '= ?')
        print('= ', equation_5)
        if str(equation_5) == user_input:
            return print(user_input, ' is equal to ', equation_5, ' Congratulations! You found an Armstrong number!')
        else:
            print(user_input, ' is not an Armstrong number.  Try again!')


    def armstrong_four():
        print('You have entered a valid, 4-digit number.  Here are your results: ')
        print('n = ', n)
        a = int(user_input[0])
        print('a = ', a)
        b = int(user_input[1])
        print('b = ', b)
        x = int(user_input[2])
        print('x = ', x)
        y = int(user_input[3])
        print('y = ', y)
        equation_4 = a ** n + b ** n + x ** n + y ** n
        print('Equation = a^n + b^n + x^n + y^n = ?')
        print(a, '^', n, '+', b, '^', n, '+', x, '^', n, '+', y, '^', n, '= ?')
        print(a ** n, '+', b ** n, '+', x ** n, '+', y ** n, '= ?')
        print('= ', equation_4)
        if str(equation_4) == user_input:
            return print(user_input, ' is equal to ', equation_4, ' Congratulations! You found an Armstrong number!')
        else:
            return print(user_input, ' is not an Armstrong number.  Try again!')


    def armstrong_three():
        print('You have entered a valid, 3-digit number.  Here are your results: ')
        print('n = ', n)
        a = int(user_input[0])
        print('a = ', a)
        b = int(user_input[1])
        print('b = ', b)
        x = int(user_input[2])
        print('x = ', x)
        equation_3 = a ** n + b ** n + x ** n
        print('Equation = a^n + b^n + x^n = ?')
        print(a, '^', n, '+', b, '^', n, '+', x, '^', n, '= ?')
        print(a ** n, '+', b ** n, '+', x ** n, '= ?')
        print('= ', equation_3)
        if str(equation_3) == user_input:
            return print(user_input, ' is equal to ', equation_3, ' Congratulations! You found an Armstrong number!')
        else:
            return print(user_input, ' is not an Armstrong number.  Try again!')


    def armstrong_two():
        print('You have entered a valid, 2-digit number.  Here are your results: ')
        print('n = ', n)
        a = int(user_input[0])
        print('a = ', a)
        b = int(user_input[1])
        print('b = ', b)
        equation_2 = a ** n + b ** n
        print('Equation = a^n + b^n = ?')
        print(a, '^', n, '+', b, '^', n, '= ?')
        print(a ** n, '+', b ** n, '= ?')
        print('= ', equation_2)
        if str(equation_2) == user_input:
            return print(user_input, ' is equal to ', equation_2, ' Congratulations! You found an Armstrong number!')
        else:
            return print(user_input, ' is not an Armstrong number.  Try again!')


    def armstrong_one():
        print('You have entered a valid 1-digit number.  Here are your results: ')
        print('All 1-digit numbers are armstrong numbers!  You can try again.')
        return user_input


    print('Enter a number below (must be less than 6 digits for this program to work): ')

    user_input = input("Enter number:  ")

    num = int(user_input)
    n = 0
    while num != 0:
        n += 1
        num //= 10
    print('Your number = ', user_input, 'n = ', n)
    if 0 < n < 6:
        lance()
    else:
        print('Please enter a valid number.')

