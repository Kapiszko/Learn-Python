cars = 100.00 #number of cars available for the day
space_in_a_car = 4.00 #amount of space in a cars
drivers = 30.00 #number of available drivers
passengers = 90.00 #number of available passengers
cars_not_driven = cars - drivers #calculation for cars that are not used
cars_driven = drivers #calculation for cars that are used
carpool_capacity = cars_driven * space_in_a_car #calculation for carpool_capacity
average_passengers_per_car = passengers / cars_driven #calculation for average


print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
