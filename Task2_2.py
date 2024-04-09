from datetime import datetime

# Task 2: Date Extractor

# Problem Statement: Write a Python program that uses the datetime module to extract and 
# display the current month and year. Additionally, allow the user to input a date string 
# and parse it into a datetime object.
# Code Example:
# main.py
# from datetime import datetime
# Implement code to display the current month and year
# Implement code to parse a user-input date string into a datetime object
# Expected Outcome: The program should accurately display the current month and year 
# and successfully convert a user-input date string (e.g., "2023-03-15") into a datetime 
# object, handling any invalid inputs gracefully.

def display_current_month_and_year():
    now = datetime.now()
    current_month = now.strftime("%B")
    current_year = now.year
    print(f"Current Month: {current_month}")
    print(f"Current Year: {current_year}")

def parse_date_string(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        print(f"Parsed Date: {date_obj}")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    display_current_month_and_year()
    date_input = input("Enter a date (YYYY-MM-DD): ")
    parse_date_string(date_input)