# This function checks if a number is even or odd
def check_odd_even(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."
# Main function to execute the program
def main():
    num = int(input("Enter a number:"))
    result = check_odd_even(num)
    print(result)
# Entry point of the program
if __name__ == "__main__":
    main()