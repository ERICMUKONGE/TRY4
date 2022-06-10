
from sys import argv
#sys is a module an from it we import argv,argv is a list containing the arguments passed to the python interpreter

script,user_name = argv
#argv variable holds the argument that are passed in the script upon execution
prompt = '>'
# asks the user to has an input

print(f"hi {user_name} and this is my {script} script.")
#Displays f-string in the print function
print("I would ike to ask you a few questions:")
#Displays the string in the print function
print(f"Do you look like me {user_name}")
#Displays the string and f-string 
likes = input(prompt)
#prompt the user to make an input

print("Where would you live {user_name}")
#Displays the string and f-string 
lives = input(prompt)
#prompt the user to make an input

print("What kind of computer do you have?")
#Displays the string  
computer = input(prompt)
#prompt the user to make an input

print(f"Alright you said {likes} about liking me. You live in {lives}.Not sure where that is .And you have a  {computer} computer.nice")
##Displays the string and f-string