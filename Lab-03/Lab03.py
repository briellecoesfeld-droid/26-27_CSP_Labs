starting_milliseconds = 10000123
print("starting_milliseconds:\t" + str(starting_milliseconds))

# hours to milliseconds
hours = starting_milliseconds // 3600000
print("hours:\t\t\t\t\t" + str(hours))

# milliseconds left after the hours taken out
milliseconds_left = starting_milliseconds % 3600000

# minutes
minutes = milliseconds_left // 60000
print("minutes:\t\t\t\t" + str(minutes))

# milliseconds left
milliseconds_left = milliseconds_left % 60000

# second
seconds = milliseconds_left // 1000
print("seconds:\t\t\t\t" + str(seconds))

# remaining balance to ending milliseconds
milliseconds_left = milliseconds_left % 1000
print("milliseconds_left:\t\t" + str(milliseconds_left))
