def translation(phrase):
## I need to fix the small input problem so the app doesn't spit out traceback errors
   translation = ""
   if type(translation) == int:
      print(Error)

   for letter in phrase:
         if letter.lower() in "AEIOUaeiou":
            if letter.isupper():
               translation = translation + " P"
            else:
               translation = translation + "p"
         else:
            translation = translation + letter
   return translation
  

print(translation(input("Enter a phrase: ")))
