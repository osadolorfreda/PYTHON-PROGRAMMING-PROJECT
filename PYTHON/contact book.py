def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, number in contacts.items():
            print(f"Name: {name}, Number: {number}")

def add_contact(contacts):
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contacts[name] = number
    print("Contact added.")

def search_contact(contacts):
    name = input("Enter the name to search: ")
    if name in contacts:
        print(f"Name: {name}, Number: {contacts[name]}")
    else:
        print("Contact not found.")

def remove_contact(contacts):
    name = input("Enter the name to remove: ")
    if name in contacts:
        del contacts[name]
        print("Contact removed.")
    else:
        print("Contact not found.")

def main():
    contacts = {}
    while True:
        print("\nContact Book")
        print("1. View contacts")
        print("2. Add contact")
        print("3. Search contact")
        print("4. Remove contact")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                display_contacts(contacts)
            elif choice == 2:
                add_contact(contacts)
            elif choice == 3:
                search_contact(contacts)
            elif choice == 4:
                remove_contact(contacts)
            elif choice == 5:
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()