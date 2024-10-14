# Define the filename where the contacts will be stored
CONTACT_FILE = 'contacts.txt'

# Function to read contacts from the file
def read_contacts():
    contacts = {}
    try:
        with open(CONTACT_FILE, 'r') as file:
            for line in file:
                name, phone, address, post = line.strip().split(',')
                contacts[name] = (phone, address, post)  # Store all details as a tuple
    except FileNotFoundError:
        pass
    return contacts

# Function to write contacts to the file
def write_contacts(contacts):
    with open(CONTACT_FILE, 'w') as file:
        for name, details in contacts.items():
            phone, address, post = details
            file.write(f'{name},{phone},{address},{post}\n')

# Function to add a contact
def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact number: ").strip()
    address = input("Enter address: ").strip()
    post = input("Enter post: ").strip()
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = (phone, address, post)  # Store all details
        print("Contact added successfully.")
    write_contacts(contacts)

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")
    write_contacts(contacts)

# Function to update a contact
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        new_phone = input(f"Enter new phone number for {name}: ").strip()
        new_address = input(f"Enter new address for {name}: ").strip()
        new_post = input(f"Enter new post for {name}: ").strip()
        contacts[name] = (new_phone, new_address, new_post)  # Update all details
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact not found.")
    write_contacts(contacts)

# Function to search for a contact
def search_contact(contacts):
    name = input("Enter the name of the contact to search: ").strip()
    if name in contacts:
        phone, address, post = contacts[name]
        print(f"Name: {name}, Phone: {phone}, Address: {address}, Post: {post}")
    else:
        print("Contact not found.")

# Function to display menu
def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. Search Contact")
    print("5. Exit")

# Main loop
def main():
    contacts = read_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            delete_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

# Run the main loop
if __name__ == "__main__":
    main()
