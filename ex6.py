types_of_people = 10 #two types of people
x = f"There are {types_of_people} types of people." #string which uses the types of people variable

binary = "binary" #binary variable
do_not = "don't" #do not variable
y = f"Those who know {binary} and those who {do_not}." #string inside string

print(x) #prints variable x
print(y) #prints variable y

print(f"I said: {x}") #string inside string
print(f"I also said '{y}'") #string inside string

hilarious = True #hilarious variable
joke_evaluation = "Isn't that joke so funy?! {}" #string inside string

print(joke_evaluation.format(hilarious)) #format for the joke_evaluation string above

w = "This is the left side of..." #beginning string
e = "a string with a right side." #ending string

print(w + e) #two strings added together

badjoke = "Fuck no it's terrible."

joke_evaluation2 = "Isn't that joke so funy?! {}" #string inside string

print(joke_evaluation2.format(badjoke)) #format for the joke_evaluation string above
