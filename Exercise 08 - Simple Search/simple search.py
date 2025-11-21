# Simple search program
names = ["Jake","Zac", "Ian", "Ron", "Sam", "Dave"]
# Ask the user to enter a name to search for
search = input("Enter your name:")
# Check if the name is in the list and print the appropriate message
if search in names:
    print(f"{search} is there on the list")
else:
    print(f"{search} is not there in the list")