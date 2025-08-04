import random

top_of_range = input("Enter the type of range : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Type a number more than 0 👍")
        quit()

else:
    print("Type a Numbers 🙌")
    quit()

guesses = 0

while True:

    random_number = random.randint(0, top_of_range)

    guesses += 1

    user_guess = int(input("Make a guess :"))

    if user_guess == random_number:
        print(f"You said {user_guess} and computer said {random_number}")
        print("You got it correct🎉🎉")
        break
    else:
        print(f"You said {user_guess} and computer said {random_number}")
        print("You are wrong 👎")

print(f"You made it in {guesses} guesses")