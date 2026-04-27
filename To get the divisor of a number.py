def divisor(n):
   return[x for x in range(1,n+1) if n%x==0]
def divisor_of_list(numbers):
   return {num:divisor(num) for num in numbers}
numbers=[10,25,50]
divisors=divisor_of_list(numbers)
print(divisors)
