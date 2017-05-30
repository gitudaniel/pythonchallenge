import re
import urllib2
"""() in regex

Parentheses in regex indicate a capturing group.
I take this to mean a group of particular interest to us.
In this case the sequence [a-z] in between [A-Z]&[A-Z]
"""

page = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')

raw_data = page.read()

parameters = "<!--(.*?)-->"

pattern = re.compile(parameters, re.DOTALL) # pre-compile for optimization

info = re.findall(pattern, raw_data)

data = ''.join(info)

new_params = "[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]"

list_data = re.findall(new_params, data)

print ''.join(list_data)
