def sort_words(s):
   words=s.split()
   words.sort()
   return " ".join(words)
s=input("Enter a sentence:")
print("Sorted sentence:",sort_words(s))
