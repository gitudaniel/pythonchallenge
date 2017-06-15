import xmlrpclib

"""
References: https://docs.python.org/2/library/simplexmlrpcserver.html#simplexmlrpcserver-example
            https://docs.python.org/2/library/xmlrpclib.html
            http://archive.oreilly.com/pub/a/python/2001/01/17/xmlrpcserver.html
            http://www.tldp.org/HOWTO/XML-RPC-HOWTO/xmlrpc-howto-python.htmlhttp://www.tldp.org/HOWTO/XML-RPC-HOWTO/xmlrpc-howto-python.html

To solve this level you need to to:
    Go back to level 12 to evil4.jpg and run:
        curl -u huge:file http://www.pythonchallenge.com/pc/return/evil4.jpg
        curl transfers data to or from a server. It can be used to fetch links
    Then refer to: https://en.wikipedia.org/wiki/555_(telephone_number)

There are two ways to do this:
    1. Try the buttons on the phone and realize number 5 is working
    2. Go to the source and follow the link http://www.pythonchallenge.com/pc/phonebook.php
Both of these solutions take you to an XML Remote Procedure Call Response page.
This means we need to use the xmlrpclib
First we get a server proxy and then list the methods in that proxy
Take the one that does not belong and run ServerProxy.system.methodHelp(name) on it to find out what it does.
Run ServerProxy.system.methodSignature(name) to find out how it takes its inputs
In this example the output of proxy.system.methodSignature(name) is [['string', 'string']].
This means that its input is a string and its output is also a string
The input is the output in curl -u huge:file http://www.pythonchallenge.com/pc/return/evil4.jpg
"""

proxy = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

#print proxy.system.listMethods()

#print proxy.system.methodHelp('phone')

#print proxy.system.methodSignature('phone')

print proxy.phone('Bert')
