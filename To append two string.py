def append_strings(s1,s2):
   l1=[char for char in s1]
   l2=[char for char in s2]
   combined_lis=[char for char in l1+l2]
   result=''.join(combined_lis)
   return result
s1=input("Enter a string:")
s2=input("Enter a string:")
print(append_strings(s1,s2))
