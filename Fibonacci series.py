n=int(input("Enter a number:"))
f=0
s=1
next=0
for i in range(0,n+1):
   print(f,end=" ")
   next=f+s
   f=s
   s=next
