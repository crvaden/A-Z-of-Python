from itertools import *

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# chain()
# groups together multiple lists into one single iterable

# They can be looped over
for i in chain(a, b, c):
    print(i)

# Or printed all at once
print(list(chain(a, b, c)))

#  You can speficy the range with brackets
print(list(chain(a[:1], b[:1], c[0:2])))

# count()
# spits out a continuous stream of numbers, starting at the first argument,
# incrementing by the second
# This will go on forever, so you have to specify a method to stop the loop
for i in count(1, .5):
    print(i)
# islice()
# Will grab a specified number of items
# Arguements are start, stop, and size of iteration
for i in islice(count(), 0, 101, 5): # Count from 0-100, by 5
    print(i)



# compress()
# Print first and last values in a, by using a binary filter
binary_values = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
for i in compress(a, binary_values):
    print(i)

# Moved from itertools to global functions

# filter
# Generator used to produce evens vs filter() used to produce evens
# filter() returns values that return true, or in this case 1 (mod 2 returns 1 for odd numbers)
evens = [x for x in a if x % 2 == 0]
odds = list(filter(lambda x: x % 2, a))
print(evens)
print(odds)


map()
Sends each item in list to a function
def square(x):
    return x ** 2


for i in map(square, a):
    print(i)

# Lambda can be used to modify a list without having to create a full fledged function
for i in map(lambda x: x ** 2, a):
    print(i)


