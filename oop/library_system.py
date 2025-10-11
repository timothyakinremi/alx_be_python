# library_system.py

class Book:
    """Base class representing a generic book."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library that manages a collection of books."""
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        """Adds a book (Book, EBook, or PrintBook) to the library."""
        if isinstance(book, Book):
            self.books.append(book)
            

    def list_books(self):
        """Lists all books currently in the library."""
        if not self.books:
            print("The library has no books.")
        else:
            for book in self.books:
                print(book)
