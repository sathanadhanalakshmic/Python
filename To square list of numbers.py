def square_elements(lis):
   square_lis=list(map(lambda x:x**2,lis))
   return square_lis
lis=[1,2,3,4,5,6]
print("Original list:",lis)
print("Squared list:",square_elements(lis))
