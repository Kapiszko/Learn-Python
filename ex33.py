def exercise_function(initialvalue, numbers, stoppoint, addpoint):

    while initialvalue < int(stoppoint):
        print(f"At the top initialvalue is {initialvalue}")
        numbers.append(initialvalue)

        initialvalue = initialvalue + int(addpoint)
        print("Numbers now: ", numbers)
        print(f"At the bottom initialvalue is {initialvalue}")


    print("The numbers: ")

    for num in numbers:
        print(num)

exercise_function(20,[],30,5)
