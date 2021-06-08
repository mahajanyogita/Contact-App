from Model import contact as c
from repository import repository
from check_list import *

print("\t\t\tCONTACT LOG")

while True:
    repo = repository.Repository()
    print("\nChoose one of the following Option :")
    choice = int(input("\n1 : Add Contact \n2 : Edit Contact \n3 : Search Contact \n4 : Display All Contacts \n5 : Delete Contact \n6 : Exit  \nEnter Choice ==>   "))

    #to add Contact
    if choice == 1:
        fname = input("\nEnter First Name : ")
        lname =   input("Enter Last Name  : ")
        while True :
            try:
                phone_number = input("\nEnter Phone Number : ")
                isValid_Phone(phone_number)
            except Exception as e:
                print(e)
            else:
                break

        while True:
            try:
                email_id = input("\nEnter email_id     : ")
                check_email(email_id)
            except Exception as e:
                print(e)
            else:
                break

        contacts = c.Contact(fname, lname, phone_number, email_id)
        output=repo.add_contact(contacts)
        print("\n",output[0],"\n",output[1])

    #to Edit Contact
    elif choice == 2:
        try:
            print("\nTo Edit Contact")
            fname = input("\nEnter First Name : ")
            lname = input("Enter Last Name  : ")
            print("\n",repo.search_by_name(fname,lname))
            while True:
                print("\nselect Edit option :")
                edit_choice = input("\nA:Edit Name \nB:Edit Phone Number \nC:Edit Email Id \nD:EXIT\n ==>")

                if edit_choice == "A":

                    edit_fname = input("\nEnter Updated First Name :  ")
                    edit_lname = input("Enter Updated Last Name :  ")
                    output=repo.edit_contact(fname, lname, edit_fname, edit_lname)
                    print("\n",output[0],"\n",output[1])
                    fname=edit_fname
                    lname=edit_lname

                elif edit_choice == "B":
                    while True:
                        try:
                            edit_phone_number = input("\nEnter Updated Phone Number : ")
                            isValid_Phone(edit_phone_number)
                        except Exception as e:
                            print(e)
                        else:
                            break

                    output=repo.edit_contact_phone_no(fname, lname, edit_phone_number)
                    print("\n",output[0], "\n", output[1])

                elif edit_choice == "C":
                    while True:
                        try:
                            edit_email_id = input("\nEnter Updated Email Id:  ")
                            check_email(edit_email_id)
                        except Exception as e:
                            print(e)
                        else:
                            break

                    output=repo.edit_contact_email(fname, lname, edit_email_id)
                    print("\n",output[0], "\n", output[1])

                elif edit_choice == 'D':
                    break

                else:
                    print("Invalid choice")

        except Exception as e:
            print(e)

    #to search contact
    elif choice == 3:
        try:
            while True:
                search_choice = input("\nA:Search By Name \nB:Search By Phone No\nC:Exit\n==>")
                if search_choice == 'A':
                    fname=input("\nEnter First Name: ")
                    lname=input("Enter Last Name :  ")
                    print("\n",repo.search_by_name(fname,lname))
                elif search_choice == 'B':
                    phone_number=input("Enter Phone No : ")

                    print("\n",repo.search_by_phone_no(phone_number))
                elif search_choice == 'C':
                    break
                else:
                    print("Invalid Choice")
        except Exception as e:
            print(e)

    #to show all contacts
    elif choice == 4:
        print("\n\t\tContact Log\n")
        try:
            contacts=repo.show_all_contacts()
            for contact in contacts:
                print(contact)
        except Exception as e:
            print(e)

    #to delete contact
    elif choice == 5:
        fname = input("\nEnter First Name: ")
        lname = input("Enter Last Name :  ")
        print("\n",repo.delete_contact_by_name(fname, lname))

    elif choice == 6:
        break

    else:
        print("Invalid Choice")

