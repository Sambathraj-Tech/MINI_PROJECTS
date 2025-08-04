name = input("Enter your name : ")
print("Welcome to the Adventure game!",name)

answer = input("Choose your Direction that's get out of this Jungle (Left / Right) : ").lower()

if answer == 'left':
    answer = input("Now head towards Waterfall or Mountain. Type (w) for waterfall | Type (m) for mountain : ").lower()

    if answer == 'w':
        print("You drown in the water.So You Lost")
    elif answer == 'm':
        print("You fall from the mountain.So You Lost")
    else:
        print("Not in the options.You Lost")
elif answer == 'right':
    answer = input("Now you want to head towards the Cave OR Go under the dense trees.Type (C) for Cave | Type (T) for trees: ").lower()

    if answer == 'c':
        print("End of the cave You exit from the Forest safely.You Win")
    elif answer == 't':
        print("You are attacked by the Tiger.You dead and lost the game")
    else:
        print("Not in the options.You Lost")
else:
    print("That's not a valid direction .You Lost")