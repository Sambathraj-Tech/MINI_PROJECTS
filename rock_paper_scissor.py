import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissor"]

while True:

    user_input = input("Enter Rock/Paper/Scissor {or} Q to quit : ").lower()

    if user_input == 'q':
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # 0 : rock ,1 : paper,2 : scissor

    computer_guess = options[random_number]  #list index values will be shuffled
    print("computer guess is",computer_guess)

    if user_input == computer_guess:
        print("Match Draw !")

    elif user_input == 'rock' and computer_guess == 'scissor':
        print("User wins 🎉🎉")
        user_wins += 1

    elif user_input == 'scissor' and computer_guess == 'paper':
        print("User wins 🎉🎉")
        user_wins += 1

    elif user_input == 'paper' and computer_guess == 'rock':
        print("User wins 🎉🎉")
        user_wins += 1

    else:
        print("Computer wins 🎉🎉")
        computer_wins += 1

print(f"User wins {user_wins} times 🎊.")
print(f"Computer wins {computer_wins} times 🎊.")

print("Good Bye 👋")
