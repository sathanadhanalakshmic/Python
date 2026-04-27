def count_strings(lis):
   count=0
   for word in lis:
      if len(word)>=2 and word[0]==word[-1] :
       count=count+1
   return count
lis=["xyz","aba","121","abc","pqp"]
print("Number of Strings:",count_strings(lis))
