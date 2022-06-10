def print_two(*args):
#Function named print_two with unknown numbers of arguments    
    arg1,arg2=args
#The variable args stores the values arg1 and arg2   
    print(f"arg1:{arg1},arg2:{arg2}")
#Displays strings in a dictonary form     

def print_two_again(arg1,arg2):
#Function named print_two_again with two arguments    
    print(f"arg1:{arg1},arg2:{arg2}")
#Displays string in a dictonary form    

def print_one(arg1):
#Function named print_one with one argument    
    print(f"arg1:{arg1}")
#Displays string in a dictonary           

def print_none():
#Function named print_none with no argument     
    print("I got nothng'.")
#Displays string in the function    

print_two("Zed","Shaw")
#calling the function in the first case
print_two_again("Zed","Shaw")
#calling the function the second case
print_one("First!")
#calling the function the third case
print_none()
#calling the function the fourth case   
     