import urllib
import string

s = urllib.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read().split('<!--')[2]

print ''.join([x for x in s if x in string.letters]) 

# print ''.join([x for x in s if x.isalpha()]) 
# .isalpha() checks that it consists only of alphabetic characters
# it is an alternative to the above

