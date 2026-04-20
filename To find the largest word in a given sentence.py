def largest(s):
   words=s.split()
   largest=max(words,key=len)
   return largest
s=input("Enter a sentence:")
print("Largest word:",largest(s))
