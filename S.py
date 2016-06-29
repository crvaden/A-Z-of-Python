
# String formatting
from string import Template
states = [('Alabama', 'Montgomery'), ('Alaska', 'Juneau'), ('Arizona', 'Phoenix'), ('Arkansas', 'Little Rock')]

s = Template('The capital of $state is $capital.')

for t in states:
    print(s.substitute(state=t[0], capital=t[1]))

