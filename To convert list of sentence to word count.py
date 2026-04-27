def sentence(sentences):
   return [len(s.split()) for s in sentences]
sentence_lis=["Python is a simple programming language","They are going to tour"]
word=sentence(sentence_lis)
print("Sentences:",sentence_lis)
print("Word count:",word)
