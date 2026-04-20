def count_words(s):
   s1=s.split()
   c=0
   for i in s1:
      c=c+1
   print("Number of words:",c)
s=input("Enter a sentence:")
count_words(s)
