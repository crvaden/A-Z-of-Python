# Operators
from datetime import datetime
'''
+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~
<       >       <=      >=      ==      !=

# Arithmetic Operators

# Addition
print(4 + 5)
print('hello' + ' ' + 'world')
print(True + False)

# Subtraction
print(4 - 5)
print(True - False)

# Multiplication
print(4 * 5)
print('hello' * -2)
print(True * False)

# Exponentiation
print(5 ** 2)

# Division
print(5 / 2)
print(2 / 5)

# Floor
print(5 // 2)
print(2 // 5)

# Modulo
print(5.5 % 2)
print(2 % 5)

# Comparison Operators

# Equal

print(1 == 1)
print(1 == 2)
print('camel' == 'camel')


a = 'cat'
b = 'cat'
print(a == b)  # This is different than a is b, which we will cover later



# Not Equal
print(1 != 1)
print(1 != 2)
print('camel' != 'camel')
print(2*5 != 4*8)

# Deprecated Not Equal
# print(1 <> 1)

# Greater Than
print(1 > 2)
print(2 > 1)
print('two' > 'one')  # compared lexicographically using sum of ord(char) (unicode code point) for all chars
print(ord('t'))
print(ord('w'))  # in essence, words with more letters, or letters later in alphabet return higher scores

# Less Than
print(1 < 2)
print(2 < 1)

# Greater Than or Equal To
print(1 >= 2)
print(2 >= 1)
print(2 >= 2)

# Less Than or Equal To
print(1 <= 2)
print(2 <= 1)
print(2 <= 2)

# Assignment Operators

# Equals
a = 10
b = 20
a = b
print(a)
a = 10
b = 20
a = b = a  # values assigned from right to left
print(a)

# Plus and
a = 5
a += 2  # same as a = a + 2
print(a)
c = 'test'
c += '2'  # cannot add int to str, but can add int as str to str

print(c)
# Minus and
a = 5
a -= 4  # same as a = a - 4
print(a)
c = 'test'
# c -= 't'   # doesn't work (TypeError)
print(c)

# This works for the rest of the operators, such as * ** % // /



#  Membership Operators

# in
if 'a' in 'cat':
    print(True)

# if 1 in 12: # Fails because int is not iterable
    print(True)

if 1 in [1, 2, 3, 4, 5]:
    print(True)

d = {'color':'blue', 'material':'glass'}
if 'color' in d:  # or blue in d.values()
    print(True)

# not in
if 'a' not in 'owl':
    print(True)

if  1 not in [2, 3, 4, 5]:
    print(True)
'''

#Identity Operators

# is
print(1 is 1)
a = 'ball'
b = 'ball'
print(a is b)  # One might think a is not literally b, but it is because they are pointed to the same space in memory
               # This prevents having to compare every character in the string which is costly

b = ''.join(['b', 'a', 'l', 'l'])
print(b)
print(a is b)  # string literals take up the same memory space, but strings created other ways do not!

# is not
print(1 is not 1)

print(input("Enter a command: ") is not 'Exit')  # Will always evaulate to True because they do not point
                                                 # to the same object.  Use not in instead.


# Bitwise
# See video B

# Lambda
# See video L