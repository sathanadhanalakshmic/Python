#Python program to find largest among three numbers#
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
if a>b:
   if a>c:
      print(a,"is bigger")
   else:
      print(c,"is bigger")
elif b>c:
   if b>a:
      print(b,"is bigger")
   else:
      print(a,"is bigger")
elif c>a:
   if c>b:
      print(c,"is bigger")
   else:
      print(b,"is bigger")

