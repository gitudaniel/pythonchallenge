import re
import urllib2
"""
Here we're told to find one small letter surrounded by EXACTLY three big bodyguards on each of its sides. 
This means we're looking for something like "AAAbAAA". But take not of the EXACTLY. 
This means that before and after the three big bodyguards we cannot have another capital letter. 
So this changes out interpretation to "cAAAbAAAc"

Unlike the previous level, there is only one block within the html commets.
Finding that gives us a list of the data of interest.
We join the data to make it a continuous block of text then find the pattern that we need.
[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z] means one small letter([a-z]) followed by a big letter([A-Z]) that occurs three times ({3})

We want the second small letter that occurs in the 4th position of each member of the resulting list.
"""

page = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')

raw_data = page.read()

parameters = "<!--(.*?)-->"

pattern = re.compile(parameters, re.DOTALL) # pre-compile for optimization

info = re.findall(pattern, raw_data)

data = ''.join(info)

new_params = "[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]"

list_data = re.findall(new_params, data)

print list_data

for char in list_data:
    result = char[4]
    print ''.join(result)

