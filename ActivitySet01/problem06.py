# Loops & Iterators
a=[]
largest = None
smallest = None

while True:
    num = input("Enter a number? ")

    if num == "done":
        break 
    else:
        try:
            num=int(num)
            a.append(num)
            largest=max(a)
            smallest=min(a)
        except:
            print("Invalid Input")

    
for i in a:
    print(i)
print("Maximum is ", largest)
print("Minimum is ",smallest)

