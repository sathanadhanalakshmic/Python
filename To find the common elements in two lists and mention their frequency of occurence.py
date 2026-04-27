def common(lis1,lis2):
   newlis=[]
   for i in lis1:
      for j in lis2:
       if (i==j) and i not in newlis:
        newlis.append(i)
   print("Common elements:",newlis)
   for i in newlis:
      l1=lis1.count(i)
      l2=lis2.count(j)
      print(i,"occured",l1,"times in list1")
      print(i,"occured",l2,"times in list2")
lis1=[2,5,1,5,2]
lis2=[1,2,3,7]
common(lis1,lis2)
