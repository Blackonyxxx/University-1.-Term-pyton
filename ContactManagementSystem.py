contacts =[] 

def add_contact(name,phone_number,email):
     for contact in contacts:
          if contact["phone_number"] == phone_number or contact["email"] == email:
              print("This phone number or email allready exist")
              return 
          
     new_contact = {"name": name, "phone_number": phone_number, "email": email}
     contacts.append(new_contact)

def display_contacts():
     if not contacts:
          print("There is no contacts")
     else:
          for contact in contacts:
               print(f"Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}\n")

def display_menu():
     print("write \"add\" to add a new contact")
     print("write \"display\" to display all contacts")
     print("write \"search\" to search a contact")
     print("write \"delete\" to delete a contact")
     print("write \"update\" to update a contact")
     print("write \"exit\" to end the program")

def search_contact(name):
    found_contacts = [contact for contact in contacts if contact["name"].lower() == name.lower()]

    if found_contacts:
        for contact in found_contacts:
               print(f"Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}")
    else:
        print("Contacts can not found")

def delete_contact(contact_to_be_deleted):
    found = False
    if "@" in contact_to_be_deleted:
        for contact in contacts[:]:
            if contact["email"] == contact_to_be_deleted:
                contacts.remove(contact)
                found = True
                print("Contact deleted successfully.")
    else:
        for contact in contacts[:]:
            if contact["phone_number"] == contact_to_be_deleted:
                contacts.remove(contact)
                found = True
                print("Contact deleted successfully.")
    
    if not found:
        print("Contact not found.")

def update_contact(contact_to_be_modified, new_name, new_phone_number, new_email):
    for contact in contacts:
        if contact["phone_number"] == contact_to_be_modified or contact["email"] == contact_to_be_modified:
            contact["name"] = new_name
            contact["phone_number"] = new_phone_number
            contact["email"] = new_email
            return
    print("Contact can not found.")


def main():
    while (True):
         display_menu()
         operation=input("choose an operation: ")

         if (operation.lower() == "add".lower()):
               add_contact(name=input("write a name "), phone_number=input("write a phone number "), email=input("write a mail "))
         elif (operation.lower() == "display".lower()):
               display_contacts()
         elif (operation.lower() == "search".lower()):
               search_contact(name=input("write a name "))
         elif operation.lower() == "delete":
            delete_contact(contact_to_be_deleted=input("Write a phone number or email: "))
         elif operation.lower() == "update":
            update_contact(
                contact_to_be_modified=input("Write a phone number or email: "),
                new_name=input("Write a new name: "),
                new_phone_number=input("Write a new phone number: "),
                new_email=input("Write a new email: ")
            )
         elif (operation.lower() == "exit".lower()):
               print("Program is over")
               break
         else:
               print("!!INVALİD OPERATİON!!")

main()