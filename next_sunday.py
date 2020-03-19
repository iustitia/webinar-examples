import datetime as dt

sunday_weekday = 6

#############
"""
Wylicz datę najbliższej niedzieli w przyszłości
"""
#############

today = dt.date.today()
print(today.weekday())

diff = sunday_weekday - today.weekday()
if diff == 0:
    diff = 7

next_sunday = today + dt.timedelta(days=diff)
print(next_sunday)

