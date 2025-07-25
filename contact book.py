contacts = {}
def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print("Contact added!")

def view_contacts():
    if not contacts:
        print("No contacts saved.")
        return
    for name, info in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print(f"Address: {info['address']}")

def search_contact():
    search = input("Enter name or phone to search: ")
    found = False
    for name, info in contacts.items():
        if search == name or search == info['phone']:
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        print("Leave field blank to keep existing value.")
        phone = input(f"New phone [{contacts[name]['phone']}]: ") or contacts[name]['phone']
        email = input(f"New email [{contacts[name]['email']}]: ") or contacts[name]['email']
        address = input(f"New address [{contacts[name]['address']}]: ") or contacts[name]['address']
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print("Contact updated!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\n1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n6. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        break
    else:
        print("Invalid option.")
