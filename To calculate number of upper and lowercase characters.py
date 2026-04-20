def count(s):
   upper=0
   lower=0
   for char in s:
      if char.isupper():
       upper+=1
      elif char.islower():
       lower+=1
   print("Upper case characters:",upper)
   print("LOwer case characters:",lower)
s=input("Enter a string:")
count(s)
