import os
def menu():
    print("\nContact Management System")
    print("1. View All Contacts")
    print("2. Add Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Save and Exit")
    
# Task 1: Function to load contacts from a file
def load_contacts(file_name):
    contacts = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts.append({"name": name, "phone": phone})
    return contacts

# Task 2: Function to save contacts to a file
def save_contacts(file_name, contacts):
    with open(file_name, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']}\n")

# Task 3: Function to add a contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts.append({"name": name, "phone": phone})
    print(f"Contact '{name}' added successfully.")

# Task 4: Function to view all contacts
def view_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        print("\nContacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

# Task 5: Function to update a contact
def update_contact(contacts):
    name = input("Enter the name of the contact you want to update: ")
    contact_found = False
    for contact in contacts:
        if contact['name'] == name:
            new_name = input(f"Enter new name for {name} (leave blank to keep the same): ")
            new_phone = input(f"Enter new phone for {name} (leave blank to keep the same): ")
            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            contact_found = True
            print(f"Contact '{name}' updated successfully.")
            break
    if not contact_found:
        print(f"No contact found with the name '{name}'.")

# Task 6: Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    contact_found = False
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            contact_found = True
            print(f"Contact '{name}' deleted successfully.")
            break
    if not contact_found:
        print(f"No contact found with the name '{name}'.")

# Task 7: Main function to run the Contact Management System
def main():
    file_name = "contacts.txt"
    contacts = load_contacts(file_name)
    
    while True:
        menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(file_name, contacts)
            print("Contacts saved. Exiting the system.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the Contact Management System
if __name__ == "__main__":
    main() 


    
