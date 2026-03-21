# Contact Book Manager

# 📌 Build a simple contact management system — add, search, and delete contacts. This simulates a real CRUD (Create, Read, Update, Delete) operation.
# 🎯 Task: Build 4 functions: add_contact(), search_contact(name), delete_contact(name), and show_all(). Store contacts in a list of dicts with name, phone, email.
# Contact Book Manager
contacts = []  # List of dicts

def add_contact(name, phone, email):
    contact = {
        "name" : name,
        "phone" : phone,
        "email" : email
    }
    contacts.append(contact)
    print(f"{name} successfully added")

def search_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            print(f"{name}: contact found")
            return
    print("contact not found")

def delete_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print(f"{name} successfully deleted")
            return
    print("contact not found")  

def show_all():
    if not contacts:
        print("No contacts available.")
        return
    print("All contacts\n")
    for contact in contacts:
        print(contact)

# Test it:
add_contact("Rahul Sharma", "9876543210", "rahul@email.com")
add_contact("Priya Singh", "9123456789", "priya@email.com")
show_all()
search_contact("Rahul Sharma")
delete_contact("Priya Singh")
show_all()