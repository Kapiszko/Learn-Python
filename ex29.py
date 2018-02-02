people = 20
cats = 30
dogs = 15


if people < cats and people > dogs:
    print("Too many cats! The world is doomed!")
    print("The world is drooled on!")
    if people != dogs:
        print("People are overlords of dogs.")

if not(people > cats and people < dogs):
    print("Not many cats! The world is saved!")
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

dogs += 20

if dogs != people and dogs > cats and dogs > people:
    print("Dogs overwhelming!")
