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
import os
#import pytz

#tz = pytz.timezone("US/Pacific")
get_datetime = datetime.now()

def date_format():
  global get_datetime
  get_datetime = datetime.now()
  month = str(get_datetime.date().month)
  day = str(get_datetime.date().day)
  year = str(get_datetime.date().year)
  result = month + "-" + day + "-" + year
  return result

def time_format():
  global get_datetime
  get_datetime = datetime.now()
  h = get_datetime.hour
  converted_h = 0
  convert_h = h > 12
  add_zero_to_h = ""
  meridiem = ""

  if convert_h:
    converted_h = h - 12
    meridiem = "PM"
  elif h == 12:
    meridiem = "PM"  
  else:
    meridiem = "AM"  
  
  if h < 10:
    add_zero_to_h = "0"

  end_h = add_zero_to_h + str(converted_h)   

  m = get_datetime.minute
  add_zero_to_m = ""

  if m < 10:
    add_zero_to_m = "0"

  end_m = add_zero_to_m + str(m)  

  s = get_datetime.second

  add_zero_to_s = ""

  if s < 10:
    add_zero_to_s = "0"

  end_s = add_zero_to_s + str(s)  

  formatted_time = end_h + ":" + end_m + ":" + end_s + " " + meridiem
  return formatted_time # return a string with final time formatting

def clear_console():
  os.system('cls')

# print formatted results by calling the date_format() and time_format() functions
print (" Date: \n",date_format(),"\n\n", "Time: \n",time_format())

def reprint_datetime():
  global get_datetime
  get_datetime = datetime.now()
  refresh = input()
  if refresh == "e":
    print (" Date: \n",date_format(),"\n\n", "Time: \n",time_format())
    return
  else:
    clear_console()
    print("try again")
    reprint_datetime()

print("\n", "Press (e) to display time again")
reprint_datetime()
