n=int(input("Enter a number:"))
no_digits=len(str(n))
num=n
sum=0
while num>0:
   r=num%10
   sum=sum+r**no_digits
   num=num//10
if sum==n:
   print(n,"is a armstrong number")
else:
   print(n,"is not an armstrong number")
