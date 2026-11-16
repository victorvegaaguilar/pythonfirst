#### Dates ####

from datetime import datetime, time, date, timedelta

now = datetime.now()



timestamp = now.timestamp()
print(timestamp)

year_2026 = datetime(2026, 11, 15)
print(year_2026)

def print_date(date):
    print(date)
    print(date.hour)
    print(date.minute)
    print(date.second)

    print(date.year)
    print(date.month)
    print(date.day)

print_date(year_2026)

current_time = time(21, 6, 1)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date2 = date(current_date.year + 1, current_date.month + 1, current_date.day + 1)
print(current_date2)


diff = year_2026 - now
print(diff)

diff = year_2026.date() - now.date()
print(diff)


start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)