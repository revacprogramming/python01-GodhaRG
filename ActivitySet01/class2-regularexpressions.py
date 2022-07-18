import re
txt="The rain in Spain"
x=re.search("ai",txt)
print(x)
y=re.findall("ai",txt)
print(y)
z=re.split("ai",txt)
print(z)
a=re.sub("ai","AI",txt)
print(a)
b=re.findall("[ai]",txt)
print(b)
c=re.findall("[a-i]",txt) #searches for alphabets from a to i
print(c)
txt1="The rain in Spain 123"
d=re.findall("[0-9]",txt1)
print(d)
e=re.findall("\d",txt1)
print(e)#\d=[0-9]
f=re.findall("S...n",txt)
print(f)
g=re.findall("^The",txt)
print(g)
h=re.findall("ABC$",txt)
print(h)