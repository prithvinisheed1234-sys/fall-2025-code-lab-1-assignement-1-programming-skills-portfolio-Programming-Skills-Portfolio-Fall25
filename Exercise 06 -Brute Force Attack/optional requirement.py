# Brute Force Attack Simulation with Limited Attempts
password = 7895
# The program will allow a maximum of 5 attempts to input the correct password.
max_attempts = 5
# Initialize attempt counter
attempts = 0
# Loop until the maximum number of attempts is reached
while attempts < max_attempts:
    a = int(input("Enter your password:"))
    attempts += 1
    if a == password:
        print("The password you entered is correct.")
        break
    else:
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("You entered too many incorrect passwords!")