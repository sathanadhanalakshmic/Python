def vowels(s):
   l=len(s)
   a=0
   for i in range(0,l):
      if ((s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u") or (s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U")):
        a=a+1
   return a
s=input("Enter a string:")
print("Number of vowels:",vowels(s))
