print("Is the cover type of the book you have, soft or hard?")
type = input()
if type == "soft":
   print("is it perfect bound?")
   bound = input()
   if bound =="yes":
      print("Soft, perfect bound books are very popular!")
   else:
      print("Soft covers with coils or stitches are great for short books")
else:
   print("Books with hard covers can be more expensive!")
