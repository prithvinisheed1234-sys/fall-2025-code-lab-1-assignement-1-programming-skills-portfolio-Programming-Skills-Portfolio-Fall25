# Dictionary to hold the number of days in each month
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
# Get user input for the month
a = int(input("Enter your month:"))
# Check if the month is valid
if 1 <= a <= 12:
    if a == 2:
        leap = input("Is it a leap year?:")
        if leap == "yes":
            print("February has 29 days")
        else:
            print("February has 28 days")
    else:
        print(f"Month {a} has {months[a]} days.")
else:
    print("This month number doesn't exist.")