def split_list(data,n):
   result=[]
   chunk_size=len(data)//n
   remainder=len(data)%n
   start=0
   for i in range(n):
      end=start+chunk_size+(1 if i<remainder else 0)
      result.append(data[start:end])
      start=end
   return result
data=[1,2,3,4,5,6,7,8,9,10]
n=3
chunks=split_list(data,n)
print(chunks)
