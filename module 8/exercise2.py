name = input("Enter name: ")

names = set()

while True:
    name = input("Enter a name: ")

    if name == "":
        break

    if name in names:
        print("Existing name")
        name = input("Enter name: ")
    else:
        print("New name")
        names.add(name)

print("Entered names:")

for name in names:
    print(name)