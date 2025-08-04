add = lambda num1, num2 : num1 + num2

sub = lambda num1, num2 : num1 - num2

mul = lambda num1, num2 : num1 * num2

div = lambda num1, num2 : num1 / num2


while True:
    print(
        f" press (1) for addition \n press (2) for subtration \n press (3) for multiplication \n press (4) for divison \n press (5) for Exit")
    choice = input("Enter your choice (1,2,3,4,5) : ")
    num1 = int(input("Enter your 1st number : "))
    num2 = int(input("Enter your 2nd number : "))
    if choice == '5':
        print("Exit, Good Bye!")
        break
    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
        break
    elif choice == '2':
        result = sub(num1, num2)
        print(f"{num1} - {num2} = {result}")
        break
    elif choice == '3':
        result = mul(num1, num2)
        print(f"{num1} * {num2} = {result}")
        break
    elif choice == '4':
        result = div(num1, num2)
        print(f"{num1} / {num2} = {result}")
        break
    else:
        print("Enter the valid choice")
        break
