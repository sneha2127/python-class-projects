# Contact Application

# Welcome to contact app
# 1. Add contact
# 2. Show contact
# 3. Update contact
# 4. Delete contact
# Choose from the above(1,2,3 or 4): 1

# Add Contact
# Enter name: Pritam
# Enter Phone: 9382637127
# Your contact has been saved!

# name:Pritam,Phone:9382637127


# ------------------------------------------------------------------------
print("Welcome to contact app")

menus = ["Add Contact", "Show Contact", "Update Contact", "Delete Contact", "Exit"]
while True:
    print("------------------------------------------------------")
    # Menu Show
    for i in range(len(menus)):
        print(f"\n{i+1}. {menus[i]}")

    print("------------------------------------------------------")


    user_choice = input("Choose a number from the above: ")


    if user_choice == "5":
        exit()


    elif user_choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        file = open("contact.txt",'a')
        file.write(f"Name:{name},Phone:{phone}\n")
        file.close()
        print("Your contact has been added!")


    elif user_choice == "2":
        print("Your all contacts are: \n")
        file = open('contact.txt',"r") 
        contacts = file.readlines()
        for i in range(len(contacts)):
            print(f"{i+1}. {contacts[i]}")


    elif user_choice == "4":
        print("Your all contacts are: \n")
        file = open('contact.txt',"r") 
        contacts = file.readlines()
        file.close()
        for i in range(len(contacts)):
            print(f"{i+1}. {contacts[i]}")
        delete_number = int(input("Enter the number you want to delete(ex:1/2/3 or ....): "))


        contacts.pop(delete_number-1)


        file = open('contact.txt','w')
        for contact in contacts:
            file.write(contact)
        file.close()
        print("Your contact has been deleted!")


    elif user_choice == "3":

        print("Your all contacts are: \n")
        file = open('contact.txt',"r") 
        contacts = file.readlines()
        file.close()
        for i in range(len(contacts)):
            print(f"{i+1}. {contacts[i]}")
        update_number = int(input("Enter the number you want to update(ex:1/2/3 or ....): "))
        
        # contacs = ["c1\n", "c2\n", "c3\n"]
        # contacts[update_number - 1] = "c4\n"


        # New Contact 
        name = input("Enter updated name:")
        phone = input("Enter updated phone:")

        contacts[update_number-1] = f"Name:{name},Phone:{phone}\n"

        # Overwriting File
        file = open('contact.txt','w')
        for contact in contacts:
            file.write(contact)
        file.close()
        print("Your contact has been updated!")


    


