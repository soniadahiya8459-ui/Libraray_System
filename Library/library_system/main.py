"""
Library Inventory System - Main Application
Author: Student Name
Date: November 21, 2025
Assignment: Programming for Problem Solving Using Python - Assignment 3
Description: Main entry point for the library management system with interactive menu
"""

from library import Library


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("=" * 60)
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Library Report")
    print("6. View All Books")
    print("7. View All Members")
    print("8. Exit")
    print("=" * 60)


def add_book_menu(library):
    """Handle adding a new book."""
    print("\n--- Add New Book ---")
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    isbn = input("Enter ISBN: ").strip()
    
    if title and author and isbn:
        library.add_book(title, author, isbn)
    else:
        print("Error: All fields are required!")


def register_member_menu(library):
    """Handle registering a new member."""
    print("\n--- Register New Member ---")
    name = input("Enter member name: ").strip()
    member_id = input("Enter member ID: ").strip()
    
    if name and member_id:
        library.register_member(name, member_id)
    else:
        print("Error: All fields are required!")


def borrow_book_menu(library):
    """Handle borrowing a book."""
    print("\n--- Borrow Book ---")
    member_id = input("Enter member ID: ").strip()
    isbn = input("Enter book ISBN: ").strip()
    
    if member_id and isbn:
        library.lend_book(member_id, isbn)
    else:
        print("Error: All fields are required!")


def return_book_menu(library):
    """Handle returning a book."""
    print("\n--- Return Book ---")
    member_id = input("Enter member ID: ").strip()
    isbn = input("Enter book ISBN: ").strip()
    
    if member_id and isbn:
        library.take_return(member_id, isbn)
    else:
        print("Error: All fields are required!")


def view_all_books(library):
    """Display all books in the library."""
    print("\n--- All Books in Library ---")
    if not library.books:
        print("No books in the library yet.")
    else:
        for i, book in enumerate(library.books, 1):
            print(f"{i}. {book}")


def view_all_members(library):
    """Display all registered members."""
    print("\n--- All Registered Members ---")
    if not library.members:
        print("No members registered yet.")
    else:
        for i, member in enumerate(library.members, 1):
            print(f"{i}. {member}")
            if member.borrowed_books:
                print("   Borrowed Books:")
                for book in member.borrowed_books:
                    print(f"   - {book.title} (ISBN: {book.isbn})")


def main():
    """Main application entry point."""
    # Display welcome message
    print("\n" + "=" * 60)
    print("WELCOME TO THE LIBRARY INVENTORY SYSTEM")
    print("=" * 60)
    print("Programming for Problem Solving Using Python")
    print("Assignment 3: Object-Oriented Library Management")
    print("MCA (AI & ML) - Semester I")
    print("=" * 60)
    
    # Initialize library
    library = Library()
    
    # Load existing data
    print("\nLoading existing data...")
    library.load_data()
    
    # Main menu loop
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            add_book_menu(library)
        elif choice == '2':
            register_member_menu(library)
        elif choice == '3':
            borrow_book_menu(library)
        elif choice == '4':
            return_book_menu(library)
        elif choice == '5':
            library.display_report()
        elif choice == '6':
            view_all_books(library)
        elif choice == '7':
            view_all_members(library)
        elif choice == '8':
            print("\nSaving data...")
            library.save_data()
            print("\nThank you for using the Library Management System!")
            print("=" * 60)
            break
        else:
            print("\nError: Invalid choice! Please enter a number between 1 and 8.")
    
    print("\nThanks!\n")


if __name__ == "__main__":
    main()