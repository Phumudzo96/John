wrong_names = []                                    # create a variable with an empty list
name = input("Enter your name: ").lower()                   # ask user to enter a name

while name != "harry":                                  # set name to be "harry"
    wrong_names.append(name)                        # If the user doesnt enter the set name, store the name entered
    name = input("Enter your name: ")

print(f"Incorrect names = {wrong_names}")           # Print out all the incorrect names

