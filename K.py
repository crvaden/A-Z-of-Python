

import requests
# KWARGS (AND) ARRRRRGGGS

# args takes any number of inputs and produces a tuple that can be iterated over
def math(*args):
    print(args)
    for i in args:
        print(i* 5)

math(1, 2, 3)

# kwargs takes keyword arguements and turns them into a dictionary
def fruits(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)

fruits(apple='red', banana='yellow', pear='green')
token = 'sdfasfsdf'

# These can be helpful when you're not sure how many parameters will be passed
# such as when calling an API with many optional parameters.
def fetch_data(token, user_id, **kwargs):
    url = 'api.whateversite.com/'
    r = requests.get(url, params=kwargs)

fetch_data(token, '6454', start_date='2015-05-01', end_date='2015-06-01', zip='30341')