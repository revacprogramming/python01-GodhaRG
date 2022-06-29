'''L1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(L1[-4:-1])
str1="reva"
l=int(len(str1))
print(l)'''
from re import A


'''def area(a):
    area=a*a
    print("area= ",area)
a=int(input("enter the number"))
area1=area(a)'''
n=int(input("enter the number of elements you want in fibonacci series ")) #n=10
a=0
b=1
i=1
while(i<=n):
        sum=a+b
        a=b
        b=sum
        i=i+1
        print(a)
print ("fibonacci series=",a)



