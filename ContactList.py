Contact_File = 'ContactsP.txt'

def read_contacts():
    contacts={}
    try:
        with open(Contact_File,'r') as file:
            for lines in file:
                name,phone = lines.strip().split(',')
                contacts[name]=phone 
    except FileNotFoundError:
        pass
    return contacts


def reading():
    record = {}
    try :
        with open(Contact_File,'r') as file:
            for lines in file:
                name,phone = lines.strip().split(',')
                record[name]=phone
    except FileNotFoundError:
        pass
    return record


            
             
































def search_contacts(contacts):
    name = input("Enter The Name you wanted to search").strip
    if name in contacts:
        print("Name : {name}Phone{contacts[name]}")
    else:
        print("Contact not found.")
    
def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. Search Contact")
    print("5. Exit")


def main():
    contacts= read_contacts()
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == '4':
            search_contacts(contacts)
        else:
            print("Enter the correct number")


if __name__ == "__main__":
    main()
        