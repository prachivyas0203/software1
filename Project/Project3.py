# Game project

items = []


def add_item():
    item = input("Enter an item: ")
    items.append(item)
    print("Item added to the list.")


def show_items():
    print("Items in the list:")

    if len(items) == 0:
        print("The list is empty.")
    else:
        for item in items:
            print(item)


def greeting():
    print("Hello! Welcome to my game.")


def menu():
    print("\n--- MAIN MENU ---")
    print("1. Add item")
    print("2. Show items")
    print("3. Greeting")
    print("lopeta - Exit")


age = int(input("Enter your age: "))

if age < 12:
    print("You are a minor. The game will close.")
else:
    print("Welcome to the game!")

    command = ""

    while command != "lopeta":
        menu()

        command = input("Enter your choice: ")

        if command == "1":
            add_item()

        elif command == "2":
            show_items()

        elif command == "3":
            greeting()

        elif command == "lopeta":
            print("Game closed.")

        else:
            print("Invalid command.")

