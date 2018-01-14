from sys import argv #imports argv

script, input_file = argv #specifies arguments for argv

def print_all(f): #sets up print_all function
    print(f.read()) #this fuction will read a file

def rewind(f): #sets up a rewind function
    f.seek(0) #this function will go to beginning of a file

def print_a_line(line_count, f): #sets up a print_a_line function
    print(line_count, f.readline(), end=' ') #this function willl print a line

current_file = open(input_file) #defines current_file variable by referencing an argv argument

print("First let's print the whole file:\n") #prints

print_all(current_file) #calls the print_all function on current_file

print("Now let's rewind, kind of like a tape.") #prints

rewind(current_file) #calls the rewind function on current_file

print("Let's print three lines:") #prints

current_line = 1 #defines current_line variable
print_a_line(current_line, current_file) #calls the print_a_line function on current_file

current_line = current_line + 1 #defines new value of current_line. This could also be done with +=
print_a_line(current_line, current_file) #calls the print_a_line function on current_file

current_line = current_line + 1 #defines a new value of current_line. this could also be done with +=
print_a_line(current_line, current_file) #calls the print_a_line function on current_file
