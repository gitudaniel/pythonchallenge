import re, urllib2
from PIL import Image
"""
Grayscale is created when proportions of red green and blue are equal.
That is red==green==blue
The text is presumably hidden in the gray area of the image.
That is the only thing out of place. 
It can also be assumed to be in the middle of the image.
Once we get the image we create an image object that we will use.
Get the pixels in the middle of the image. Middle == height/2
We want to get the pixels for that whole width because although the gray doesn't run through the whole image, it is impossible to accurately estimate what doesn't contain gray.
The pixels are a list of RGBA tuples. (RGBA -> Red, Green, Blue, Alpha)
Once we have all the pixels, filter out those that have the gray area.
i.e. Those where red==green==blue and get a color from each tuple.
RGB runs from 0-255, map the resulting colors to their alphabetic strings.

# NOTE: Something interesting I learnt along the way:
  # if red is a list of items
  # red[::7] starts from 0 and skips 7 elements
  # [begin here: end here: skip this many]
  # reference: https://stackoverflow.com/questions/509211/explain-slice-notation

# NOTE2: How to remove duplicates in lists
  # if the order is not important use set(<name of list>)
  # if list is important use OrderedDict
        # start with from collections import OrderedDict
        # usecase: list(OrderedDict.fromkeys(<name of list, dict or tuple here>)
        # references: set: https://stackoverflow.com/a/7961390
        #             OrderedDict: https://stackoverflow.com/a/7961425
"""
link = urllib2.Request('http://www.pythonchallenge.com/pc/def/oxygen.png')

pic = urllib2.urlopen(link) # open the url containing the image

img = Image.open(pic) # creates an image object

row = [img.getpixel((x, (img.height)/2)) for x in range(img.width)]
        # get the pixels in the middle of the image

sorted_row = row[::7] # start at row[0] and skip 7 tuples

vals = []

values = [r for r, g, b, a in sorted_row if r==g==b]
        # from the tuple of repeated digits, get a single digit

mapped_values = map(chr,values)

text = ''.join(mapped_values)

text_digits = re.findall('\d+', text) 

print ''.join(map(chr, [int(r) for r in text_digits]))
                   # makes the digit string into an integer
                   # maps the integer value to the corresponding alphabet letter
                   # joins that into a continuous string
