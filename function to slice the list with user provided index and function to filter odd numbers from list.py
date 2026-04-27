#A function to slice the list with user provided index

lis=[10,20,30,40,50,6,7,8,9,10]
start=int(input("Enter the start value:"))
end=int(input("Enter the end value:"))
sliced_lis=lis[start:end]
print("Sliced list\n",sliced_lis)

#A function to filter odd numbers from the list
l=[1,2,3,4,5,6,7,8,9,10]
filtered_lis=[x for x in l if x%2==0]
print("Filtered list\n",filtered_lis)
