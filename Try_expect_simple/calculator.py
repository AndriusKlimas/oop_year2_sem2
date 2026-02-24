def multiply():
    valid = False
    while not valid:
        try:
            num1 = float(input("Enter first number: "))
            valid = True
        except ValueError as e:
            print("Please enter a valid number.")
#so that the num 1 is saved and only num 2 is chucking errors
    valid = False
    while not valid:
        try:
            num2 = float(input("Enter second number: "))
            valid = True
        except ValueError as e:
            print("Please enter a valid number.")


    print(num1 * num2)

def add():
    valid = False
    while not valid:
        try:
            num1 = float(input("Enter first number: "))
            valid = True
        except ValueError as e:
            print("Please enter a valid number.")

    valid = False
    while not valid:
        try:
            num2 = float(input("Enter second number: "))
            valid = True
        except ValueError as e:
            print("Please enter a valid number.")


    print(num1 + num2)




def display_menu():
    print("Choose from the following: ")
    print("1) Add two numbers")
    print("2) Multiply two numbers")
    print("exit to exit the calculate")


def Option_menu():
    keepRunning = True
    while keepRunning:
        display_menu()
        choice = input()
        match (choice.lower()):
            case "1":
                add()
            case "2":
                multiply()
            case "exit":
                print("Goodbye!")
                keepRunning = False
                continue
            case _:
                print("Please enter a valid option from the menu")


Option_menu()

