import datetime
import calendar

"""
We are given the date as January 26th and only the first and last numbers of the year (1xx6)
This means we have a range of between 1006 and 1996 to look through.
All the years under consideration must end with a 6
At the bottom of the year we notice that February ends on the 29th, meaning it is a leap year.
We are looking for years between 1006 and 1996 that end with a 6 and are perfectly divisible by 4.
If you start from 1016 and increment by 20 years the resulting years are divisible by 4.

We are given a hint he ain't the youngest he is the second.
We will assume second refers to second youngest.
Given all the years who would be the youngest and who would be the second youngest by age.
Another hint we are given is a to do list for the following day.
<!-- todo: buy flowers for tomorrow -->
Google what day the following day is

Refer to : https://stackoverflow.com/questions/9847213/which-day-of-week-given-a-date-python
         : https://stackoverflow.com/a/1504848 explains why is did not work in
            if calendar.day_name[date_of_interest.weekday()] is 'Monday':
                print date_of_interest
"""
i = 1016

years = []

while i <= 1996:
    years.append(i)

    i += 20

for n in years:
    date_of_interest = datetime.date(n, 1, 26)
    if date_of_interest.weekday() == 0:
        print date_of_interest 

 # calendar.day_name[date_of_interest.weekday()]) gives day of the week in words
