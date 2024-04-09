import text_utils as tu

# Task 1: Custom Module with Aliases

# Problem Statement: Create a custom module named text_utils.py with functions for string 
# manipulation (e.g., reversing a string, capitalizing). In your main script, import this 
# module using an alias and utilize its functions.
# Code Example:
# text_utils.py
# def reverse_string(s):
    # function to reverse a string

# def capitalize_string(s):
    # function to capitalize a string

# main.py
# Import text_utils using an alias and utilize its functions
# Expected Outcome: Your main script should be able to use the functions from text_utils.py via an alias, demonstrating an understanding of custom module creation and aliasing.

while True:
    print("1. Reverse String")
    print("2. Capitalize String")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        s = input("Enter a string to reverse: ")
        print(f"Reversed String: {tu.reverse_string(s)}")
    elif choice == "2":
        s = input("Enter a string to capitalize: ")
        print(f"Capitalized String: {tu.capitalize_string(s)}")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")