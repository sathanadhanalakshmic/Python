def merge(lis1,lis2):
   m=lis1+lis2
   m.sort()
   return m
lis1=["abc","bac","baa","see"]
lis2=["bat","nap","ball","map"]
print("Single sorted list:\n",merge(lis1,lis2))
