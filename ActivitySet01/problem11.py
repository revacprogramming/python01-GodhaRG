# Tuples

filename = "dataset/mbox-short.txt"
o=open(filename,"r")
h=o.readlines() 
for i in h:
    k=i.split()
    if i.startswith("From:"):
      print(k[1]) 
counts=dict()
for line in o:
    emails=line.split()
    for email in emails:
        if  email not in counts:
            counts[email]=1
        else:
            counts[email]+=1
print(counts)


