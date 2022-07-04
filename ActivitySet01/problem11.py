# Tuples

filename = "dataset/mbox-short.txt"
o=open(filename,"r")
count=0
h=o.readlines() 
for i in h:
    k=i.split()
    if i.startswith("From "):
      print(k[1]) 
counts=dict()
emails=[]
for i in h:
    if i.startswith("From "):
        emails.append(i.split()[1])
for x in emails:
     if  x not in counts:
        counts[x]=1
     else:
        counts[x]+=1
#for key, value in counts.emails():
        #print ("% d : % d"%(key, value))
print(" most repeating email is =",x)
print("no. of times the email is repeating is=",counts[x])

#tuples
fhand=open("dataset/romeo.txt")
counts=dict()
for line in fhand:
        words=line.split()
        for word in words:
                counts[word]=counts.get(word,0)+1
lst=list()
for k,v in counts.items():
        newup=(v,k)
        lst.append(newup)
lst=sorted(lst,reverse=True)
for v,k in lst[:10]:
        print(k,v)



