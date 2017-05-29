import itertools
import re
import urllib2
"""Walkthrough


For this challenge we are told recognize the characters. maybe they are in the book, but MAYBE they are in the page source.

Viewing the page source there is a section written "find rare characters in the mess below:" and a large block of jargon below it.

What the two have in common is that they are both started by "<!--" and ended by "-->". So these are our two separators.
.split did not work as intended so I resorted to regex.

First I am looking for text within "<!--" and "-->" hence (.*?) and re.DOTALL makes sure that newline characters are matched as well.

"(.*?)" we want a non-greedy representation(?) of everything within the comments(.) that is repeated zero or more times(*).

This gives us 2 lists but we are only interested in the second one hence the [1]

Since we are shown the picture of a book it means we are looking for letters but more specifically rare letters hence the "?"

"?" means appears zero or one times
once we have the individual letters we join them into one word using the .join
"""

source = urllib2.Request('http://www.pythonchallenge.com/pc/def/ocr.html')

page = urllib2.urlopen(source)

html = page.read()

parameters = "<!--(.*?)-->"

pattern=re.compile(parameters, re.DOTALL) # re.DOTALL reference (https://stackoverflow.com/a/41620138)

text = re.findall(pattern, html)

compiled_text = text[1] # the list we're interested in

new_pattern = "[a-z][A-z]?" # parameters to use

new_text = re.findall(new_pattern, compiled_text) # finds the letters

print ''.join(new_text)

