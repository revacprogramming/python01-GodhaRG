#to verify phone number using regexp
from collections import Counter
import re
pattern="(0|91)?[6-9][0-9]{9}"
p1="9731822325"
a=re.search(pattern,p1)
if a:
    print("Search is successful")
else:
    print("Search is unsuccessful")
#for email
import re
pattern="(\w)+@(\w+\.)+(com)"
email="john_123@gmail.com"
s1=re.search(pattern,email)
if s1:
    print("Search is successful")
else:
    print("Search is unsuccessful")
#program 6
import re
pattern1="^a...z$"
word=input("enter the word")
s=re.search(pattern1,word)
if s:
    print("Search is successful")
else:
    print("Search is Unsuccessful")
#program 7
email1="abc@gmail.com"
b=re.split("@ "+".",email1)
print(b)
#to concatenate dictionaries
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for d in(dic1,dic2,dic3):dic4.update(d)
print(dic4)