from sys import argv #stes up the required starting input - filename

script, filename = argv #lists the starting inputs

txt = open(filename) #the txt variable is defined here as opening a file with the filename given when running the script

print(f"Here's your file {filename}:") #prints out a sentence explaining the below
print(txt.read(), txt.close()) #prints and reads the txt variable, so effectively opens the file with filename initially given and reads it
print (f"The {filename} file is now closed.")


print("Type the filename again:") #prints out a prompt sentence
file_again = input("> ") #sets up an input for the filename (this time in script and not at entry)

txt_again = open(file_again) #the txt_again variable is defined here as opening the file whose name was input

print(txt_again.read(), txt_again.close()) #prints and reads the txt_again variable, so effectively opens the file with filename given in script and reads it
