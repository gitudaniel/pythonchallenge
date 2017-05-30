import urllib, urllib2

data = {}
number = '12345'

for i in range(400):
    data['nothing'] = number
    url_values = urllib.urlencode(data)
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    full_url = url + '?' + url_values
    
    foo = urllib2.urlopen(full_url)
    foo = foo.read()
    print foo
    foo = foo.split(" ")

    number = [i for i in foo if i.isdigit()][0]
