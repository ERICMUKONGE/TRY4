people = 30000
cars = 4000
trucks = 150000

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the truck.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright,let's just take the truck.")
else:
    print("Fine, let's stay home then.") 

if cars > people or trucks < cars:
    print("wait for it:")
else:
    print("Big deal my gee")                                   