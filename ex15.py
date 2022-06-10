from sys import argv
#sys is a module an from it we import argv,argv is a list containing the arguments passed to the python interpreter
script , filename = argv
#argv variable holds the argument that are passed in the script upon execution
txt =  open(filename)
#Opens the next .txt file
print(f"Here is a file{filename}")
#Displays the string
print(txt.read())
# Displays the txt and reads the .txt file

print("Type the filename again:")
# Displays string 

file_again = input(">")
#Prompts the user to have an input from the keyboard

txt_again = open(file_again)
#This gives a second chance to open the .txt file 

print(txt_again.read())
#This gives a other chance to display and re-read the .txt file