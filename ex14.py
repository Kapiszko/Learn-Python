from sys import argv

script, user_name, gender = argv
prompt = "> "
prompt2 = '> '
prompt3 = '> '

print(f"Hi {user_name}, I see you are an attractive {gender}.")
print(f"I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt2)

print("What kind of computer do you have?")
computer = input(prompt3)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
You are a {gender}. Perfect.
And you have a {computer} computer. Nice.
""")
