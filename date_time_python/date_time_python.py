#
# FILE HEADER #
#
# This python script will display the  current local date and time if ran from installed IDE
# Note: online IDEs like Repl.it will show time data for their server by default, not your local time.
#   to specify a timezone, import pytz and create a timezone variable to feed in to datetime.now() as a parameter.
#   EX: import pytz
#       tz = pytz.timezone('US/Pacific')
#       get_now = datetime.now(tz)
#
# Time format: (12H) {H}:{M}:{S} {meridiem}
# Date format: {MM}-{DD}-{YYYY}
#

from datetime import datetime

get_now = datetime.now()
h = get_now.hour
m = get_now.minute
s = get_now.second
is_pm = h > 11
meridiem = ""
convert_to_12_h = h > 12
twelve_hour_time = h

if h>12:
  twelve_hour_time -= 12

if is_pm:
  meridiem = "PM"
else:
  meridiem = "AM"

time_format = ""

if twelve_hour_time < 10 and m > 9 and s > 9:
  time_format = "Current time: \n0{}:{}:{} "
elif m < 10 and twelve_hour_time > 9 and s > 9:
  time_format = "Current time: \n{}:0{}:{} "
elif s < 10 and twelve_hour_time > 9 and m > 9:
  time_format = "Current time: \n{}:{}:0{} "
elif twelve_hour_time < 10 and m < 10 and s > 10:
  time_format = "Current time: \n0{}:0{}:{} "
elif twelve_hour_time < 10 and m < 10 and s < 10:
  time_format = "Current time: \n0{}:0{}:0{} "
elif m < 10 and s < 10 and twelve_hour_time > 10:
  time_format = "Current time: \n{}:0{}:0{} "
elif twelve_hour_time < 10 and m > 9 and s < 10:
  time_format = "Current time: \n0{}:{}:0{} "
else:
  time_format = "Current time: \n{}:{}:{} "

formatted_time = time_format.format(twelve_hour_time, m, s) + meridiem


# print the final result for current time
print(formatted_time + "\n")

month = get_now.date().month
day = get_now.date().day
year = get_now.date().year
date_info = "Current date: \n{}-{}-{}".format(month, day, year)

# print the result for current calendar date
print(date_info)
