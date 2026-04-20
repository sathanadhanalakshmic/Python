temp=input("Enter a temperature:")
humi=input("Enter the humidity:")
if temp=="warm":
   if humi=="dry":
      print("Play basketball")
   else:
      print("Play Tennis")
else:
   if humi=="dry":
      print("Play cricket")
   else:
      print("Swim")
