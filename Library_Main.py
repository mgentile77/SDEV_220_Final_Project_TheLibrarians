import Library_Mods as lm
from Library_Mods import *
import re

    
menu_start_page = """\n1 - Reports\t\t2 - Member Look-up\n3 - Book Look-up\t4 - Borrow Book
5 - End program"""
start = "\nSelect the number of the operation you want to complete: "
menu_reports_page = """\n1 - Run report for ALL books out\n2 - Run report for Late accounts
3 - Return to Start Page"""
menu_member_page = """\n1 - Search Member by Member ID\t\t2 - Search Member by Name and/or Phone
3 - Add new Member\t4 - Drop Member\t\t5 - Return to Start Page"""
menu_book_page = """\n1 - Search Book by Book ID\t\t2 - Search Book by Title and/or Author
3 - Add new Book\t4 - Drop Book\t5 - Return to Start Page"""
menu_borrow_page = """\n1 - Borrow a Book\t\t2 - Return a Book\n3 - Return to Start Page"""

def options(max, choice):
    if int(choice) == False or int(choice) > max:
        return False
    else:
        return True
    
def yesorno_ck(choice):
        if len(choice) < 2 and re.match("^[ENY]$", choice):
            return True
        else:
            return False 
    
def name_ck(name="", length = 100):
    if name == "":
        return True
    elif len(name) < length and not re.match("^[a-z]*$", name):
        return True
    else:
        return False

def number_ck(number = "", length = 1):
    if number == "":
        return True
    elif len(str(number)) == length and (re.match("^\d+$", str(number)) or re.match("^\d{3}-\d{3}-\d{4}$", str(number))):
        return True
    else:
        return False

def start_page():
    print(menu_start_page)
    main_menu_choice = input(start)
    while number_ck(main_menu_choice) == False:
        print("Your entry was not correct.\nPlease try again.\n")
        print(menu_start_page)
        main_menu_choice = input(start)
    main_menu_choice = int(main_menu_choice)
    if options(5,main_menu_choice) == False:
        start_page()
    elif main_menu_choice == 1:
        reports_page()
    elif main_menu_choice == 2:
        members_page()
    elif main_menu_choice == 3:
        books_page()
    elif main_menu_choice == 4:
        borrow_page()
    else:
        print ("Thank you for using the Library System")
        
def reports_page():
    print (menu_reports_page)
    reports_menu_choice = input (start)
    while number_ck(reports_menu_choice) == False:
        print("Your entry was not correct.\nPlease try again.\n")
        print(menu_reports_page)
        reports_menu_choice = input (start)
    reports_menu_choice = int(reports_menu_choice)
    if options(3, reports_menu_choice) == False:
        reports_page()
    elif reports_menu_choice == 1:
        lm.Report().bks_out_emails()
        reports_page()
    elif reports_menu_choice == 2:
        lm.Report().bks_late()
        reports_page()
    else:
        start_page()
        
def members_page():
    print (menu_member_page)
    members_menu_choice = input(start)
    while number_ck(members_menu_choice) == False:
        print("Your entry was not correct.\nPlease try again.\n")
        print(menu_member_page)
        members_menu_choice = input(start)
    members_menu_choice = int(members_menu_choice)
    if options(5, members_menu_choice) == False:
        members_page()
    elif members_menu_choice == 1:
        id = int(input("Enter Member ID: "))
        print(lm.Lib_Members().search_memID(id))
        members_page()
    elif members_menu_choice == 2:
        fname = input("Enter the first 2 letters of members First Name: ").capitalize()
        fn_ck = name_ck(fname,3)
        while fn_ck == False:
            fname = input("""The entry is not as requested.\nPlease check your entry and try again.
Enter the first 2 letters of members First Name: """).capitalize()
            fn_ck = name_ck(fname,3)
            print (fn_ck)
        lname = input("""Enter the first 2 letters of the members Last Name: """).capitalize()
        while name_ck(lname,3) == False:
            lname = input("""The entry is not as requested.\nPlease check your entry and try again.
Enter the first 2 letters of the members Last Name: """).capitalize()
        phone = input("Enter the last 4 numbers of the members Phone Number: ")
        while number_ck(phone,4) == False:
            phone = input("Enter the last 4 numbers of the members Phone Number: ")
        print(lm.Lib_Members().search_mem(fname,lname,phone))
        members_page()
    elif members_menu_choice == 3:
        fname = input("Enter the new members First Name: ").capitalize()
        while name_ck(fname) == False:
            fname = input("Enter the new members First Name: ").capitalize()
        lname = input("Enter the new members Last Name: ").capitalize()
        while name_ck(lname) == False:
            lname = input("Enter the new members Last Name: ").capitalize()
        street_add = input("Enter the new members Street Address: ").title()
        city = input("Enter the new members City: ").capitalize()
        while name_ck(city) == False:
            city = input("Enter the new members City: ").capitalize()
        state = input("Enter the new members State Abbreviation: ").upper()
        while name_ck(state, 3) == False:
            lname = input("Enter the new members State Abbreviation: ").upper()
        zip = input("Enter the new members Zip Code: ")
        while number_ck(zip, 5) == False:
            zip = input("Enter the new members Zip Code: ")
        email= input("Enter the new members Email: ").lower()
        phone = input("Enter the new members Phone Number (XXX-XXX-XXXX): ")
        while number_ck(phone,12) == False:
            phone = input("Enter the new members Phone Number (XXX-XXX-XXXX): ")
        print(lm.Lib_Members().add_mem(fname, lname, street_add, city, 
                                       state, zip, email, phone))
        members_page()
    elif members_menu_choice == 4:
        id = int(input("Enter Member ID you are removing from the library system: "))
        print(lm.Lib_Members().search_memID(id))
        correct_mem = input("\nIs this the correct member to remove? (Y/N or E to exit): ")
        while yesorno_ck(correct_mem) == False or correct_mem == "N":
            id = int(input("Enter Member ID you are removing from the library system: "))
            print(lm.Lib_Members().search_memID(id))
            correct_mem = input ("\nIs this the correct member to remove? (Y/N or E to exit): ").upper()
        if correct_mem == "E":
            members_page()
        else:
            print(lm.Lib_Members().drop_mem(id))
            members_page()        
    else:
        start_page()

def books_page():
    print (menu_book_page)
    books_menu_choice = input (start)
    while number_ck(books_menu_choice) == False:
        print("Your entry was not correct.\nPlease try again.\n")
        print(menu_book_page)
        books_menu_choice = input (start)
    books_menu_choice = int(books_menu_choice)
    if options(5, books_menu_choice) == False:
        books_page()
    elif books_menu_choice == 1:
        id = int(input("Enter Book ID: "))
        print(lm.Lib_Books().search_bkID(id))
        books_page()
    elif books_menu_choice == 2:
        fname = input("Enter the first 2 letters of members First Name: ").upper()
        while name_ck(fname,2) == False:
            fname = input("Enter the first 2 letters of members First Name: ").upper()
        lname = input("Enter the first 2 letters of the members Last Name: ").upper()
        while name_ck(lname,2) == False:
            lname = input("Enter the first 2 letters of members Last Name: ").upper()
        title = input("Enter up to 10 characters of the Books Title: ").upper()
        while name_ck(title,25) == False:
            title = input("Enter up to 10 characters of the Books Title: ").upper()
        print(lm.Lib_Books().search_book(title,fname,lname))
        books_page()
    elif books_menu_choice == 3:
        isbn = input ("Enter the books ISBN: ")
        while number_ck(isbn,10) == False:
            isbn = input ("Enter the books ISBN: ")
        title = input("Enter the Books Title: ").upper()
        author = input("Enter the Author's Full Name: ").upper()
        while name_ck(author) == False:
            author = input("Enter the Author's Full Name: ").upper()
        date_of_publication = input("Enter the Year of Publication: ")
        while number_ck(date_of_publication,4) == False:
            date_of_publication = input("Enter the Year of Publication: ")
        publisher = input("Enter the book's Publisher: ").upper()
        while name_ck(publisher) == False:
            publisher = input("Enter the book's Publisher: ").upper()
        print(lm.Lib_Books().add_book(isbn, title, author, date_of_publication, publisher))
        books_page()
    elif books_menu_choice == 4:
        id = int(input("Enter Book ID you are removing from the catalog: "))
        print(lm.Lib_Books().search_bkID(id))
        correct_bk = input ("\nIs this the correct book? (Y/N or E to exit): ").upper()
        while yesorno_ck(correct_bk) == False or correct_bk == "N":
            id = int(input("Enter Book ID you are removing from the catalog: "))
            print(lm.Lib_Books().search_bkID(id))
            correct_bk = input ("\nIs this the correct book? (Y/N or E to exit): ").upper()
        if correct_bk == "E":
            books_page()
        else:
            print(lm.Lib_Books().drop_book(id))
            books_page()        
    else:
        start_page()
        
def borrow_page():
    print (menu_borrow_page)
    borrow_menu_choice = input (start)
    while number_ck(borrow_menu_choice) == False:
        print("Your entry was not correct.\nPlease try again.\n")
        print(menu_borrow_page)
        borrow_menu_choice = input (start)
    borrow_menu_choice = int(borrow_menu_choice)
    if options(3, borrow_menu_choice) == False:
        borrow_page()
    elif borrow_menu_choice == 1:
        mem = input("Do you have the member ID? (Y/N or E to Exit): ").upper()
        if yesorno_ck(mem) == False or mem == "N":
            fname = input("Enter the first 2 letters of members First Name: ").capitalize()
            while name_ck(fname,3) == False:
                fname = input("Enter the first 2 letters of members First Name: ").capitalize()
            lname = input("Enter the first 2 letters of the members Last Name: ").capitalize()
            while name_ck(lname,3) == False:
                lname = input("Enter the first 2 letters of members Last Name: ").capitalize()
            phone = input("Enter the last 4 numbers of the members Phone Number: ")
            while number_ck(phone,4) == False:
                phone = input("Enter the last 4 numbers of the members Phone Number: ")
            print(lm.Lib_Members().search_mem(fname,lname,phone))
            memid = int(input("Please enter the Member ID: "))
            bkid = int(input("Please enter the Book ID: "))
            print(lm.Lib_Borrow().bor_bk(memid, bkid))
            next_bk = input("Would you like to add another Book? (Y/N): ").upper()
            while yesorno_ck(next_bk) == True and next_bk == "Y":
                bkid = int(input("Please enter the Book ID: "))
                print(lm.Lib_Borrow().bor_bk(memid, bkid))
                next_bk = input("Would you like to add another Book? (Y/N): ").upper()
            else:
                print(lm.Lib_Borrow().member_receipt(memid))
                borrow_page()
        elif mem == "Y":
            memid = int(input("Please enter the Member ID: "))
            bkid = int(input("Please enter the Book ID: "))
            print(lm.Lib_Borrow().bor_bk(memid, bkid))
            next_bk = input("Would you like to add another Book? (Y/N): ").upper()
            while yesorno_ck(next_bk) == True and next_bk == "Y":
                bkid = int(input("Please enter the Book ID: "))
                print(lm.Lib_Borrow().bor_bk(memid, bkid))
                next_bk = input("Would you like to add another Book? (Y/N): ").upper()
            print(lm.Lib_Borrow().member_receipt(memid))
            borrow_page()
        else:
            borrow_page()
    elif borrow_menu_choice == 2:
        bkid = int(input("Please enter the Book ID: "))
        print (lm.Lib_Borrow().ret_bk(bkid))
        print ()
        next_bk = input("Would you like to return another book? (Y/N): ").upper()
        while yesorno_ck(next_bk) == True and next_bk == "Y":
            bkid = int(input("Please enter the Book ID: "))
            print(lm.Lib_Borrow().ret_bk(bkid))
            next_bk = input("Would you like to return another book? (Y/N): ").upper()
        else:
            borrow_page()
    else:
        start_page()


if __name__ == start_page():
    start_page()