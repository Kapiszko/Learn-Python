def break_words(stuff): #defines break_words function
    """This function will break up words for us.""" #creates a documentation comment
    words = stuff.split(' ') #defines the words variable as splitting the input for the function
    return words #returns the split up input

def sort_words(words): #defines the sort_words fucntion
    """Sorts the words.""" #creates a documentation comment
    return sorted(words) #returns the sorted function input

def print_first_word(words): #defines the print_first_word function
    """Prints the first word after popping it off.""" #creates documentation comment
    word = words.pop(0) #define the word variable as popping off the first word of the function input
    print(word) #prints the word variable

def print_last_word(words): #defines the print_last_word function
    """Prints the last word after popping it off.""" #creates a documentation comment
    word = words.pop(-1) #define the word variable as popping off the last word of the function input
    print(word) #prints the word variable

def sort_sentence(sentence): #defines the sort_sentence function
    """Takes in a full sentence and returns the sorted words.""" #creates a documentation comment
    words = break_words(sentence) #defines the words variable by calling the break_words function on the input for this function
    return sort_words(words) #returns the result of calling the sort_words function on the words variable

def print_first_and_last(sentence): #defines the print_first_and_last function
    """Prints the first and last words of the sentence.""" #creates a documentation comment
    words = break_words(sentence) #defines the words variable by calling the break_words function on the input for this function
    print_first_word(words) #calls the print_first_word function on the words variable
    print_last_word(words) #calls the print_last_word function on the words variable

def print_first_and_last_sorted(sentence): #defines the print_first_and_last_sorted function
    """Sorts the words then prints the first and last one.""" #creates a documentation comment
    words = sort_sentence(sentence) #defines the words variable by calling the sort_sentence function on the input for this fucntion
    print_first_word(words) #calls the print_first_word function on the words variable
    print_last_word(words) #calls the print_last_word function on the words variable
