from class_question import question
question_prompts = [
   "What color is anger? \n (a) Red \n (b) black",

   "What color is the sky? \n (a) White \n (b) Blue",
]

question = [
   question(question_prompts[0], "a"),
   question(question_prompts[1], "b"),

]



def runtest(question):
   score = 0
   for question in question:
      answer = input(question.prompt)
      if answer == question.answer:
         score += 1
   print("You got " + str(score) + "/" + str(len(question)) + "Correct")

runtest(question)
   