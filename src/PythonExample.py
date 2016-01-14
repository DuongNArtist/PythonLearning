'''
    multiline comment
'''
# single line comment
total_secs = 7684
print("Total Secs = " + str(total_secs))
hours = total_secs / 3600
print("Hours = " + str(hours))
secs_still_remaining = total_secs % 3600
print("Secs Still Remaining = " + str(secs_still_remaining))
minutes = secs_still_remaining / 60
print("Minutes = " + str(minutes))
