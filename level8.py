import bz2, re, urllib2
"""
Here we are have a link that requires a username and password.
The username and passwords are contained in the source as a comment.
However they are in compressed format.
The copression used is bz2.
We know this because both the username and password texts start with 'BZh9'
'BZ' is the signature/magic number
'h' stands for Bzip2('H'uffman coding)
'9' is the block size of the data. 
Bzip2 compresses data in block size between 100 and 900kB
Source: https://en.wikipedia.org/wiki/Bzip2

We use regex to find the data contained within the comment tags <!-- and -->
re.DOTALL makes it possible to include newline characters(\n).
We join the data into a continuous string and split according to the newline character
This is because the username and password compressions are located on separate lines.
They both contain some unnecessary characters.
For the username 'un: ' and the ' character
For the password 'pw: ' and the ' character

The characters we want to remove are leading and trailing characters.
This means that we can use strip to remove them.
For removing other characters refer to https://stackoverflow.com/a/3900078
Strip only takes one argument. Therefore we successively strip the characters.
This leaves us with the compressed string.
We can use one-shot decompression.
Refer to https://docs.python.org/2/library/bz2.html (bottom of page)
but since we have escape characters that should be considered as string literalswe use string.decode('string_escape')
Reference: https://stackoverflow.com/a/27503678
         https://docs.python.org/2/library/codecs.html#python-specific-encodings
"""

# NOTE: From the official solutions see:
    # IDs of various crunched(compressed) files
        # http://www.amiga-stuff.com/crunchers-id.html


link = urllib2.Request('http://www.pythonchallenge.com/pc/def/integrity.html')

page = urllib2.urlopen(link).read()

params = re.compile('<!--(.*?)-->', re.DOTALL)

info =  re.findall(params, page)

info = ''.join(info) 

split_info = info.split('\n') # Split according to the newline character "\n"

username = split_info[1] # username is at index 1 in the list

password = split_info[2] # password is at index 2 in the list

username = username.strip('un: ').strip("'")
    # remove unnecessary strings and quotes to remain with compressed text only
    # assign the resulting string to variable username to replace old value

password = password.strip('pw: ').strip("'")
    # see comment in username above. Replace username with password

username = bz2.decompress(username.decode('string_escape'))

password = bz2.decompress(password.decode('string_escape'))

print "Username: {}\nPassword: {}".format(username, password)
