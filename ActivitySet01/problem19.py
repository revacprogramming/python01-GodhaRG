#sum of even and odd numbers
from pickle import STRING


a=int(input("enter the number"))
even_sum=0
odd_sum=0
count=0
count1=0
for number in range(1,a+1):
    if(number%2==0):
        even_sum=even_sum+number
        count=count+1
    else:
        odd_sum=odd_sum+number
        count1=count1+1
print("sum of even numbers=",even_sum)
print("sum of odd numbers=",odd_sum)
print(count)
print(count1)
#sum of n numbers
n=int(input("enter the number:"))
n=n*(n+1)/2
print("sum of n numbers=",n)
#area of a square
def computearea(a,b):
    if a==b:
        s=a*a
    else:
        print("not square")
        s=0
    return s
    
a=int(input("enter side of the square"))
b=int(input("enter adjacent side of the square"))
s=computearea(a,b)
print("area of square=",s)
#program 14
a=float(input("enter number"))
b=float(input("enter the number"))
c=int(input("enter the number"))
d=int(input("ente the number"))
print("sum of 2 integers=",c+d)
print("sum of 2 flaoting point numbers=",a+b)
#program 15
a=int(input("enter the age"))
if a>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")
#program 16
a=float(input("enter a score between 0.0 and 1.0"))
if 0.0<a<1.0:
    if a>=0.9:
        print("A grade")
    elif a>=0.8:
        print("B grade")
    elif a>=0.7:
        print("C grade")
    elif a>=0.6:
        print("D garde")
    elif a<0.6:
        print("F grade")
else:
    print("error")
#program 17
a=str(input("enter the word "))
def reverse(a):
    b=""
    for i in a:
        b=i+b
    return b
b=reverse(a)
if a==b:
    print("palindrome")
else:
    print("not palindrome")
print("original string= ",a)
print(" reversed string=",b)
#program 20
fruit="banana"
index=0
while index<len(fruit):
    letter=fruit[index]
    print(index,letter)
    index=index+1
print(fruit)
c=letter[:3]
print(c)
#program 22
a="hello  world"
print(a[0:5 ])
b=str(input("enter a string"))
c=b.split()
print(c[0])
print(c[1])
