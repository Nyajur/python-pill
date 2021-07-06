happy_file = open("happy.txt", "a")
print(happy_file.write("\nkelly"))
happy_file.close()


happy_file = open("happy.txt", "r")
print(happy_file.read())
happy_file.close()

happy_file = open("happy.txt1", "w")##tp create a new file
print(happy_file.write("\nkelly"))
happy_file.close()

happy_file = open("happy.html", "w")##tp create a new html file
print(happy_file.write("<p>creating  a html page within python</P>"))
happy_file.close()

#writing--1 overides an existing file
#2-- creates a new file if one in specified in the open string where first var is stored
#3--append to the new file you have created             