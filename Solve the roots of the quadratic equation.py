import math
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
d=math.sqrt((b*b)-(4*a*c))
r1=(-b+d)/(2*a)
r2=(-b-d)/(2*a)
print("The roots are",r1,r2)

