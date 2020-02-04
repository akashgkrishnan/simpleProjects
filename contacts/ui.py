import contacts
from time import sleep
ch = contacts.menu()

while True:
    if ch == 1:
        name = input("Enter Name: ")
        mobile = int(input("Enter Mobile number: "))
        print(f"<saving -> {name}, {mobile} to DB...")
        sleep(1)
        print(contacts.save_contact(name, mobile))
        ch = contacts.menu()
        print('\n'*20)

    elif ch == 2:
        print("<PRINTING ALL CONTACTS...")
        sleep(2)
        all_contacts = contacts.all_contacts()
        for contact in all_contacts:
            print(f"NAME:  {contact[0]}         MOBILE:  {contact[1]}")
        ch = contacts.menu()
        print('\n'*20)
    elif ch == 3:
        name = input("Enter Name: ")
        print("<Searching {name} in contacts...")
        sleep(1)
        all_contacts = contacts.search_contact(name)
        for contact in all_contacts:
            print(f"NAME:  {contact[0]}         MOBILE:  {contact[1]}")
        ch = contacts.menu()
        print('\n'*20)

    elif ch == 4:
        name = input("Enter Name: ")
        print(f"<DELETING {name},FROM CONTACTS...")
        sleep(1)
        print(contacts.delete_contact(name))
        ch = contacts.menu()
        print('\n'*20)
    else:
        print("INVALID CHOICE: ")
        print("RETURNING TO MAIN MENU: ")
        print('\n'*20)
        ch = contacts.menu()


