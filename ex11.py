print("How old are you?", end=' ')
age = int(input("Please give your age "))
print("How tall are you?", end=' ')
height = int(input("Please give your height "))
print("How much do you weigh?", end=' ')
weight = int(input("Please give your weight "))

print (f"So, you're {age} old, {height} tall and {weight} heavy.")

sum_of_measurements = age + height + weight

print("The sum of your measurements is", sum_of_measurements)
