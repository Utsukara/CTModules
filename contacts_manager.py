
contact_list = []

def add_contact(name, phone):
    contact = {"name": name, "phone": phone}
    contact_list.append(contact)
    print(f"Contact {name} added successfully!")

def remove_contact(name):
    for contact in contact_list:
        if contact["name"] == name:
            contact_list.remove(contact)
            print(f"Contact {name} removed successfully!")
            return
    print(f"Contact {name} not found!")

def display_contacts():
    if len(contact_list) == 0:
        print("No contacts found!")
    else:
        for contact in contact_list:
            print(f"{contact['name']}: {contact['phone']}")