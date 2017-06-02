import os, zipfile
"""
This implementation assumes that the number is the last item in the file being read.
Hence the .split()[-1]
"""

home = os.getenv('HOME')

full_path = os.path.join(home, 'Downloads/channel.zip')

z = zipfile.ZipFile(full_path)

name = '90052.txt'

while 1:
    print z.getinfo(name).comment,
    name = z.read(name).split()[-1] + '.txt'
    
