def rotate(lis,n):
   for i in range(n):
      lis.append(lis.pop(0))
   return lis
#main routine
lis=[1,2,3,4,5]
print(rotate(lis,1))
