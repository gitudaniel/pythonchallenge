import urllib2
"""
In this implementation, if the first 3 lines of a file are 'un:' or 'pw:', then retreive whatever is located at index 5 to the second last character and assign it to a variable.
"""

page = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/integrity.html')

for line in page:
    if line[:3] == 'un:': un = line[5:-2]
    if line[:3] == 'pw:': pw = line[5:-2]

username = un.decode('string_escape').decode('bz2')

password = pw.decode('string_escape').decode('bz2')

print 'The username is: {}\nThe password is: {}'.format(username, password)
