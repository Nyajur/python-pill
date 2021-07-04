base = float(input("Please enter a number: "))
exponential = float(input("Pleae enter a power to raise to: "))

def raiser():
    return base**exponential
print(raiser()) 


def raiser():
   base = float(input("Please enter a number: "))
   exponential = float(input("Pleae enter a power to raise to: "))
   return base**exponential
print(raiser())  
 

def raiser(base,exponential):
   return base**exponential
print(raiser(2,4)) 

def raiser(base,exponential):
   result = 1
   for i in range(exponential):
      result =result*base
   return result
print(raiser(2,4)) 
