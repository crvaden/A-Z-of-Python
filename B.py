# Bitwise Operators
#
# Counting in Binary - Right to left, binary values with bits of 1 are added to total
#
# |     |     |    |    |    |   |   |   |   |
# --------------------------------------------
# | 256 | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
# --------------------------------------------
# |     |     |    |    |    |   |   |   |   |
#
# 110110 = (right to left) 0 + 2 + 4 + 0 + 16 + 32 = 54

# Convert both ways
print('\n', '------------------------------------------', '\n')
print('Converting to and from binary:')
print('54 converted to binary is:', "{0:b}".format(54))  # int to binary
print('110110 converted to int is:', int('110110', 2))   # binary to int
print('')

# Assign variables for exercise
x = 27
y = 12

# Print variables for exercise
print('The values for x, y for this exercise are:')
print('x = ', x)
print('y = ', y)
print('\n', '------------------------------------------', '\n')

# x << y
# Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros).
# This is the same as multiplying x by 2**y.
print(x, '<< 2 =', x << 2)
print('In binary:')
print(' ', "{0:b}".format(x), '<-- shift to the left two places')
print("{0:b}".format(x << 2), '<-- results in larger number')
print('\n', '------------------------------------------', '\n')

# x >> y
# Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
print(x, '>> 2 =', x >> 2)
print('In binary:')
print("{0:b}".format(x), '--> shift to the right 2 places')
print(' ', "{0:b}".format(x >> 2), '<-- results in smaller number')
print('\n', '------------------------------------------', '\n')

# x & y
# Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0
print(x, '&', y, '=', x & y)
print('In binary:')
print("{0:b}".format(x), '||| compare each bit - if both = 1, output bit = 1, else output bit = 0')
print('', "{0:b}".format(y), 'vvv')
print('-----')
print('', "{0:b}".format(x & y), '<-- results in equal or smaller number')
print('\n', '------------------------------------------', '\n')

# x | y
# Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
print(x, '|', y, '=', x | y)
print('In binary:')
print("{0:b}".format(x), '||| compare each bit - if both = 0, output bit = 0, else output = 1')
print('', "{0:b}".format(y), 'vvv')
print('-----')
print("{0:b}".format(x | y), '<-- results in number equal or larger than either individual number')
print('\n', '------------------------------------------', '\n')

# ~ x
# Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1.
# This is the same as -x - 1.
print('~', x, '=', ~x)
print('In binary:')
print('', "{0:b}".format(x), '<-- switch each bit to its complement')
print("{0:b}".format(~x), '<-- result is equal to -x -1')
print('\n', '------------------------------------------', '\n')
# x ^ y
# Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0,
#  and it's the complement of the bit in x if that bit in y is 1.

print(x, '^', y, '=', x ^ y)
print('In binary:')
print('{0:b}'.format(x), '||| compare each bit - output bit = x bit if y bit = 0, '
                         'else output bit is the complement of x bit.')
print('', '{0:b}'.format(y), 'vvv')
print('{0:b}'.format(x ^ y))
print('\n', '------------------------------------------', '\n')

print('Using XOR for indexing, example')
print('Values: Single/Married, Male/Female, Minor/Adult')
smm = 0
sma = 1
mfa = 7

person1 = 0 ^ mfa
print('{:03b}'.format(person1))
