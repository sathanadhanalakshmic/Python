def count(strings):
   reversed_strings=[s[::-1] for s in strings]
   palindromes=[s for s in reversed_strings if s==s[::-1]]
   return len(palindromes)
strings=["madam","hello","racecar","world","ece"]
palindrome_count=count(strings)
print("Number of palindromes:",palindrome_count)
