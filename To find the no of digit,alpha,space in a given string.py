def count_case(p):
   d=0
   s=0
   a=0
   for i in p:
      if i.isdigit():
       d=d+1
      elif i.isspace():
       s=s+1
      elif i.isalpha():
       a=a+1
   print("Alphabets:",a)
   print("space:",s)
   print("digit:",d)
t=input("Enter a string:")
count_case(t)
