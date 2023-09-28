
import value_return

hour = value_return.get_hour(3800)
minutes = value_return.get_minutes(3800)
seconds = value_return.get_seconds(3800)

time = (f"{hour:02d}:{minutes:02d}:{seconds:02d}")
# using an f-string makes concatenation easier to read & format
# 02d displays hour, mins, & seconds with two digits
print(time)
