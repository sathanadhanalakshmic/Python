def count(lis):
   odd=0
   even=0
   for i in lis:
      if i%2==0:
       even=even+1
      else:
       odd=odd+1
   print("Number of Even Integers in list:",even)
   print("Number of Odd Integers in list:",odd)
lis=[10,11,23,5,3,2,13,22,50]
count(lis)
