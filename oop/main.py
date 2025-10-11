# main.py

from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a library
    library = Library()

    # Create some books
    book1 = Book("Things Fall Apart", "Chinua Achebe")
    ebook1 = EBook("Python Programming", "Guido van Rossum", 5)
    printbook1 = PrintBook("Introduction to Algorithms", "Thomas H. Cormen", 1312)

    # Add books to the library
    library.add_book(book1)
    library.add_book(ebook1)
    library.add_book(printbook1)

    # List all books
    library.list_books()


if __name__ == "__main__":
    main()
