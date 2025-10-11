# library_system.py

class Book:
    """Base class representing a generic book."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    def __init__(self, title: str, author: str, file_size: int):
        # Call the constructor of the base class
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        return f"'{self.title}' by {self.author} [E-Book, {self.file_size}MB]"


class PrintBook(Book):
    """Derived class representing a printed book."""
    def __init__(self, title: str, author: str, page_count: int):
        # Call the constructor of the base class
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"'{self.title}' by {self.author} [Print Book, {self.page_count} pages]"


class Library:
    """Class representing a library that manages a collection of books."""
    def __init__(self):
        self.books = []  # list to store all book objects

    def add_book(self, book: Book):
        """Adds a book (Book, EBook, or PrintBook) to the library."""
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added {book.title} to the library.")
        else:
            print("Only Book or its subclasses can be added to the library.")

    def list_books(self):
        """Lists all books currently in the library."""
        if not self.books:
            print("The library has no books.")
        else:
            print("\nBooks in the library:")
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book}")
