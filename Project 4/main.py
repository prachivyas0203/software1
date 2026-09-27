from item import Item
from room import Room
from player import Player 

name = input("What is your name?")
age = int(input("How old are you?"))

if age < 12:
    print("you are a minor.")
    exit()


# Create items
key = Item("Key", 0.1)
book = Item("Book", 0.5)
apple = Item("Apple", 0.2)


# Create rooms
hall = Room("Hall", key)
kitchen = Room("Kitchen", apple)
library = Room("Library", book)


# Create player
player = Player(name, hall)

print("Welcome", player.name)
print("You are in", player.location.name)


# Game menu
while True:
    print()
    print("----- GAME MENU -----")
    print("1. Move")
    print("2. Collect item")
    print("3. Show my items")
    print("4. Show location")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        print()
        print("1. Hall")
        print("2. Kitchen")
        print("3. Library")

        destination = input("Choose a room: ")

        if destination == "1":
            player.move(hall)
        elif destination == "2":
            player.move(kitchen)
        elif destination == "3":
            player.move(library)
        else:
            print("Invalid choice.")

    elif choice == "2":
        player.collect_item()

    elif choice == "3":
        if len(player.items) == 0:
            print("You have no items.")
        else:
            print("Your items:")
            for item in player.items:
                print(item.name, "-", item.weight, "kg")

    elif choice == "4":
        print("You are in", player.location.name)

        if player.location.item is not None:
            print("There is a", player.location.item.name, "here.")
        else:
            print("There is no item here.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")