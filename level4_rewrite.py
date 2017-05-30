import urllib2, re
"""

This is a rewrite of the original level 4 to cater for its deficiencies.
You get your solution where this code breaks
"""

link = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

page = urllib2.urlopen(link)

raw_data = page.read()

pattern = '<a href="(.*?)">'

in_links = re.findall(pattern, raw_data) # We find all the links contained in the page

in_links = ''.join(in_links[0]) # Link of interest is at position 0
                                # Use ''.join to make it a string

nothing = in_links.split("=")[1] # We split it at the = to get the first nothing

new_link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

n = 0

while n < 400:
    new_url = new_link + nothing

    new_page = urllib2.urlopen(new_url)

    new_data = new_page.read()


    if 'Divide' in new_data:
        nothing = str(int(nothing)/2)
    else:
        nothing = [i for i in new_data.split(' ') if i.isdigit()][0] 
                # this finds the digit in the text

    n += 1

    print '{} {}'.format(n, new_data)


