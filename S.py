# Strings
import datetime

s = 'Winner!'
adjective = "Winning"
names = ['Bob', 'John', 'Todd']
spaces = "     yellow  "
dimensions = '1280*1024'
salutation = "Hello and welcome to our home"
title = "the big lebowski"
student = {'name': 'Alex', 'age': 13, 'school': 'Reed Middle School'}
bingo = [('B', '16'), ('number', 'winner')]
percent = (12 / 5.2)
# New methods introduced somewhere around python 2.7


# Print string centered, with filler text on either side
print(s.center(50, '-'))  # old way
print('{:-^50}'.format(s))  # new way
# Right aligned to 50, using spaces as filler
print(s.rjust(50, " "))
print('{:>50}'.format(s))
# Left Aligned to 50, using * as filler
print(s.ljust(50, '*'))
print('{:*<50}'.format(s))
# Sub items into string with placeholders
# char after % represents the conversion type %s - string, %i integer, etc
print("Good %s %s to see you" % ('morning', 'happy'))  # old way
print("Good {} {} to see you".format('morning', 'happy'))  # new way

# Indexing
print('{}, {}, {}, {}'.format('North', 'East', 'West', 'South'))  # manual definition, default indexing
print('{3}, {2}, {1}, {0}'.format('North', 'East', 'West', 'South'))  # reversing the order by specifying index in {}s

# Use dictionary/list/etc in string formatting
print('%(name)s, age %(age)0d is attending %(school)s' % student)  # old way
print('{name}, age {age} is attending {school}'.format(**student))  # new way
print("Today's contestants are: {}, {}, and {}.".format(*names))  # using a list
print('The {toy} is {color}'.format(toy='ball', color='red'))  # named arguements
print("The next number is {0[0][0]}{0[0][1]}.  If you have this {0[1][0]} you may be the {0[1][1]}!".format(
    bingo))  # Tuples

# Sometimes you need to specify a format
print('{:,}'.format(123456789))  # use comma separation for numbers
print('%{:.2f}'.format(percent))  # format as percentage 2 decimal places
d = datetime.datetime(2016, 6, 29, 10, 30, 25)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))  # datetime object formatting

# Templating
from string import Template

states = [('Alabama', 'Montgomery'), ('Alaska', 'Juneau'), ('Arizona', 'Phoenix'), ('Arkansas', 'Little Rock')]

s = Template('The capital of $state is $capital')  # Set template identifiers with $

for t in states:
    print(s.substitute(state=t[0], capital=t[1]))  # .substititue replaces identifies with values

    #