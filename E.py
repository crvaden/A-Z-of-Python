

# Exception Handling

# Fraction to Decimal

while True:
    try:
        numerator = int(input('Please enter your numerator value: '))
        denominator = int(input('Please enter your denominator value: '))

        decimal = numerator / denominator

    except ZeroDivisionError:
        print("You can't divide by zero, enter new numbers.")
    except ValueError:
        print('Please enter number in integer form (ex: 1-9).')
    else:
        print('Your fraction in decimal form is: ', numerator / denominator)
        break

