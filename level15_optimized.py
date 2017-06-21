import datetime, calendar

for year in range(1006, 2000, 10):
    d = datetime.date(year, 1, 26)

    if d.isoweekday() == 1 & calendar.isleap(year):
        print(d)
