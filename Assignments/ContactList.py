
operations_on_contact_list = ["1.Add Contact","2.Delete Contact","3.Update Contact","4.Show Contact","5.Exit"]

def display_phonebook_options():
    for option in operations_on_contact_list:
        print(option)

def display_contacts():
    contactFile = open('ContactList.txt', 'r')
    contactList = contactFile.read().splitlines()
    for i in range(0,len(contactList)-1):
        print(f"{i}.{contactList[i]}")


def add_contact():
    name = input("Enter the name of the person")
    number = input("Enter the contact number of the person")
    contactFile = open('ContactList.txt','a')
    contactFile.write(f"{name}:{number}" + "\n")
    contactFile.close()
    display_contacts()


def update_contact():
    display_contacts()
    updateChoice = int(input("Enter the number of the contact that you want to update: "))
    contactFile = open('ContactList.txt', 'r')
    contactList = contactFile.read().splitlines()
    contactFile.close()
    updateContactChoice = contactList[updateChoice-1]
    updatename = updateContactChoice.split(":")[0]
    updatenumber = updateContactChoice.split(":")[1]
    updatenameContact = int(input("enter 1 for name 2 for contact number"))

    if updatenameContact == 1:
        updatename = input("Enter the updated name.")
    elif updatenameContact == 2:
        updatenumber = input("Enter the new number")
    contactList[updateChoice-1] = f"{updatename}:{updatenumber}"
    contactFile = open('ContactList.txt', 'w')
    for contact in contactList:
        contactFile.write(contact + "\n")
    print("Your updated contact list is as follows..")


def delete_contact():
    display_contacts()
    contactFile = open('ContactList.txt', 'r')
    contactList = contactFile.read().splitlines()
    contactFile.close()
    deleteChoice = int(input("Enter the number of the contact that you want to delete:"))
    contactList.pop(deleteChoice-1)
    contactFile = open('ContactList.txt', 'w')
    for contact in contactList:
        contactFile.write(contact + "\n")

    contactFile.close()
    display_contacts()
    # display_phonebook_options()


while True:
    print("Welcome to Phone Book App")

    display_phonebook_options()
    user_choice = int(input("Enter your choice number: "))

    if user_choice == 5:
        exit()
    elif user_choice == 1:
        add_contact()
    elif user_choice == 2:
        delete_contact()
    elif user_choice == 3:
        update_contact()
        # display_contacts()
    elif user_choice == 4:
        display_contacts()
    else:
        exit()


