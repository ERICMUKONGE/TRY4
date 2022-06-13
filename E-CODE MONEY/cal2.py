while True:
    print("Welcome to the world of math\t\n1.Add\n2.Subtract\n3.Divide\n4.Mulitply\nEnter q or Q to Exit")

    choice = input("Enter your choice:")

    if choice == 'q' or choice == 'Q':
        break

    num1 = float(input("Enter number 1:"))
    num2 = float(input("Enter number 2:"))

    if choice == "1":
        print(num1,"+",num2,"=",(num1+num2))

    elif choice == "2":
        print(num1,"-",num2,"=",(num1-num2))

    elif choice == "3":
        print(num1,"*",num2,"=",(num1*num2)) 

    elif choice == "4":
        if num2 == 0.0:
            print("Divide by 0 Error")
        else:
            print(num1,"/",num2,"=",(num1/num2))

    else:
        print("Invalid choice")            