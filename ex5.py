name = 'Kamil Piszko'
age = 26 #not a lie
height = 188 #centimeters
weight = 75 #kilograms
eyes = 'Green'
teeth = 'White'
hair = 'Blonde'
heightconverter = 0.393
convertedheight = height * heightconverter
weightconverter = 2.2
convertedweight = weight * weightconverter

print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"That's {convertedheight} in inches.")
print(f"He's {weight} kilograms heavy.")
print(f"That's {convertedweight} in pounds.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
