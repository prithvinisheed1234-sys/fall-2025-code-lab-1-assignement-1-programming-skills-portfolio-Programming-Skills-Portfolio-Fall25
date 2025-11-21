# Brute Force Attack Simulation
password = 7895
# The program will keep asking the user to input the password until the correct one is entered.
while True:
    a = int(input("Enter your password:"))
    if a == password:
        print("The password you entered is correct.")
        break
    else:
        print("The password you entered is incorrect")
