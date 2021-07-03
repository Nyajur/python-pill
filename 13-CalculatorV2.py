""" num1 = float(input("Please enter number: "))
operator = input("Please enter operator: ")
num2 = float(input("Please enter number: ")) """

def calculator():
   num1 = float(input("Please enter number: "))
   operator = input("Please enter operator: ")
   num2 = float(input("Please enter number: "))
   if operator == "+":
      print(num1+num2)
   elif operator =="-":
      print(num1-num2)
   elif operator =="*":
      print(num1*num2)
   elif operator == "/":
      print(num1/num2)
   else:
      print("invalid operator")      
print(calculator())