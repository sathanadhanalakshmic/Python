def max(a,b,c):
   if a>b and a>c:
      return a
   elif b>c and b>a:
      return b
   elif c>a and c>b:
      return c
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
print("Maximum element : ",max(a,b,c))

