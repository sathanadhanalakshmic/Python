def palindrome(str1):
   if str1==str1[::-1]:
      print(str1,"is a palindrome")
   else:
      print(str1,"is not a palindrome")
str1=input("Enter a string:")
palindrome(str1)
