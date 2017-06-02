import pickle, urllib2

page = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()

obj = pickle.loads(page)

result = ""

for outer in obj:
    for inner in outer:
        for i in range(0, inner[1]):
            result += inner[0]
    result += "\n"

print result
