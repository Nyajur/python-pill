##if statements using boleans
is_happy = False
is_fat = True
if is_happy:
   print("You're so happy")
if is_fat:
   print("I love my lumps rueda rueda rueda")
if is_happy and is_fat:
   print("The jolly old fat king")
elif is_happy and not is_fat:
   print("You look like a skinny version of the king")
elif not is_happy and is_fat:
   print("you look like the king but dont act like him")
else:
   print("You are not the king we love")
