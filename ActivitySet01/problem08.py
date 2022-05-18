# File
#fname="dataset/mbox-short.txt"
#Use the file name mbox-short.txt as the file name
fname=input("enter file name: ")
fh=open(fname)
n=0
a=[]
result=0
for line in fh:
    if not line.startswitch("X-DSPAM-Confidence:"):
        continue
    x=line.split()
    a.append(float(x[1]))
    result=result+float(x[1])
    n=n+1
average=result/n
print("Average spam confidence: " ,average)   

