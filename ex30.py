people = 50 #defines the people variable
cars = 10 #defines the cars variable
trucks = 35 #defines the trucks variable


if cars > people or trucks < cars: #sets up the first branch
    print("We should take the cars.") #print that runs if the if above is true
elif cars < people: #sets up second branch that runs if the first one is not true
    print("We should not take the cars.") #print that runs if the elif above is true
else: #sets up third and last branch that will run if the above ifs are not true
    print("We can't decide.") #print that runs if the else above is true

if trucks > cars:#sets up the first branch
    print("That's too many trucks.")#print that runs if the if above is true
elif trucks < cars:#sets up second branch that runs if the first one is not true
    print("Maybe we could take the trucks.")#print that runs if the elif above is true
else:#sets up third and last branch that will run if the above ifs are not true
    print("We still can't decide.")#print that runs if the else above is true

if people > trucks:#sets up the first branch
    print("Alright, let's just take the trucks.")#print that runs if the if above is true
else: #sets up second and last branch
    print("Fine, let's stay home then.")#print that runs if the else above is true
