print("""You would like to watch a new anime about Japanese sports.
Which sport do you pick?
1. Shogi.
2. Go.
3. Karuta.
4. Baseball.""")

sport = input("> ")

if sport == "1":
    print("What, in your opinion, is the right age of consent?")
    age_of_consent = int(input("> "))
    if age_of_consent < 12:
        print("You decide to watch Ryuou no Oshigoto. A couple days after you start watching, FBI arrests you, as you are an obvious sexual deviant. Poor you.")
    elif age_of_consent > 12:
        print("You decide to watch Sangatsu no Lion. You have fun and don't break any laws. Good job!")

elif sport == "2":
    print("You decide to watch Hikaru no Go. Are you scared of ghosts?")
    ghost = input("Yes/No ")
    if ghost == "Yes":
        print("You are scared of Fujiwara's ghost. You stop watching and don't have any fun. Poor you.")
    elif ghost == "No":
        print("You enjoy a great anime about go. Good job!")
    else:
        print("Learn to type Yes or No.")

elif sport == "3":
    print("How the hell do you even know what karuta is?")
    reason = input("> ")
    if reason == "Tumblr":
        print("Get the hell out of my game.")
    else:
        print("That's OK, I suppose. Go watch Chihayafuru.")

elif sport == "4":
    print("""    Baseball is an American sport, not a Japanese one.
    Are you American?
    Oh wait, I might as well ask a different question.
    Do you think America is great again?""")
    great = input("Yes/No ")
    if great == "Yes":
        print("Go build a wall or something.")
    elif great == "No":
        print("Good answer. Go watch Major.")
    else:
        print("Learn to type Yes or No.")

else:
    print("It seems you don't like sports. Go watch Shouwa Genroku Rakugo Shinjuu. It's a hell of a show.")
