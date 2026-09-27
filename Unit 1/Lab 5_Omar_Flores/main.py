from books import Book
from user import User
from library import library
import sys

libreria = library()

def Register_Book():
    id_book = input("Enter the book's id: ")
    title= input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    editorial = input("Enter the book's editorial:")
    libreria.add_book(Book(id_book,title,author,editorial))

def Register_User():
    id_user = input("Enter the user's id: ")
    name= input("Enter the user's name: ")
    password = input("Enter the user's password: ")
    libreria.add_users(User(id_user,name,password))

def Borrow_Book():
    id_book = input("Enter the book's id: ")
    id_user = input("Enter the user's id: ")

    for x in libreria.users:
        if x.id_user == id_user:
            if x.borrow == False:
                print(f'The user with ID: "{id_user}" has already a book borrowed')
                return

            for i in libreria.books:
                if i.id_book == id_book:
                    if i.available == True:
                        x.borrow = False
                        i.available = False
                        print("The book was borrowed succesful")
                        return 
                    else:
                        print(f'The book with ID: "{id_book}" was borrowed to someone else')
                        return

            print(f'The book with ID: "{id_book}" does not exist')
            return

    print(f"The user with ID: {id_user} does not exist")


def Return_Book():
    id_book = input("Enter the book's id: ")
    id_user = input("Enter the user's id: ")

    for x in libreria.users:
        if x.id_user == id_user:
            if x.borrow == False:
                for i in libreria.books:
                    if i.id_book == id_book:
                        if i.available == False:
                            x.borrow = True
                            i.available = True
                            print("The book was returned successfully")
                            return 
                        else:
                            print(f'The book with ID: "{id_book}" is not borrowed')
                            return 
                
                print(f'The book with ID: "{id_book}" does not exist')
                return
            else:
                print(f'The user with ID: "{id_user}" has no books borrowed')
                return

    print(f"The user with ID: {id_user} does not exist")

opc=0
while opc!=5:
    print(f"\n1.-Register Book\n2.-Register User\n3.-Borrow a book\n4.-Return a book\n5.-Exit")
    opc = (input("\nEnter a option: "))
    match opc:
        case "1":
            Register_Book()
        case "2":
            Register_User()
        case "3":
            Borrow_Book()
        case "4":
            Return_Book()
        case "5":
            sys.exit()
        case _:
            print("Opcion invalida, vuelva a intentarlo.....")

#Requirements:
#1.-The system must allow register books
#2.-The system must allow register users
#3.-The system must allow a book to be borrowed by a user
#4.-The book that has already been borrowed cannot be borrow again
#5.-The system must allow a book to be returned