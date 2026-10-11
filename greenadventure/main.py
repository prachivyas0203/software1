# The Green Adventure
# An environmental adventure game

from player import Player
from room import Room

# Display the player's current score
def show_score(player):
    print("\nYour current score is:", player.show_score())
    
# Display information about a room
def show_room(room):
    print("\nLocation:", room.name)
    print("Problem:", room.problem)
    print("Possible solution:", room.solve_problem())
    

print("===================================")
print("       THE GREEN ADVENTURE")
print("===================================")

print("\nWelcome to Finland!")
print("Your mission is to protect the environment.")

# Get player information
player_name = input("\nEnter your name: ")

while True:
    try:
        player_age = int(input("Enter your age: "))

        if player_age >= 12:
            break
        else:
            print("You must be at least 12 years old to play.")

    except ValueError:
        print("Please enter your age as a number.")
        
        # Create the player object
player = Player(player_name, player_age)

# Create room objects
forest = Room("Forest", "The forest is full of rubbish.", "Collect rubbish")
lake = Room("Lake", "The lake is polluted.", "Collect plastic")
town = Room("Town", "People are wasting resources.", "Organise recycling")


print("\nWelcome,", player_name + "!")
print("Choose a route and help nature.")



# Main game loop
while True:
    print("\n========== MAIN MENU ==========")
    print("1. Forest Route")
    print("2. Lake Route")
    print("3. Town Route")
    print("4. View Score")
    print("5. Exit Game")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        print("\n--- FOREST ROUTE ---")
        show_room(forest)
        print("1. Collect rubbish")
        print("2. Plant trees")

        action = input("Choose 1 or 2: ")

        if action == "1":
                print("You collected rubbish and protected wildlife!")
                player.add_points(10)

        elif action == "2":
            print("You planted trees and helped the forest!")
            player.add_points(10)

        else:
            print("Invalid choice. No points earned.")

    elif choice == "2":
        print("\n--- LAKE ROUTE ---")
        show_room(lake)
        print("1. Collect plastic")
        print("2. Leave the lake")

        action = input("Choose 1 or 2: ")

        if action == "1":
            print("You collected plastic and helped aquatic animals!")
            player.add_points(10)
        elif action == "2":
            print("You left the lake. The pollution remains.")
        else:
            print("Invalid choice. No points earned.")

    elif choice == "3":
        print("\n--- TOWN ROUTE ---")
        show_room(town)
        print("1. Organise recycling")
        print("2. Save electricity")

        action = input("Choose 1 or 2: ")

        if action == "1":
            print("You organised recycling and reduced waste!")
            player.add_points(10)
        elif action == "2":
            print("You saved electricity and helped the planet!")
            player.add_points(10)
        else:
            print("Invalid choice. No points earned.")

    elif choice == "4":
        show_score(player)

    elif choice == "5":
        print("\nThank you for playing,", player_name + "!")
        print("Your final score is:", player.show_score())
        print("Remember: Small actions can protect our planet!")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 5.")
        