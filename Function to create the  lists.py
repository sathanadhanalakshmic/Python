
def colours():
   colours=["Blue","Pink","Purple","Red","Green","Yellow"]
   l=len(colours)
   return l
def max_min(lis):
   return min(lis),max(lis)
def sum_avg(lis):
   s=sum(lis)
   avg=s/len(lis)
   return s,avg
print("Size of the list colours:",colours())
lis=[10,20,30,100,200,150]
mini,maxi=max_min(lis)
print("Maximum element:",maxi,"Minimum element:",mini)
s,avg=sum_avg(lis)
print("Sum:",s,"Average:",avg)
