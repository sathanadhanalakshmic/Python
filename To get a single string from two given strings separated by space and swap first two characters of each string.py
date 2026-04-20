def strspace(s1,s2):
   s=s1+" "+s2
   print("String:",s)
   temp=s1
   s1=s2
   s2=temp
   print("Swapped string is:",s1,s2)
s1=input("Enter a string1:")
s2=input("Enter a string2:")
strspace(s1,s2)

