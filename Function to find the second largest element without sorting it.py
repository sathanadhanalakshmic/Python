def largest(lis):
   first=max(lis)
   lis.remove(first)
   second=max(lis)
   return second
lis=[10,20,1,2,25]
print("Second largest element:",largest(lis))
