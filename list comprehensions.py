a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))
n = int(input("Enter value of n:"))
result = [[i, j, k]
          for i in range(a+1) 
          for j in range(b+1) 
          for k in range(c+1) 
          if i + j + k != n]

print(result)
