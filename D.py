# Dates and Times
from datetime import datetime
from time import time

# Datetimes
# Current datetime
current_datetime = datetime.now()
print('It is currently:', current_datetime)

# Print individual attributes
print('Current year:', current_datetime.year)
print('Current month:', current_datetime.month)
print('Current day:', current_datetime.day)
print('Current hour:', current_datetime.hour)
print('Current minutes:', current_datetime.minute)
print('Current seconds:', current_datetime.second)

# Use string formatting to output date in specific format
print("Today's date is: {:%d %B, %Y}".format(current_datetime))

# Parse string into a datetime object
anniversary_date = datetime.strptime('Jan 15, 2017, 16:14 PM', '%b %d, %Y, %H:%M %p')

# Use string formatting to output date in specific format
print('Our anniversary date is: {:%d %B, %Y}'.format(anniversary_date))

# Epoch time
epoch_time = time()

# Print current epoch time
print('The current epoch time is:', epoch_time)

# Calculate the number of years since epoch
print('Years since epoch:', (epoch_time / 60 / 60 / 24 / 365))

# Print epoch as datetime
epoch_to_datetime = datetime.fromtimestamp(epoch_time)
