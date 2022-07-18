#1.
l1=[1,2,3]
s1={1,2,3}
print(l1,type(l1))
print(s1,type(s1))
s2=set(l1)
print(s2,type(s2))
#to create empty set a=set()
#print(s1[0],s2[2])will show error as set doesnot support indexing
s=set(range(1,6))
print(s)#s.clear() function clears the set
s1.add("reva")#single element insertion
print("s1=",s1)
s2.update({4,5,6})#multiple data element insertion
print("s2=",s2)# can also give as s2.update([10,20,30])
a=s1.union(s2)#also can use or |
print("union of set s1 and s2 is=",a)
print(s1.pop())#removes random element
s1.remove(3)#removes the specified element-shows error when the element is not in the set
print(s1)
s1.discard(4)#doesnot show error when element is not there in set
print(s1)
print("length of s1=",len(s1))
for i in s2:
    print("element in s2=",i)
print(2 in s2)
print("reva" in s2)
s3=s2
print("set s3=",s3)
s3.remove(4)
print(" set s3=",s3 , "set s2=",s2)# removes 4 for both sets-assign method
s3=s2.copy()
print("set 3=",s3)
s3.remove(5)
print("set 3=",s3 ,"set 2=",s2)#removes 4 for only set 3 -copy method
a1=s3.intersection(s2)
a2=s3&s2
print("intersection of s2 and s3=",a1)
print("a2=",a2)
a3=s2.difference(s3)
print("elements in s2 and not in s3=",a3)
print("element left out in both sets=",s2.symmetric_difference(s3))
a4=s3.isdisjoint(s2)
print(a4)
a5=s2.isdisjoint({4})
print(a5)
print(s3.issubset(s2))#or can use<=
print({1,2}.issuperset({2,3}))#or can use>=
d={(1,2,3):"hello"}
print(d[(1,2,3)])#tuple as key in dictionary
