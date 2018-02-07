def exercise_function(initialvalue, numbers, stoppoint, addpoint):

    for initialvalue in range(initialvalue, stoppoint):
        print(f"At the top initialvalue is {initialvalue}")
        numbers.append(initialvalue)

        print("Numbers now: ", numbers)
        print(f"At the bottom initialvalue is {initialvalue}")


    print("The numbers: ")

    for num in numbers:
        print(num)

exercise_function(0,[],50,5)
