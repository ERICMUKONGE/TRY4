def add(a,b):
#Function named add with two arguments    
    print(f"ADDING {a} + {b}")
#Displays the string adding   

    return a + b
#Displays value of arguments    

def subtract(a,b):
#Function named subtract with two arguments    
    print(f"SUBTRACTING {a} - {b}")
#Displays the string subtracting    
    return a - b
#Displays value of arguments

def multiply(a,b):
#Function named multiply with two arguments    
    print(f"MULTIPLY {a} * {b}")
#Displays the string multiply    
    return a * b
#Displays values of arguments    

def divide(a,b):
#Function named divide with two arguments    
    print(f"DIVIDING {a} / {b}")
#Diplays the string dividing    
    return a / b 
#Displays values of arguments       

print("Let's do some math with just functions!") 
#Displays the string in the print function
age = add(30,5)
#calling the add function with two parameters and stored in a variable called age
height = subtract(78,4)
#calling the subtract function with two parameters and stored in a variable called height
weight = multiply(90,2)
#calling the multiply function with two parameters and stored in a variable called weight
iq = divide(100,2)
#calling the divide function with two parameters and stored in a variable called iq

print(f"Age:{age},Height:{height},Weight:{weight},IQ:{iq}")
#Displays f-string in dictionary way
print("Here is a puzzle.")
#Displays the string in the fucntion
what = add(age,subtract(height,multiply(weight, divide(iq,2))))
#All the functions are stored in a variable called what

print("That becomes: ",what,"Can you do it by hand?")
#Displays the string and value of what