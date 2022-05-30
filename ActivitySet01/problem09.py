#Lists
filename= "dataset/romeo.txt"
fh = open(filename)
x=fh.readlines()
lst = list()
for i in fh.readlines():
    for j in i.split():
        if  j not in lst:
             lst.append(j)
print(sorted( lst))