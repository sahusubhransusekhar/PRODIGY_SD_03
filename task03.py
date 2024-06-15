import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from a file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Save contacts to a file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact '{name}' added.")

def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def edit_contact(contacts):
    """Edit an existing contact."""
    name = input("Enter the name of the contact to edit: ")
    if name not in contacts:
        print(f"No contact found with the name '{name}'.")
        return

    print(f"Editing contact '{name}'")
    phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
    email = input(f"Enter new email address (current: {contacts[name]['email']}): ")

    contacts[name] = {
        "phone": phone if phone else contacts[name]['phone'],
        "email": email if email else contacts[name]['email']
    }

    save_contacts(contacts)
    print(f"Contact '{name}' updated.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ")
    if name not in contacts:
        print(f"No contact found with the name '{name}'.")
        return

    del contacts[name]
    save_contacts(contacts)
    print(f"Contact '{name}' deleted.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()