number = 1
Pick_number = ""## in a while loop you always need an input to store the users guess
Tries = []
Pick_number = float(input("Enter a number: "))
   
if Pick_number == number:
   print("that's the one!")
elif Pick_number != number and len(Tries)<3:
   Tries.append(Pick_number)
   print(Tries)
   Pick_number
elif len(Tries)>3:
   print("You're out of tries!")
      
      

