import string
"""This is the optimized version of my answer from reading the solutions.

We know that we are translating letters of the alphabet and that the cipher starts from c-z and ends in ab.
Instead of manually printing out the letters, we can use string.ascii_lowercase since in this case all of our letters are lowercase.
For the cipher we use string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
string.ascii_lowercase[2:] prints out from c-z
string.ascii_lowercase[:2] prints out a&b"""

alphabet = string.ascii_lowercase
cipher_text = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
cipher = string.maketrans(alphabet, cipher_text)

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print text.translate(cipher)
