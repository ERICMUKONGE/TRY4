from sys import argv
script,filename = argv
print(f'We are going to erase {filename}.')
print("If you dont want that ,hit the CTRL-C (^C).")
print("If you want that ,hit RETURN. ")

input("?")

print("Open this file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye")
target.truncate()

print("Now am going to ask you for three lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("Iam going to write this to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it")
target.close()