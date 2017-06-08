import base64, re, urllib2
from PIL import Image, ImageDraw

"""
Here we need to do basic authentication to access the jpeg file over url.
The page is login protected so we use headers to do authentication.
See reference: https://stackoverflow.com/a/2955687

For another way to do authentication, see: https://stackoverflow.com/a/23577024

NOTE: For this level the image on the website has nothing to do with the solution.
The hint given is "first+second=?"
What do you get when you combine the first and the second.

Both first and second have a series of numbers associated with them.
We turn these numbers into a list that we can work with.

We then treat them as a series of coordinates with the first in the list being x and the second being y, the third in the list being x and the fourth y and so on.
Fortunately, draw.line() likes lists of coordinates and doesn't even require us to make it a list of 2-tuples. 
Combine the coordinates of first and second and see what you get.
Basically, connect the dots to see what you get.
Use ImageDraw

You can create co-ordinates for x and y using list slices.
To get x coordinates do [::2] -> start from zero and skip 2
To get y coordinates do [1::2] -> start from one and skip 2
Then do coordinates = list(itertools.izip_longest(x, y, fillvalue=0))
This gives you a list in the form [(x,y), (x,y)...]
"""

username = 'huge'
password = 'file'


base64string = base64.b64encode('%s:%s' % (username, password))
# base64 encoding reference: https://stackoverflow.com/a/8909233


# Processing for the page stars here
page_link = urllib2.Request('http://www.pythonchallenge.com/pc/return/good.html')

page_link.add_header("Authorization", "Basic %s" % base64string)

main_page = urllib2.urlopen(page_link)
info = main_page.read()

params = re.compile('<!--(.*?)-->', re.DOTALL)

data = re.findall(params, info)

first = data[1].split('first:')[1].split('second:')[0]
    # use print statement to see representation

second = data[1].split('first:')[1].split('second:')[1]
    # Use print statement to see representation

first = first.split(',')
first = map(lambda x: int(x), map(lambda s: s.strip('\n'), first))
    # Strips the newline characters from the list
    # Then converts the strings to integers

second = second.split(',')
second = map(lambda x: int(x), map(lambda s: s.strip('\n'), second))
    # Strips the newline characters from the list
    # Then converts the strings to integers



img = Image.new('RGBA', (500,500))
draw = ImageDraw.Draw(img)
draw.line(first, fill='white')
draw.line(second, fill='white')
print img.show()


