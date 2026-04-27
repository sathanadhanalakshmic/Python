def filter_greater_than_k(nested_list,k):
   return[[num for num in sublist if num>k] for sublist in nested_list]
nested_list= [[1,2,3],[4,5,6],[7,8,9]]
k=int(input("Enter the k value:"))
filtered_list=filter_greater_than_k(nested_list,k)
print("Filtered list:",filtered_list)
