from sys import argv #imports entry values
from os.path import exists #imports existence of file

script, from_file, to_file = argv #lists entry values

print(f"Copying from {from_file} to {to_file}") #print with format

#we could do these two on one line, how?
in_file = open(from_file).read() #defines variable with one of the entry inputs

print(f"The input file is {len(in_file)} bytes long") #prints length of file


print(f"Does the output file exist? {exists(to_file)}") #prints if file exists
print("Ready, hit RETURN to continue, CTRL-C to abort.") #print
input() #input

out_file = open(to_file, 'w') #variable
out_file.write(in_file) #writing in file

print("Alright, all done.") #print

out_file.close() #close file
