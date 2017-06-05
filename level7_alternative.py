import re, urllib2
from PIL import Image
"""
I did not find the official solutions to be more optimal than the one written.
They were simply different.
What I did find was a way to yank an entire vim file.
Yank means copy.
The only difference between this and level7.py is the use of map twice at the end.
To yank an entire file, while in normal mode press the keys gg"*yG
gg -> gets the cursor to the first character of the file
"*y -> starts a yank command to register * from the first line
G -> got to the end of the file
Reference: https://stackoverflow.com/a/1620029

NOTE: The restriction on the number of lines you can yank at once still stands

For Vim modes refer to: https://en.wikibooks.org/wiki/Learning_the_vi_Editor/Vim/Modes
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

print ''.join(map(chr, map(int, text_digits))) 

