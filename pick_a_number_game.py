number = "1"
Pick_number = ""## in a while loop you always need an input to store the users guess
Tries = []
number_count = 0
number_limit = 3
out_of_tries = False


while Pick_number != number and not(out_of_tries):
   if number_count < number_limit:
      Pick_number = input("Enter a number: ")
      number_count += 1
   else:
      out_of_tries = True
if out_of_tries:
      print("you've run out of tries")
      
else:
 print("Way to go!") 

""" while Pick_number != number and len(Tries)<3:
      if len(Tries) <3:
        Pick_number = input("Enter a number: ")
        Tries.append(Pick_number)       
      else:
       print("you've run out of tries")
      
      

print("Way to go!") """
