# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor that initializes the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that announces when a Book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Human-readable string representation of the Book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation of the Book object for debugging and recreation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Example usage (you can remove this part if not needed):
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    print(str(book1))   # Human-readable format
    print(repr(book1))  # Reproducible format
    del book1           # Triggers destructor
