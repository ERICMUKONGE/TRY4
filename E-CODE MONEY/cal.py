
print("Welcome to the world of math\t\n1.Add\n2.Subtract\n3.Divide\n4.Mulitply")

operator = input("Enter operation of your choice:\n")

if operator == "1":
    num1 = input("Enter first_number:\n")
    num2 = input("Enter second_number:\n")
    print('The sum is:\n' + str(float(num1) + float(num2)))

elif operator == "2":
    num3 = input("Enter first_number:\n")
    num4 = input("Enter second_number:\n")
    print("The difference is:\n" + str(float(num3) - float(num4)))

elif operator == "3":
    num5 = input("Enter first_number:\n")
    num6 = input("Enter second_number:\n")
    print("The qutote is:\n" + str(float(num5)/float(num6)))

elif operator == "4":
    num7 = input("Enter first_number:\n")
    num8 = input("Enter second_number:\n")
    print("The product is:\n" + str(float(num7) * float(num8)))

else:
    print("Invaild input")    
