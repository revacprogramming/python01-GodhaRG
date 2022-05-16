# Strings

from xml.etree.ElementPath import find


text = "X-DSPAM-Confidence:    0.8475"
c=text.split()
a=text.find('0.8475')
print(a)
print(text[a:])

