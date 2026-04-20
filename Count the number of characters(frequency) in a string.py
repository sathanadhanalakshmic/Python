def count(s):
   c=0
   for i in s:
      c=s.count(i)
      print(i,":",c)
s=input("Enter a string:")
count(s)
