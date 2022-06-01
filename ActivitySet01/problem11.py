# Tuples

filename = "dataset/mbox-short.txt"
o=open(filename,"r")
count=0
h=o.readlines() 
for i in h:
    k=i.split()
    if i.startswith("From:"):
      print(k[1]) 
counts=dict()
for i in h:
    if i.startswith("From:"):
        emails=i.split()
for email in emails:
    if  email not in counts:
        counts[email]=1
    else:
        counts[email]+=1
print(" most repeating email is =",email)
print("no. of times the email is repeating is=",counts[email])


