
"""
The image at the bottom of the page is actually 10000 x 1 pixels
Above it is an image of a spiralled bun.
This is a hint that you need to create a spiral of the image at the bottom.
In the source you'll find <!-- remember: 100*100 = (100+99+99+98) + (...  -->
These are the dimensions you're supposed to use to spiral.(coordinates_step in the code)
You're supposed to create a square spiral.
See: https://openclipart.org/detail/131341/square-spiral
You should use coordinates corresponding to the x and y axis and pick an appropriate starting point.

Once you have the image, create a new image that we're going to write pixels to.
We come up with a set of co-ordinates that we should go through and initialize a counter.
We also pick a starting point in this case x, y = -1, 0
range(100, 1, -2) gives an output of [100, 98, 96...2]
For each of those values in that range take each value and use it in coordinates_step
coordinates_step is the length over which we're going to put pixels
Where we're going to put the pixels is determined by the coordinates
We get a range of values from 0-3 (for index in range(4))
These will serve as our index values in coordinates_step
We inirialize a variable dimension and equate it to zero
While the value of dimension is less than the value of coordinates_step at a given index, we take that same index and use it to access the values in the coordinates list (coordinates[index])
coordinates is a list of tuples
The value for the x coordinate is located at index 0 in the tuple
The value for y is located at index 1
By doing x += coordinates[index][0] and y += coordinates[index][1] we ensure that we cover all possible coordinates without having to explicitly state them all i.e. (1, 1), (1, -1), (-1, 1), (-1, -1), (1,0), (0,1), (-1,0), (0,-1)
Since the picture is only 1 pixel long its y coordinate value is zero
The counter variable is supposed to represent the x axis and we increment it to go through all 10000 pixels in the picture
Once we get a pixel from the original image we put it into the new image at a specific length within the coordinates.
"""

username = 'huge'
password = 'file'

base64string = base64.b64encode('%s:%s' % (username, password))

link = urllib2.Request('http://www.pythonchallenge.com/pc/return/wire.png')

link.add_header('Authorization', 'Basic %s' % base64string)

page = urllib2.urlopen(link)

img = Image.open(page)
out = Image.new(img.mode, (100,100))

coordinates = [(1,0), (0,1), (-1,0), (0,-1)]

x, y = -1, 0 # This is out start point
counter = 0

for dimension_value in range(100, 1, -2): # see numbered_v2.py for why we use every second value in this range as the dimension_value
    coordinates_step = [dimension_value, dimension_value-1, dimension_value-1, dimension_value-2]
    for index in range(4):
        dimension = 0
        while dimension < coordinates_step[index]:
            x += coordinates[index][0]
            y += coordinates[index][1]
            dimension += 1
            out.putpixel((x, y), img.getpixel((counter, 0)))
            counter += 1

print out.show() 


