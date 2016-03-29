# Generators
# Try running this program with a start of 1 and a stop of 100 to see everything in action

import sys
import itertools
import time

# Get start/stop range of x values
a = int(input('Input starting x value: '))
b = int(input('Input ending x value: '))
print('----------------------------------------------------------------------')


# Standard function approach
def line(start, stop):  # y = mx + b
    y = [(2 * x + 1) for x in range(start, stop)]
    return y

my_line = line(a, b)
print('Results as list and file size:')
print(my_line)
print('The list of y values is ', sys.getsizeof(my_line) / 1048576, ' MB')
print('----------------------------------------------------------------------')


# Converted to a generator with 'yield'
def line2(start, stop):  # y = mx + b
    for x in range(start, stop):
        y = 2 * x + 1
        yield y

my_line = line2(a, b)

# You can print as few or as many as you like, until you run out of results
# Manually print the first 4 results
print('First 4 results using generator and "next":')
print(next(my_line))
print(next(my_line))
print(next(my_line))
print(next(my_line))
print('----------------------------------------------------------------------')

# You can create a generator by using parenthesis - the yield is implied
y = ((2 * x + 1) for x in range(a, b))

print('Working in batches:')
# You can loop through the function and do all sorts of things
for n in y:
    try:
        for i in range(50):
            print(next(y))  # imagine this is building a JSON of 100 values and posting to API
        print('Waiting 5 seconds for next batch...')
        time.sleep(5)       # then pausing to avoid overloading the API
    except StopIteration:
        break
print('----------------------------------------------------------------------')


# It works for infinite loops too - take this example which can run forever
def line():
    x = 1
    while True:  # Starting at x = 1, yield values for y, one at a time, incrementing by 1 each time
        y = 2 * x + 1
        yield y
        x += 1

# Use islice to get a range back from the above function
print('Use itertools to get ranges of results:')
for n in itertools.islice(line(), 5):
    print(n)
print('----------------------------------------------------------------------')

# You can get any range you want, and you can even save them in a list with the list() function
print('You can start and stop anywhere you like, and even save the results to a list:')
y_values = list(itertools.islice(line(), 49, 100))
print(y_values)
print('----------------------------------------------------------------------')