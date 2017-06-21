from calendar import weekday, isleap

print filter(lambda y: isleap(y) and 0 == weekday(y, 1, 26), range(1006, 2000, 10))[-2]
