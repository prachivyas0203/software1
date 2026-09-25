name = input("Enter name: ")

names = set()

while name != "":
    if name in names:
        print("Existing name")
        name = input("Enter name: ")
    else:
        print("New name")
        names.add(name)

for name in names:
    print(name)