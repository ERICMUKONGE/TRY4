from sys import exit

def opened():
    print("Do you want to start as a beginner")
    print("Do you want to start as advanced user")


    
    choice = int(input(">"))
    if choice == 1: 
        level= "beginner"
        print("Finally your a good beginner")
    elif choice == 2:
        level= "advanced"
        print("Welcome to the table of men")
    else:
        print("Go with this idea to the grave.") 


def game_up():
    print("The first is a snake game.")
    
    print("The third is a brick game")
    
    
    choice = int(input(">"))
    if choice == 1:
        game = "snake game"
        opened()

    else:
        print("Nevermind keep trying  to understand this game. ") 

# game_up()

def option_check():
    print("View through what the game has to offer.")

    choice =int(input(">"))
    if choice ==1:
        option = "View options"
        print("After veiwing what you like about the app please go and custom it accordingly")
    else:
        print("Go back to the menu") 

# option_check()        

def custom():
    print("Adjust the coloring")
    print("Make a change to the themes")
    print("Make any changes to the fonts")
    
    choice = int(input(">"))
    if choice == 1:
        setting = "Coloring"
        print("Thanks for changing the colour")
    elif choice ==2:
        setting = "Themes"
        print("Niceness my bro i got you.")
    elif choice == 3:
        setting = "Fonts"
        print("Standard themes have been used my dear.")
    else:
        print("Go back to main menu")

# custom()


def begin():
    print("Enter 1 to open the game:")
    print("Enter 2 to veiw the game menu:")
    print("Enter 3 to make suggestions to the game")

    choice = int(input(">"))
    if choice == 1:
        setting = "open"
        game_up()
    elif choice == 2:
        setting = "menu"
        option_check()
    elif choice == 3:
        setting = "suggestions"
        custom()
    else:
        print("Please go back to the main menu") 
begin()            

