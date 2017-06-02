import pickle, urllib2
"""This level deals with pickled(peak hell) data

There is a link in the source code that  contains pickled data.
First you have to find the link itself.
You then unpickle the data and join the resulting list.
The list is a list of lists that is a list of tuples.

Hint: It is a tuple of a string and a number.
      What if the number is the number of times the string is repeated.
      Once you've got this then join the resulting string.
"""

link = 'http://www.pythonchallenge.com/pc/def/banner.p'

page = urllib2.urlopen(link)

data = page.read()

p = pickle.loads(data)

packed = []

for sub_list in p:
    print"".join([k * v for k, v in sub_list])
