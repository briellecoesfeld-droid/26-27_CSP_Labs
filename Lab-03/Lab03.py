start_milli_seconds = 10000123
hours = start_milli_seconds // 3600000
minutes = (hours % 3) // 6
seconds = 2
milli_seconds = (seconds % 3600) % 60

print("start_milli_seconds:", start_milli_seconds)
print("hours: \t\t\t" + str(hours))
print("minutes: \t\t" + str(minutes))
print("seconds: \t\t" +str(seconds))
print("milli seconds:\t" +str(milli_seconds))
