import json
import requests
# JSON

# Create a dictionary
player_salaries = {'players': [{'position': 'RB', 'salary': 2300000}, {'position': 'QB', 'salary': 7400000}]}

# Standard dictionary, we can access individual components as expected
print(player_salaries)
print(player_salaries['players'])

# A solid understanding of navigating nested dicts/lists is important to working with JSON objects
# Specify dict keys and list indicies to narrow down to specific data
print(player_salaries['players'][0]['position'])

# You can loop through the list in this manner
for i in player_salaries['players']:
    print(i['position'], i['salary'])

# Lets turn his dict into JSON
json_salaries = json.dumps(player_salaries)

# json.dumps converts the object into a string, which can be passed over the internet or to a database
print(json_salaries)


# These print exactly the same, so what's the difference?
# The first is still an object
# The second is now a string
print(player_salaries)
print(json_salaries)

# Write data to file
# First option attempts to write a dictionary to the file, which is an invalid operation
# but dumping it to the file as JSON work, because it converts the object to a string
with open('data.txt', 'w') as f:
    # f.write(player_salaries)
    json.dump(player_salaries, f)

# Read data from file
# This operation converts the string back into an object so we can work with the data
with open('data.txt') as f:
    data = json.load(f)

# Proving that it is in object by specifying a key
print(data['players'])

# You can print your JSON in a more readable format
print(json.dumps(player_salaries, sort_keys=True, indent=4))

# Lets try to fetch some actual JSON data from a real API
url = 'https://tidesandcurrents.noaa.gov/api/datagetter?station=8722670&date=today&units=english&time_zone=lst&product=water_temperature&format=json'
r = requests.get(url).json()

# We can either use the pretty print function above, or a browser addon to prettify the JSON to make it easier to find
# individual components

# In this example we can find the first temperature reading with the following command
print(r['data'][0]['v'])

# We can iterage through every temperature reading like so
for i in r['data']:
    print(i['v'])