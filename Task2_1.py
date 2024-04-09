import contacts_manager as cm

# Task 1: Contact List Manager

# Problem Statement: Create a Python script using a custom module to manage a contact list. 
# The script should allow adding, removing, and displaying contacts stored in a list.
# Code Example:
# contacts_manager.py
# Define functions to add, remove, and display contacts

# main.py
# Implement the logic to interact with the contact manager
# Expected Outcome: Your script should be able to add new contacts, remove existing contacts, 
# and display all contacts. Each contact can be a dictionary with a name and phone number.

while True:
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Display Contacts")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone: ")
        cm.add_contact(name, phone)
    elif choice == "2":
        name = input("Enter contact name to remove: ")
        cm.remove_contact(name)
    elif choice == "3":
        cm.display_contacts()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")