formatter = "{} {} {} {}" #this gives 4 empty slots in the formatter variable

print(formatter.format(1, 2, 3, 4)) #this fill the slots with 1234
print(formatter.format("one", "two", "three", "four")) #this fills the slots with one two three four
print(formatter.format(True, False, False, True)) #this fills the slots with true false false true
print(formatter.format(formatter, formatter, formatter, formatter)) #this calls the variable 4 times but does not fill, so 16 {} show up
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
)) #this calls up four different strings to fill the slots in the variable
