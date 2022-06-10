from sys import argv
#sys is a module an from it we import argv,argv is a list containing the arguments passed to the python interpreter
from os.path import exists
#creates a path for transfer of data from one  file to another 
script , from_file , to_file = argv
#argv variable holds the argument that are passed in the script upon execution
print(f"Copying from {from_file} to {to_file}")
# we could do these two or one line ,how?
in_file = open(from_file)
#allows access from the file to be accessed from
indata = in_file.read()
#allows reading from the file to be accessed from

print(f"The input file is {len(indata)} bytes long")
#Display string and length of the string in the file

print(f"Does the out file exist?{exists (to_file)}")
#Display string to be accessed by the in_file
print("Ready,hit RETURN to continue, CTRL-C to absort.")
#Display suggestion given to user
input()
#prompts the user to make an input

out_file = open(to_file,'w')
#allows to open the file being copied to by writing to it
out_file.write(indata)
#allows writing  data to the file

print("Alright,all done")
#Displays string showing process is done

out_file.close()
#closes the file being copied from
in_file.close()
#closes the file being copied at