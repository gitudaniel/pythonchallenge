import base64, re, urllib2
from PIL import Image, ImageEnhance

"""
The source in this page gives us a very big hint. Odd Even.
This means split the pixels in the image into odd and even elements based on their position.
Get all the pixels in the image.
If the pixel is at position 1 it is odd it goes together with all odd pixels.
If the pixel is at position 2 it is even and goes with all other even pixels.
Use all this data to create a new image by putting the new pixel values to a new image.
Use list comprehension to get odd and even
Both odd and even give the same results so pick any to go with
"""

username = 'huge'
password = 'file'

base64string = base64.b64encode('%s:%s' % (username, password))

link = urllib2.Request('http://www.pythonchallenge.com/pc/return/cave.jpg')

link.add_header('Authorization', 'Basic %s' % base64string)

page = urllib2.urlopen(link)

img = Image.open(page)

pixels = list(img.getdata())

even = []
odd = []

[even.append(pixels[i]) for i in range(len(pixels)) if i % 2 == 0]

[odd.append(pixels[i]) for i in range(len(pixels)) if i % 2 != 0]

# The new images retain the properties of the original image.
# This means that the mode(RGB) and the size(640x480) remain unchanged
even_img = Image.new(img.mode, img.size)

even_img.putdata(even)

print even_img.show()

