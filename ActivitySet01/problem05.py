# Functions


def computepay(hrs, rte):

 if  hrs>40:
    reg=rte*hrs
    otp=(hrs-40.0) *(rte*0.5)
    p=reg+otp
 else:
    p=hrs*rte
 return p

hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
print("Pay:", p)
