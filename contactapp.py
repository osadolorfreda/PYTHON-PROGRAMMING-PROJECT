contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contact = {"name": name, "phone": phone}
    contacts.append(contact)
    print("Contact added!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact["name"]}, Phone: {contact["phone"]}")

def search_contact():
    search_name = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print(f'Found - Name: {contact["name"]}, Phone: {contact["phone"]}')
            found = True
    if not found:
        print("Contact not found.")

while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")
    choice = input("select your choice 1-4: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid input")

print(contacts)

