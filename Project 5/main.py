import os


def read_file(filename):
    with open(filename,"r") as file:
        return file.read()


def save_game(name, score):
    with open("savegame.txt", "w") as file:
        file.write(name + "\n")
        file.write(str(score))


def load_game(name):
    if not os.path.exists("savegame.txt"):
        return None

    with open("savegame.txt", "r") as file:
        saved_name = file.readline().strip()
        saved_score = file.readline().strip()

    if saved_name == name:
        return int(saved_score)

    return None


print(read_file("intro.txt"))
print(read_file("instructions.txt"))

name = input("Enter your name: ")

saved_score = load_game(name)

if saved_score is not None:
    print("Welcome back, " + name + "!")
    print("Your saved score is:", saved_score)
    score = saved_score
else:
    print("Welcome, " + name + "!")
    print("Starting a new game.")
    score = 0


while True:
    print("\nChoose an action:")
    print("1. Explore")
    print("2. Rest")
    print("3. Save and quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You explored the area and found something useful!")
        score += 10
        print("Your score is now:", score)

    elif choice == "2":
        print("You rested and recovered.")
        score += 5
        print("Your score is now:", score)

    elif choice == "3":
        save_game(name, score)
        print("Game saved successfully!")
        print("Goodbye, " + name + "!")
        break

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")