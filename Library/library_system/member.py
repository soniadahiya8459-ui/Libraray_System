"""
Library Inventory System - Member Module
Author: Student Name
Date: November 21, 2025
Assignment: Programming for Problem Solving Using Python - Assignment 3
Description: Member class to represent library members and their borrowed books
"""


class Member:
    """
    Represents a library member.
    
    Attributes:
        name (str): The name of the member
        member_id (str): The unique member ID
        borrowed_books (list): List of Book objects currently borrowed by the member
    """
    
    def __init__(self, name, member_id):
        """
        Initialize a Member object.
        
        Args:
            name (str): The name of the member
            member_id (str): The unique member ID
        """
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        """
        Borrow a book for the member.
        
        Args:
            book (Book): The Book object to borrow
            
        Returns:
            bool: True if successful, False if book is not available
        """
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        else:
            return False
    
    def return_book(self, book):
        """
        Return a borrowed book.
        
        Args:
            book (Book): The Book object to return
            
        Returns:
            bool: True if successful, False if book was not borrowed by this member
        """
        if book in self.borrowed_books:
            if book.return_book():
                self.borrowed_books.remove(book)
                return True
        return False
    
    def to_dict(self):
        """
        Convert member object to dictionary for file storage.
        
        Returns:
            dict: Dictionary representation of the member
        """
        return {
            'name': self.name,
            'member_id': self.member_id,
            'borrowed_books': [book.isbn for book in self.borrowed_books]
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a Member object from dictionary.
        
        Args:
            data (dict): Dictionary containing member data
            
        Returns:
            Member: A new Member object
        """
        member = cls(
            name=data['name'],
            member_id=data['member_id']
        )
        return member
    
    def __str__(self):
        """String representation of the member."""
        book_count = len(self.borrowed_books)
        return f"Member: {self.name} (ID: {self.member_id}) - Borrowed Books: {book_count}"
    
    def __repr__(self):
        """Developer-friendly representation of the member."""
        return f"Member(name='{self.name}', member_id='{self.member_id}', borrowed_books={len(self.borrowed_books)})"
