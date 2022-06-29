'''#9 th program in question bank
l=[1,2,3,4,5]
for i in l:
    print(i)'''
#dictionaries
purse=dict()
purse["money"]=12
purse["candy"]=3
purse["tissues"]=7
print(purse)
print(purse["candy"])
purse["candy"]=purse["candy"]+1
print(purse)
#dictionaries and lists
counts=dict()
names=["a","b","c","d"]
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]+=1
print(counts)