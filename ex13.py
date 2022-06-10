from sys import argv
#sys is a module an from it we import argv,argv is a list containing the arguments passed to the python interpreter

script,first,second,third = argv
#argv variable holds the argument that are passed in the script upon execution
print("This is a script:",script)
#outputs the string in the script as [0]
print("This is a first name:",first)
#outputs the string in the first as [1]
print("This is a second name:",second)
#output the string in the second as [2]
print("This is a third name:",third)
#outputs the string in the third as [3]