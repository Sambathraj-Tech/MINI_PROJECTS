print("Welcome to Quiz Game")
print("For every right answer you got (1) marks \n"
      "If you made mistake your marks reduced (0.5) marks from you scored")

user_input = input("Do You want to Play :")
marks = 0

if user_input.lower() == 'yes':
    print("Let's Play! :)")
else:
    quit()

result = input("CPU stands for : ")
if result.lower() == 'central processing unit':
    print("Correct")
    marks += 1
else:
    print("Incorrect")
    marks -= 0.5

result = input("PSU stands for : ")
if result.lower() == 'power supply':
    print("Correct")
    marks += 1
else:
    print("Incorrect")
    marks -= 0.5

result = input("PM stands for : ")
if result.lower() == 'prime minister':
    print("Correct")
    marks += 1
else:
    print("Incorrect")
    marks -= 0.5

result = input("GPU stands for : ")
if result.lower() == 'graphics processing unit':
    print("Correct")
    marks += 1
else:
    print("Incorrect")
    marks -= 0.5

result = input("CM stands for : ")
if result.lower() == 'chief minister':
    print("Correct")
    marks += 1
else:
    print("Incorrect")
    marks -= 0.5


print(f"Your total correct answer is {marks}")
print(f"Your total percentage is {((marks/5) * 100)} %")





