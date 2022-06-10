cars = 100
#100 has been stored in the variable called car
space_in_a_car = 4.0
#4.0 has been stored in the variable called space_in_a_car
drivers = 30
#30 has been stored in the variable called driver
passengers = 90
#90 has been stored in the variable called passenger
cars_not_driven = cars - drivers
#variable car_not_driven stores the value of car - drivers
cars_driven = drivers
#car_driven variable stores the value of drivers
carpool_capacity = cars_driven * space_in_a_car
#The variable carpool_capacity stores the product of cars_driven and space_in_a_car
average_passengers_per_car = passengers /cars_driven
#The variable average_passengers_per_car stores the result of passengers and cars_driven

print("There are ",cars,"cars available.")
# returns the string'there are',figure of cars,'cars available.'
print("There are only",drivers,"drivers available.")
# returns the string'there are only',figure if drivers,'drivers available'
print("There will be",cars_not_driven,"empty cars today.")
# returns the string'there will be',figure of cars_not_driven,'empty cars today'
print("We can transport",carpool_capacity,"people today.")
# returns the string'we can transport',carpool_capacity,'people'
print("we have",passengers,"to carpool today.")
# returns the string'we have',figure of passengers,'to carpool today'
print("We need to put about",average_passengers_per_car,"in each car")
# returns the string'we need to put about',figure of average_passengers_per_car,'in each car'