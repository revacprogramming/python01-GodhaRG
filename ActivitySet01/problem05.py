# Functions


def computepay(h, r):
    pass  # ...


hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
if hrs>40:
    reg=rte*hrs
    otp=(hrs-40.0) *(rte*0.5)
    p=reg+otp
else:
    p=hrs*r3te

print("Pay", p)
