from StringIO import StringIO
import urllib2, zipfile
"""
For more info on StringIO refer to https://stackoverflow.com/questions/7996479/what-is-stringio-in-python-used-for-in-reality
"""

zobj = StringIO()

zobj.write(urllib2.urlopen("http://pythonchallenge.com/pc/def/channel.zip").read())

z = zipfile.ZipFile(zobj)

filenum = '90052'

lcomment = []

while True:
    if filenum.isdigit():
        filename = filenum + '.txt'
        lcomment.append(z.getinfo(filename).comment)
        info = z.read(filename)
        filenum = info.split(' ')[-1]
    else:
        break
z.close()
print ''.join(lcomment)
