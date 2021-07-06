## the different ways you can access a file
""" open("happy.txt", "r") # read only
open("happy.txt", "r+") # read and write
open("happy.txt", "w") # write
open("happy.txt", "a") # can modify but only to the end of the documnent """
#always close a file
#always open file in a variable

happy_ready = open("happy.txt", "r")
##print(happy_ready.readable()) #checks if file can be read. Do this first
##print(happy_ready.readlines()[1])
for r in happy_ready.readlines():
   print(r)
happy_ready.close()
