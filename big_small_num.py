#!/usr/bin/env python3
# Created By: Tony Tran
# Date: November. 14, 2023
# This program finds the smallest and the biggest number from user responses.


def main():
    # Sets initial values for the biggest and smallest numbers
    biggest_num = float("-inf")  # Initialize with negative infinity
    smallest_num = float("inf")  # Initialize with positive infinity

    # Welcome message
    print(
        "HELLO! WELCOME TO MY PROGRAM I WILL GET YOUR SET OF NUMBERS AND PRINT OUT THE SMALLEST AND THE BIGGEST NUMBER PROVIDED!"
    )

    # Loop to get user numbers until 'q' is entered
    while True:
        user_num = input("Enter a number (or q to quit): ")
        if user_num.lower() == "q":
            break
        else:
            try:
                num = float(user_num)
            except ValueError:
                # Handles non-numeric inputs
                print(f"{user_num} is not a number. ", end="")
            else:
                # Updates the biggest and smallest numbers accordingly
                if num > biggest_num:
                    biggest_num = num
                if num < smallest_num:
                    smallest_num = num

    # Prints the largest and smallest numbers entered by the user
    print(
        f"The largest number entered is: {biggest_num}\nThe smallest number entered is: {smallest_num}"
    )


if __name__ == "__main__":
    main()
