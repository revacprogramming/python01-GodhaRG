import re
txt="The rain is fun in Spain"
x=re.search("^The.*Spain$",txt)
print(x)
print("starting index",x.start())
print("ending index", x.end())
print("start and end index" ,x.span())
print("matched object",x.group())
a=re.match("^The.*Spain$",txt)#matched words will display
b=re.findall("[a-m]",txt)#find all lower case characters alphabeticlly between "a" and "m"
print(b)
print(a)
if x:
    print("pattern found in txt")
else:
    print("pattern not found")
s="acde"
pattern=".."
c=re.match(pattern,s)
print(c)
pattern1="^a...s$"
d=re.match(pattern1,s)
print(d)
e="abyss"
p=re.sub(pattern1,"train",e)  #(pattern,replace,string)#("^a","b",e)
print(p)
p1=re.sub("a","b","aaa",2)
print(p1)
p2=re.subn("a","b","aaaba")
print(p2)
p3=re.findall("A","abab")#empty list if we give "a" then we get["a" ,"a"]
print(p3)#return type of p3 is list
inp="aerial"
p4=re.findall("^a",inp)
print(p4)
s1=re.split("a","bbabaccaab")
print(s1)
s2=re.split("a","aababa")
print(s2)
s3=re.split("a","aababa",3)
print(s3)
pattern3='\w+'#alphanumeric
s5="shiva1"
s4=re.search(pattern3,s5)
print(s4)