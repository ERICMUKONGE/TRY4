formatter = "{} {} {} {}"
#The variable formatter stores a string of empty lists

print(formatter.format(1,2,3,4))
#Displays the integers in a list
print(formatter.format("one","two","three","four"))
#Displays the strings in the tuple
print(formatter.format(True,False,False,True))
#Displays the list of boolean
print(formatter.format(formatter,formatter,formatter,formatter))
#Displays the list of empty list 16times
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
#Displays the string in the print function