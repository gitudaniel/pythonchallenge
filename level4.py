import urllib2
import re
"""

This method assumes that you know nothing before hand and you cannot ascertain anything.
It builds everything as it goes.
The only assumption made is that you know you're looking for a link and that this is a html file.
You are basically opening the link you have and finding relevant information and dealing with it as required.

This method suffers from one main deficiency. It does catch the first error where we're supposed to divide by two in the try...except block but catches no other subsequent errors. You therefore have to scroll up to find what's different
"""

link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php' # The link given

page = urllib2.urlopen(link)

raw_data = page.read() # Read what is contained in the link
print raw_data

pattern = '<a href="(.*?)">' # We're looking for whatever's in the <a href

parameter = re.compile(pattern)

new_pattern = re.findall(pattern, raw_data)

text = ''.join(new_pattern)

query = text.split('.php')[1] # Take only what wasn't in the original link

page2 = urllib2.urlopen(link+query) # Build a new link and open it

raw_data2 = page2.read()

numeral = raw_data2.split('is')[1].lstrip() # Remove the whitespace at the beginning of the word(lstrip)

link2 = link+query

link_default = link2.split('=')[0] # We want what comes before the "="
                                   # This is the default structure of the link

query_default = '=' + str(numeral) # this is what is needed to give us the next nothing

link_default + query_default

i = 0

while i < 400:
    page_default = urllib2.urlopen(link_default + query_default)

    data_default = page_default.read()

    try:
        numeral = data_default.split('nothing is')[1].lstrip() # do this
    except IndexError: 
        numeral = 16044/2 # if you get an index error, then do this


    query_default = '=' + numeral

    i += 1
    print data_default
    print '{} {}'.format(i, data_default)
        # prints out where in the iteration you are(no. of iterations deep),
        # the text contained in the page you're in
