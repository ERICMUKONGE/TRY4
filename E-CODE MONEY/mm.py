
def option1():
    am = 50000
    print("Select network\t\n1.MTN-USER\n2.AIRTEL-USER")
    user = input("Enter network:\n")
    if(user == "1"):
        print("MTN-USER")
    choice = input("Enter phone number to send to:\n")
    amount = input("Enter amount of money:\n")

    if float(amount < am):
        print("Insufficent funds")
    else:
        print("Continue with transaction")
    choice = input("Enter pin to confirm transaction:\n")
    print("Your transaction was successful")
            
def option2():
    choice = input("Enter phone number:\n")
    choice = input("Enter amount of money:\n")
    choice = input("Enter pin to confirm transaction:\n")
    print("Your transaction was successful")
     
def option3():
    choice = input("Enter phone number:\n")
    choice = input("Enter amount of money:\n")
    choice = input("Enter pin to confirm transaction:\n")
    print("Your transaction was successful")
      
def option4():
    choice = input("Enter meter number:\n")
    choice = input("Enter amount of money:\n")
    choice = input("Enter pin to confirm transaction:\n")
    print("Your transaction was successful") 
     
def option5():
    choice = input("Enter pin to confirm transaction:\n")
    print("Your transaction was successful")
   
def option6():
    choice = input("Enter phone number:\n")
    choice = input("Enter amount of money:\n")
    choice = input("Enter pin to confirm transaction:\n")
    print("Your transaction was successful")
     
def money():
    print("Welcome to E-code Money Service.\t\n1.Send money\n2.Withdraw\n3.Buy credit\n4.Pay bills\n5.Check balance\n6.Deposit")
    choice = input("Enter service of your choice:\n")
    if  (choice == "1"):
        option1()
    elif (choice == "2"):
        option2()
    elif (choice == "3"):
        option3()
    elif (choice == "4"):
        option4()
    elif (choice == "5"):
        option5()
    elif (choice == "6"):
        option6()
    else:
       print("Invaild input,Please go back to main menu")            
               
    
money()    
