file="dataset/mbox-short.txt"
c=open(file,"r")
z=c.readlines()
count=0
count1=0
#print(z)
for i in z:
    #print(i)
    count+=1
    if i.startswith("X-Content"):
        print(i)   
        count1+=1
print(count1)
print(count)
#for line in fhand:
 #line=line.rstrip()
 # if not "@uct.ac.za" in line:
   #continue
 #print(line)