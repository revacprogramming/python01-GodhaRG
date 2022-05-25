# Dictionaries

filename = "dataset/mbox-short.txt"
fname="dataset/mbox-short.txt"
c=open(fname,"r")
n=0
h=c.readlines()
for i in h:
    k=i.split()
    if i.startswith("From:"):
        print(k[1])
        n+=1
print("There were",n,"lines in the file with From as the first word")
#print(f"there were {n} lins in the file with from as the first word")