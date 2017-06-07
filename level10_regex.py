import re

"""
refer to https://stackoverflow.com/questions/8624345/whats-the-meaning-of-a-number-after-a-backslash-in-a-regular-expression
&&
https://regex101.com/ with regex:(\d)(\1*) and test string:13211311123113112211
"""

value = '1'

for i in range(0, 6):
    values_compiled = re.compile(r'(\d)(\1*)')
    values = values_compiled.findall(value)
    value = ''.join([str(len(i+j))+i for i,j in values])
    print value
