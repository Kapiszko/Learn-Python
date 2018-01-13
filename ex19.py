def cheese_and_crackers(cheese_count, boxes_of_crackers): #defines the function with two arguments
    print(f"You have {cheese_count} cheeses!") #print with format, part of the function
    print(f"You have {boxes_of_crackers} boxes of crackers!") #print with format, part of the function
    print("Man that's enough for a party!") #print, part of the function
    print("Get a blanket.\n") #print with line break


print("We can just give the function numbers directly:") #print explaining
cheese_and_crackers(20, 30) #run function with direct input of numbers to function


print("OR, we can use variables from our script:") #print explaining
amount_of_cheese = 10 #first variable to use with function
amount_of_crackers = 50 #second variable to use with function

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #run function with variables as arguments


print("We can even do math inside too:") #print explaining
cheese_and_crackers(10 + 20, 5 + 6) #run function with math as arguments


print("And we can combine the two, variables and math:") #print explaining
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #run function with variables and math as arguments
