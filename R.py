import re
# Important Tokens
# [aeiou] - Match any of these characters
# [a-z] - Match any character in the range
# [^aeiou] or [^a-z] - Match any character NOT in the list or range
# . Match any single character
# \s \S \d \D \w \W - Whitespace char, non-whitespace char, digit, non-digit, word, non-word
# a* a+ a{5} a{5,} a{2,6} - zero or more, one or more, exactly 5, 5 or more, 2 to 6
#

#Important Methods
# re.search(pattern, string, flags) - returns none or match object, can be used in if statements
# re.match(pattern, string, flags) - same as search, but will only match from the start of the string
# re.fullmatch(pattern, string, flags) - requires entire string to match (very handy) eliminates ^ $
# re.findall(pattern,string, flags) - returns list of strings (or tuples if you use groups) of non-overlapping matches
# re.finditer(pattern, string, flags) - returns iterable match object of non-overlapping matches
# re.sub(pattern, repl, string, count, flags)

# Covering search, match, and sub
s = "Who wants to go to the park if it rains?"

# Returns first s
print(re.search('s', s))
# Fails because string does not start with s
print(re.match('s', s))
# replace all instances of s with $
print(re.sub('s', '$', s))
# Returns all instances of s


# Password Complexity Check
# Ask user for password, and verify it is 8 characters, has a capital letter, number, and special character

# List part at the end is the typical regex component - at least 8 of any of these characters
# The 4 groups are lookahead assertions, checking of they exist but not consuming the string
# ^ and $ indicate that the beginning and end of the string, so the
# ?= is a positive lookahead assertion, telling the regex to return match/nomatch for the following group
# the lookahead does not consume anything, so once it passes, the next item will have the entire string to work with
# .* is a greedy quantifier, matching all of . (any character), meaning it matches the entire string
# Then it works backwards, one character at a time, until it matches [A-Z], at which point the assertion passes
# and the regex moves forward.
# Each lookahead assertion must pass before the part of the regex that consumes the string can begin, at which point
# the regex looks for 8 or more of the characters in the final set of brackets.

# There are several pattern methods for compiles regex patterns (pattern.findall())

pattern = re.compile(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[$@$!%*#?&.])[A-Za-z\d$@$!%*#?&.]{8,}')
while True:
    user_pass = input('Enter a secure password: ')
    if pattern.fullmatch(user_pass): # use fullmatch method to avoid having to pass in pattern
        print('Successfully changed password')
        break
    else:
        print('Not secure enough. Ensure pass is 8 characters long with at least one upper and lowercase letter, number,'
              ' and special character.')


# regex object can be used repeatedly when iterating over a list
# Check a list of passwords to see if they pass our requirements
pw_list = ['1Ki77y', '.Susan53', 'jelly22fi$h', '$m3llycat', 'a11Black$']

for pw in pw_list:
    if pattern.match(pw):
        print(pw, 'pass')
    else:
        print(pw, 'fail')


# Text copied form wikipedia article on email addresses
# Open, read, and apply regex to string
# findall / finditer work the same, except you have extra info with finditer
f = open('emails.txt', 'r')
r = f.read()
# findall returns list of non-overlapping matches, great for finding all occurrences of something in a string
regular_matches = re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,})', r)
# finditer returns an iterable match object, which contains match position info
iter_matches = re.finditer(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,})', r)

print(regular_matches)
for i in regular_matches:
    print(i)

print(iter_matches)
for i in iter_matches:
    print(i)


