import os, zipfile
"""
Here the biggest hint that we are given is that we are dealing with a zip file.
There is no link to a zip file in the page source.
Although we are given the hint "<html> <!-- <-- zip -->"
This is supposed to tell you to change the html file to a zip file.
Do this in the link above so that it becomes "http://www.pythonchallenge.com/pc/def/channel.zip"
This will automatically download a zip file to the default download location.
Mine is Downloads directory.
We need to point python to the directory /home/user/Downloads/
The file downloaded is called channel.zip
The file path becomes /home/user/Downloads/channel.zip
This is what os.path.join does
The getenv gets the path to Home on the local machine
zipfile.ZipFile is the class for reading and writing ZIP files (see: https://docs.python.org/2/library/zipfile.html)
The readme file suggests we start with 90052.txt
Reading the file it tells me we are following the same format as level 4
So we need to loop through the files getting the next nothing.
Since all files are in .txt format, I take the number, convert it into a string using str(number) and concantenate it with ".txt"
This makes it easy to loop through the document getting only the number.
We get to a point where we are told to collect all the comments.
To do this we first run .getinfo(name) -> this retuns an object with information about the member name then we get the comment contained therein.
We can't get comments on filenames directly since these are strings.
I appended the comments to an empty list and joined them all.
"""

home = os.getenv('HOME') # /Home/user/

path = os.path.join(home, 'Downloads') # /Home/user/Downloads/

zip_file = os.path.join(path, 'channel.zip') # /Home/user/Downloads/channel.zip

x = zipfile.ZipFile(zip_file,'r') # open a zip file to read contents

document = 90052
comment_list = []
while True:
    for filename in [str(document) + '.txt']: # convert to string and concantenate .txt
        try:
            data = x.read(filename) # read the file
            comments = x.getinfo(filename).comment # get the comments
            comment_list.append(comments) # add to the end of the list
        except KeyError:
            print 'ERROR: Did not find %s in zip file' % filename
        else:
            print filename, ':'
            print repr(data)
        digits = int(filter(str.isdigit, data)) # get the number contained within the text 
        print
    document = digits # update the document variable with the new number
   
    print ''.join(comment_list)
