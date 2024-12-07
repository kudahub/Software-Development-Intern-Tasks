import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"


def load_contacts():
    """Load contacts from the JSON file."""
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)


def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!\n")


def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts found.\n")
        return

    print("\nContact List:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print()


def edit_contact(contacts):
    """Edit an existing contact."""
    view_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("Enter the contact number to edit: ")) - 1
        if index < 0 or index >= len(contacts):
            print("Invalid contact number.\n")
            return

        print(f"Editing contact: {contacts[index]['name']}")
        contacts[index]["name"] = input("Enter new name (leave blank to keep current): ").strip() or contacts[index]["name"]
        contacts[index]["phone"] = input("Enter new phone number (leave blank to keep current): ").strip() or contacts[index]["phone"]
        contacts[index]["email"] = input("Enter new email address (leave blank to keep current): ").strip() or contacts[index]["email"]

        save_contacts(contacts)
        print("Contact updated successfully!\n")

    except ValueError:
        print("Invalid input. Please enter a valid number.\n")


def delete_contact(contacts):
    """Delete an existing contact."""
    view_contacts(contacts)
    if not contacts:
        return

    try:
        index = int(input("Enter the contact number to delete: ")) - 1
        if index < 0 or index >= len(contacts):
            print("Invalid contact number.\n")
            return

        deleted_contact = contacts.pop(index)
        save_contacts(contacts)
        print(f"Contact '{deleted_contact['name']}' deleted successfully!\n")

    except ValueError:
        print("Invalid input. Please enter a valid number.\n")


def contact_manager():
    """Main program loop for the contact manager."""
    contacts = load_contacts()

    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the program
contact_manager()
