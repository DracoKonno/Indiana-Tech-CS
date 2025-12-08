#1.1
#Contact Structure
from datetime import datetime

from homework1_Konno_Draco import contact_data

def create_contact():
    #input validation for required contact info
    def get_required_input(prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print(("This field is required, please enter a value"))
            
    #collect required contact info
    first_name = get_required_input("enter first name: ")
    last_name = get_required_input("enter last name: ")
    phone = get_required_input("enter phone number: ")
    
    #collect optional data
    email = input("enter email (optional): ")
    address = input("enter address (optional): ")
    category = input("enter type of contact (personal, work, family)(optional): ")
    notes = input("enter any additional notes (optional): ")
    
    #timestamps
    timestamp = datetime.now().isoformat()
    
    contact = {
        "first_name": first_name.upper,
        "last_name": last_name.upper, 
        "phone": phone,
        "email": email if email else "",
        "address": address if address else "",
        "category": category.upper if category else "",
        "note": notes if notes else "",
        "created_date": timestamp,
        "last_modified": timestamp
    }
    
    return contact

#1.2 implementation
contacts_db = {
    
}

def generate_contact_id(contact):
    #generate a unique contact id
    timestamp = contact["created_date"].strftime("%Y%m%d%H%M%S")
    name_part = contact["first_name"][:2] + contact["last_name"][:2]
    return f"{name_part}_{timestamp}"

def add_contact(contacts_db, contact_data):
    if not contact_data.get("first_name") or not contact_data.get("last_name") or not contact_data.get("phone"):
        print("Error: Missing Required contact fields.")
        return None
    
    contact_id = generate_contact_id(contact_data)
    contacts_db[contact_id] = contact_data
    print(f'Contact added with ID: {contact_id}')
    return contact_id

def display_contact(contacts_db, contact_id):
    #Display a formatted view of a single contact
    contact = contacts_db.get(contact_id)
    if contact:
        print(f'Contact ID: {contact_id}')
        print(f'Name: {contact['first_name']} {contact['last_name']}')
        print(f'Phone: {contact['phone']}')
        print(f'Email: {contact['email']}')
        print(f'Address: {contact['address']}')
        print(f'Category: {contact['category']}')
        print(f'Note: {contact['note']}')
        return True
    else:
        print("Contact Not Found")
        return False

def list_all_contacts(contacts_db):
    #Display a summary list of all contacts
    if not contacts_db:
        print("No contacts Available")
        return

    print("All Contacts")
    for contact_id, contact in contacts_db.items():
        full_name = f"{contact['first_name']} {contact['last_name']}"
        print(f"Id: {contact_id} | Name: {full_name} | Phone: {contact['phone']}")