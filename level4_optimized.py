import urllib2, re

prefix = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

findnothing = re.compile(r"nothing is (\d+)").search

nothing = '23053'

while True:
    text = urllib2.urlopen(prefix + nothing).read()
    print text
    match = findnothing(text)
    if match:
        nothing = match.group(1)
        print "  going to", nothing
    elif 'Divide' in text:
        nothing = str(int(nothing)/2)
    else:
        break
