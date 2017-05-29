from string import maketrans
# This level involves an encrypted text. So we need to create a cypher to make the text human-legible

alphabet = 'abcdefghijklmnopqrstuvwxyz'

cipher_text = 'cdefghijklmnopqrstuvwxyzab'

cipher = maketrans(alphabet, cipher_text)

#text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
text = 'map'
print text.translate(cipher)

