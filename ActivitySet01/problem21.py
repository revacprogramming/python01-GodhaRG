#example program
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
