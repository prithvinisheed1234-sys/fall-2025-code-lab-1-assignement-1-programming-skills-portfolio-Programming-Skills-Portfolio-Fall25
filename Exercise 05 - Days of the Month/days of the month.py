# This program prompts the user to enter a month number (1-12)
months = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31}
# and then displays the number of days in that month.
user_input = int(input("Enter the month number (1-12): "))
# Check if the input is valid and display the number of days
if (user_input in months):
    print(f"The month {user_input} has {months[user_input]} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")