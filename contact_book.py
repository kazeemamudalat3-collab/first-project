# Create a contact book using a dictionary.
# Your program should allow the user to:
# Add a contact
# Search for a contact
# Delete a contact
# Display all contacts


# choice = ""

# while choice != 5:
#     choice = input("Enter an option you'd like to choose\n1. Add contact\n2. Search contact\n3. Delete contact\n4. Display all contacts\n5. Exit\n")

#     if choice == "1":
#         print("Adding contact")

#     elif choice == "2":
#         print("Searching contacts ")

#     elif choice == "3":
#         print("Deleting contact")

#     elif choice == "4":
#         print("Displaying all contacts")

#     elif choice == "5":
#         print("Exit")

#     else:
#         print("Invalid Choice\n Please make the correct choice  ")
ContactBook = {'lola':1234
               ,'daniel' : 625662
                 ,'lily' :90123  }



choice = ""

while choice != "5":
    choice = input("Choose \n1 to add a new contact\n2 to search for a contact\n3 to delete a contact\n4 to display all contacts\n5 to exit:\n")

    print("You entered:", choice)

    if choice == "1":
        print("Adding contact")
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        ContactBook[name] = phone

        print("\nContact added successfully!")


    elif choice == "2":
        print("Searching contacts")

        SearchContact = input("Enter contact you'd like to search: ")

        if SearchContact in ContactBook:
            print(f"{SearchContact}: {ContactBook[SearchContact]}")
        else:
            print("Contact not found")

    elif choice == "3":
        print("Deleting contact")
        DeleteContact = input("Enter contact you'd like to delete: ")
        if DeleteContact in ContactBook:
            del ContactBook[DeleteContact]
            print(f"{DeleteContact}'s contact successfully deleted")
        else:
            print("contact non-existent")

    elif choice == "4":
        print("Displaying contacts")
        print("\nAll Contacts:")

        for name, phone in ContactBook.items():
            print(f"{name}: {phone}")

    elif choice == "5":
        print("Exit")

    else:
        print("Invalid choice")








# print (ContactBook)
