import base64, urllib2
from PIL import Image

"""
This iteration uses list slicing to get the values at the even and odd pairs.
Once you get this the operation is similar to that in level11.py.
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
[even.append(i) for i in pixels[::2]]

odd = []
[odd.append(i) for i in pixels[1::2]]

even_img = Image.new(img.mode , img.size)

even_img.putdata(even)

print even_img.show()
