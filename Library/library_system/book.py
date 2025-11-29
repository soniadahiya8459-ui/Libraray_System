"""
Library Inventory System - Book Module
Author: Student Name
Date: November 21, 2025
Assignment: Programming for Problem Solving Using Python - Assignment 3
Description: Book class to represent library books with borrow/return functionality
"""


class Book:
    """
    Represents a book in the library inventory.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        isbn (str): The ISBN number of the book
        available (bool): The availability status of the book (default: True)
    """
    
    # Class variable to track total books created
    total_books = 0
    
    def __init__(self, title, author, isbn, available=True):
        """
        Initialize a Book object.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            isbn (str): The ISBN number of the book
            available (bool): The availability status (default: True)
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        Book.total_books += 1
    
    def borrow(self):
        """
        Mark the book as borrowed (not available).
        
        Returns:
            bool: True if book was successfully borrowed, False if already borrowed
        """
        if self.available:
            self.available = False
            return True
        else:
            return False
    
    def return_book(self):
        """
        Mark the book as returned (available).
        
        Returns:
            bool: True if book was successfully returned, False if already available
        """
        if not self.available:
            self.available = True
            return True
        else:
            return False
    
    def to_dict(self):
        """
        Convert book object to dictionary for file storage.
        
        Returns:
            dict: Dictionary representation of the book
        """
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'available': self.available
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a Book object from dictionary.
        
        Args:
            data (dict): Dictionary containing book data
            
        Returns:
            Book: A new Book object
        """
        return cls(
            title=data['title'],
            author=data['author'],
            isbn=data['isbn'],
            available=data['available']
        )
    
    def __str__(self):
        """String representation of the book."""
        status = "Available" if self.available else "Borrowed"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"
    
    def __repr__(self):
        """Developer-friendly representation of the book."""
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}', available={self.available})"