import datetime as dt

sunday_weekday = 6

#############
"""
Wylicz datę najbliższej niedzieli w przyszłości
"""

#############

now = dt.date.today()
print(now.weekday())

diff = sunday_weekday - now.weekday()
if diff == 0:
    diff = 7

next_sunday = now + dt.timedelta(days=diff)
print(next_sunday)
