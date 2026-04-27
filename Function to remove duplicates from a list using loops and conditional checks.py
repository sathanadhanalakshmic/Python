def remove_duplicates(lis):
   newlis=[]
   for i in lis:
      if i not in newlis:
       newlis.append(i)
   return newlis
lis=[1,3,1,5,2,5,25,10,23,14,5,2,7]
newlis=remove_duplicates(lis)
print("New list after removing duplicate elements:\n",newlis)
