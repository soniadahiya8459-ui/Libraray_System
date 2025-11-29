"""
Library Inventory System - Library Management Module
Author: Student Name
Date: November 21, 2025
Assignment: Programming for Problem Solving Using Python - Assignment 3
Description: Library class to manage books, members, and borrowing operations
"""

import json
import os
from book import Book
from member import Member


class Library:
    """
    Represents the library management system.
    
    Attributes:
        books (list): List of all Book objects in the library
        members (list): List of all Member objects registered
        borrow_history (dict): Track borrow count for each ISBN
    """
    
    def __init__(self):
        """Initialize the Library with empty books and members lists."""
        self.books = []
        self.members = []
        self.borrow_history = {}  # ISBN -> borrow count
    
    def add_book(self, title, author, isbn):
        """
        Add a new book to the library.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            isbn (str): The ISBN number of the book
            
        Returns:
            Book: The newly created Book object, or None if ISBN already exists
        """
        # Check if book with same ISBN already exists
        if self.find_book_by_isbn(isbn):
            print(f"Warning: Book with ISBN {isbn} already exists!")
            return None
        
        book = Book(title, author, isbn)
        self.books.append(book)
        self.borrow_history[isbn] = 0
        print(f"Success: Book added - {book.title}")
        return book
    
    def register_member(self, name, member_id):
        """
        Register a new member to the library.
        
        Args:
            name (str): The name of the member
            member_id (str): The unique member ID
            
        Returns:
            Member: The newly created Member object, or None if ID already exists
        """
        # Check if member with same ID already exists
        if self.find_member_by_id(member_id):
            print(f"Warning: Member with ID {member_id} already exists!")
            return None
        
        member = Member(name, member_id)
        self.members.append(member)
        print(f"Success: Member registered - {member.name}")
        return member
    
    def lend_book(self, member_id, isbn):
        """
        Lend a book to a member.
        
        Args:
            member_id (str): The member ID
            isbn (str): The ISBN of the book
            
        Returns:
            bool: True if successful, False otherwise
        """
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_isbn(isbn)
        
        if not member:
            print(f"Error: Member with ID {member_id} not found!")
            return False
        
        if not book:
            print(f"Error: Book with ISBN {isbn} not found!")
            return False
        
        if member.borrow_book(book):
            self.borrow_history[isbn] += 1
            print(f"Success: '{book.title}' borrowed by {member.name}")
            return True
        else:
            print(f"Error: '{book.title}' is currently not available!")
            return False
    
    def take_return(self, member_id, isbn):
        """
        Accept a book return from a member.
        
        Args:
            member_id (str): The member ID
            isbn (str): The ISBN of the book
            
        Returns:
            bool: True if successful, False otherwise
        """
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_isbn(isbn)
        
        if not member:
            print(f"Error: Member with ID {member_id} not found!")
            return False
        
        if not book:
            print(f"Error: Book with ISBN {isbn} not found!")
            return False
        
        if member.return_book(book):
            print(f"Success: '{book.title}' returned by {member.name}")
            return True
        else:
            print(f"Error: '{book.title}' was not borrowed by {member.name}!")
            return False
    
    def find_book_by_isbn(self, isbn):
        """
        Find a book by its ISBN.
        
        Args:
            isbn (str): The ISBN to search for
            
        Returns:
            Book: The Book object if found, None otherwise
        """
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def find_member_by_id(self, member_id):
        """
        Find a member by their ID.
        
        Args:
            member_id (str): The member ID to search for
            
        Returns:
            Member: The Member object if found, None otherwise
        """
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    
    def get_most_borrowed_book(self):
        """
        Get the most borrowed book.
        
        Returns:
            tuple: (Book, count) or (None, 0) if no books borrowed
        """
        if not self.borrow_history or max(self.borrow_history.values()) == 0:
            return None, 0
        
        most_borrowed_isbn = max(self.borrow_history, key=self.borrow_history.get)
        book = self.find_book_by_isbn(most_borrowed_isbn)
        count = self.borrow_history[most_borrowed_isbn]
        return book, count
    
    def get_active_members_count(self):
        """
        Get the count of active members (members who have borrowed books).
        
        Returns:
            int: Number of active members
        """
        return sum(1 for member in self.members if len(member.borrowed_books) > 0)
    
    def get_borrowed_books_count(self):
        """
        Get the total number of books currently borrowed.
        
        Returns:
            int: Number of books currently borrowed
        """
        return sum(1 for book in self.books if not book.available)
    
    def display_report(self):
        """Display library analytics report."""
        print("\n" + "=" * 60)
        print("LIBRARY ANALYTICS REPORT")
        print("=" * 60)
        
        print(f"\nTotal Books in Library: {len(self.books)}")
        print(f"Total Registered Members: {len(self.members)}")
        print(f"Books Currently Borrowed: {self.get_borrowed_books_count()}")
        print(f"Active Members: {self.get_active_members_count()}")
        
        most_borrowed, count = self.get_most_borrowed_book()
        if most_borrowed:
            print(f"\nMost Borrowed Book:")
            print(f"   Title: {most_borrowed.title}")
            print(f"   Author: {most_borrowed.author}")
            print(f"   Times Borrowed: {count}")
        else:
            print(f"\nMost Borrowed Book: None (No books borrowed yet)")
        
        print("\n" + "=" * 60)
    
    def save_data(self, books_file='books.json', members_file='members.json'):
        """
        Save library data to JSON files.
        
        Args:
            books_file (str): Filename for books data
            members_file (str): Filename for members data
        """
        try:
            # Save books
            books_data = {
                'books': [book.to_dict() for book in self.books],
                'borrow_history': self.borrow_history
            }
            with open(books_file, 'w') as f:
                json.dump(books_data, f, indent=4)
            
            # Save members
            members_data = {
                'members': [member.to_dict() for member in self.members]
            }
            with open(members_file, 'w') as f:
                json.dump(members_data, f, indent=4)
            
            print(f"Success: Data saved successfully!")
            
        except Exception as e:
            print(f"Error: Failed to save data - {e}")
    
    def load_data(self, books_file='books.json', members_file='members.json'):
        """
        Load library data from JSON files.
        
        Args:
            books_file (str): Filename for books data
            members_file (str): Filename for members data
        """
        try:
            # Load books
            if os.path.exists(books_file):
                with open(books_file, 'r') as f:
                    books_data = json.load(f)
                    self.books = [Book.from_dict(book) for book in books_data.get('books', [])]
                    self.borrow_history = books_data.get('borrow_history', {})
                print(f"Info: Loaded {len(self.books)} books from file")
            else:
                print(f"Info: No existing books file found, starting fresh")
            
            # Load members
            if os.path.exists(members_file):
                with open(members_file, 'r') as f:
                    members_data = json.load(f)
                    self.members = [Member.from_dict(member) for member in members_data.get('members', [])]
                
                # Re-link borrowed books
                for member_data in members_data.get('members', []):
                    member = self.find_member_by_id(member_data['member_id'])
                    for isbn in member_data.get('borrowed_books', []):
                        book = self.find_book_by_isbn(isbn)
                        if book and not book.available:
                            member.borrowed_books.append(book)
                
                print(f"Info: Loaded {len(self.members)} members from file")
            else:
                print(f"Info: No existing members file found, starting fresh")
                
        except json.JSONDecodeError as e:
            print(f"Error: Corrupted JSON file - {e}")
            print(f"Info: Starting with empty library")
        except Exception as e:
            print(f"Error: Failed to load data - {e}")
            print(f"Info: Starting with empty library")
