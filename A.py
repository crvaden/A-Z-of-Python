import numpy as np
# Arrays

# List
# Create list of integers
a = [1, 2, 3, 4, 5]

# Print list
print('Print the entire list:')
print(a)
print('')

# Iterate through list
print('Print each item in list, one at a time:')
for i in a:
    print(i)
print('')

# Attempting math functions on list
print('Math operations on lists have an unexpected behavior, and may not be suitable for mathematical use')
print('a * 2 = ', a*2)
print('')

# Dictionaries
# Create dictionary with personal measurements
b = {
    'Name': 'Alex',
    'Age': 25,
    'Height': 55,
    'Weight': 145
}

# Print dictionary
print('Print entire dictionary:')
print(b)
print('')

# Loops through dict, printing both the key and value, separated by :
print('Print each dictionary key:pair value on a new line:')
for i in b:
    print(i, ':', b[i])
print('')

# NumPy arrays for mathematical use
# Create NumPy array with integers
c = np.array([1, 2, 3])

# Print NumPy array
print('Print entire NumPy array:')
print(c)
print('')

# Demonstrate math operations on NumPy array
print('Math functions work as expected if you use a NumPy array:')
print('c * 2.23 = ', c * 2.23)

