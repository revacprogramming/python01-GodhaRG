#example program
from math import sqrt


s="Reva cse@bangalore new"
a=s.find("@")
b=s.find(" ",a)#finding space starting from @
string1=s[a+1:b]
print(a)
print(b)
print(string1)
#example program
friends=['joseph','glen','sally']
for friend in friends:
    print("happy new year: ",friend)
for i in range(len(friends)):
    friend=friends[i]
    print("happy new year: ",friend)
#sqrt of a number
from math import sqrt
a=float(input("Enter the number for which sqrt has to be found "))
b=sqrt(a)
print(b)
#2nd method
f=float(input("Enter the number for which sqrt has to be found "))
a=f/2
a2=f
while(a2!=a):
    a2=a
    a=(a+(f/a))/2
print(a)
# to add different numbers
#a=[]
b=int(input("enter the number of numbers to be added "))
i=1
sum=0
while(i<=b):
    c=float(input("enter the numbers ")) #c=int(input("enter the numbers"))
   # a.append(c)
    sum=sum+c
    i=i+1
print("the sum of numbers=",sum)