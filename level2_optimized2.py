import urllib2
"""This solution assumes rare to be the least occuring. It maps out the occurence of the characters and then finds the characters that occur the least number of times and uses that.


By splitting the raw_data using "<!--" we get three separate lists.
We're only interested in the third list hence "[2]"

rstrip() removes any whitespace from the end of the text (https://www.tutorialspoint.com/python/string_rstrip.htmhttps://www.tutorialspoint.com/python/string_rstrip.htm). It only leaves the text that we need. Doing line.rstrip removes the whitespace line by line. We join to remove any whitespace within the line itself so that we have one continuous block.

.get() method reference: https://stackoverflow.com/questions/2068349/understanding-get-method-in-python

We put the number of occurences of each character into a dictionary with the key as the character and the value as the number of occurences.
"""

page = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')

raw_data = page.read()

data = raw_data.split('<!--')[2]

s = ''.join([line.rstrip() for line in data])

OCCURENCES = {}

for c in s: OCCURENCES[c] = OCCURENCES.get(c, 0) + 1

min_val = min(OCCURENCES.itervalues()) # Iterate through the dictionary values(itervalues) and get the least value(min)

print ''.join([c for c in s if OCCURENCES[c] == min_val])
