from sys import argv #calls up module and imports argv

script, filename = argv #sets up argv values

print(f"We're going to erase {filename}.") #print with formatting
print("If you don't want that, hit CTRL-C (^C).") #print
print("If you do want that, hit RETURN.") #print

input("?") #input with ? as prompt

print("Opening the file...") #print
target = open(filename, 'w') #opens the file whose filename was entered when running the script

print("Truncating the file. Goodbye!") #print
target.truncate() #truncates the file. not really necessary, as opening in "w" mode truncates the file first

print("Now I'm going to ask you for three lines.") #print

line1 = input("line 1: ") #variable with input line 1
line2 = input("line 2: ") #variable with input line 2
line3 = input("line 3: ") #variable with input line 3
line4 = f"{line1} \n{line2} \n{line3} \n"

print("I'm going to write these to the file.") #print


target.write(line4)

print("And finally, we close it.") #print
target.close() #close the file.
