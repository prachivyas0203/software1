age = int(input("How old are you? "))

if age < 12:
    print("You are a minor. The game is now closing.")
else:
    print("Welcome to the game!")

    command = ""

    while command != "lopeta":
        print("\nMAIN MENU")
        print("treasure - Find a treasure")
        print("monster - Meet a monster")
        print("shop - Visit the shop")
        print("help - Get help")
        print("lopeta - Quit the game")

        command = input("Enter your command: ")

        if command == "treasure":
            print("You found a hidden treasure!")

        elif command == "monster":
            print("Oh no! A monster appeared!")

        elif command == "shop":
            print("Welcome to the magic shop!")

        elif command == "help":
            print("You can use the commands shown in the menu.")

        elif command == "lopeta":
            print("The game is closing. Goodbye!")

        else:
            print("I don't know that command.")