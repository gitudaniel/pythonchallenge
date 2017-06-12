import os
from PIL import Image,ImageFile

"""
Here when you view the source of the page http://www.pythonchallenge.com/pc/return/evil.html you see a link to http://www.pythonchallenge.com/pc/return/evil1.jpg
This is interesting since in the original image evil does not have a number as a suffix
Increase the number to see what you get and you'll get to http://www.pythonchallenge.com/pc/return/evil2.jpg
There is an image telling you not jpg _.gfx.
Try changing the suffix to .gfx and download the resulting file.
On opening the file, you notice that it contains binary data and has a length of 63575
In the original evil we are shown a dealer dealing cards to 5 players so you should deal evils 5 ways.
In a card game with 5 players a player gets every 5th card.
We create 5 separate images(for i in range(5)) and each image gets every 5th element from the original data(*.write(data[i::5))
The section open('%d.jpg' %i, 'wb') means that we want to open an image for every number in range(5) and write bytes to it('wb')
For more info on %d refer to https://stackoverflow.com/a/15699580

We read all the images starting from 0.jpg up to 4.jpg and get the information contained therein
"""

ImageFile.LOAD_TRUNCATED_IMAGES = True

home = os.getenv('HOME')

data = os.path.join(home, 'Downloads/evil2.gfx')

data = open(data, 'rb').read()

for i in range(5):
    open('%d.jpg' %i , 'wb').write(data[i::5])

    img = Image.open('%d.jpg' %i)
    print img.show()
