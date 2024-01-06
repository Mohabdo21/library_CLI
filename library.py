"""
This module defines a Library class and several subclasses for different sections of a library.
Each class provides methods for managing books in that section.
"""
import json


class Library:
    """A Class representing a library."""

    def __init__(self, filename):
        """Initialize an empty library."""
        self.books = []
        self.counter = 0
        self.filename = filename

    def load_books(self):
        """Load books from a file."""
        try:
            with open(self.filename, "r", encoding="utf-8") as infile:
                try:
                    self.books = json.load(infile)
                except json.JSONDecodeError:
                    print(
                        f"The file {self.filename} is empty or does not contain valid JSON."
                    )
                    self.books = []
                self.counter = len(self.books)
        except FileNotFoundError:
            print(f"The file {self.filename} is not found")
            print("Starting a New Book List")

    def save_books(self):
        """Save books to a file."""
        with open(self.filename, "w", encoding="utf-8") as outfile:
            json.dump(self.books, outfile)

    def add_book(self):
        """Add Book to the library."""
        print(f"Adding a Book to the Section {self.__class__.__name__}")
        book_name = input("Enter The name of The Book: ")
        author_name = input("Enter The name of The Author: ")
        while True:
            number_of_pages = input("Enter The Number of The Pages: ")
            if number_of_pages.isdigit() and int(number_of_pages) > 0:
                break
            print("Envalid Input. Please Enter a Positive Integer.")
        self.books.append(
            {"name": book_name, "author": author_name, "pages": number_of_pages}
        )
        self.counter += 1
        self.save_books()

    def lookup_book(self):
        """Search for a Book in the library."""
        print(f"Looking up for a Book in {self.__class__.__name__}")
        keyword = input("Enter Search Term: ").lower()
        found = False
        for book in self.books:
            if keyword in map(str.lower, book.values()):
                print(f"Book Name: {book['name']}")
                print(f"Author Name: {book['author']}")
                print(f"Number of Pages: {book['pages']}\n")
                found = True
            if not found:
                print(
                    f"The Book is Not Found in The Section {self.__class__.__name__}."
                )

    def display_books(self):
        """Display all Books in The library"""
        if not self.books:
            print(f"No Books in The {self.__class__.__name__} Section.")
            return

        print(f"Displaying All Books in The {self.__class__.__name__} Section ...")
        for i, book in enumerate(self.books, start=1):
            print(f"Book no ({i}):")
            print(f"Book Name: {book['name']}")
            print(f"Author Name: {book['author']}")
            print(f"Number of Pages: {book['pages']}\n")


class Biology(Library):
    """A Class representing the Biology Section in The library."""

    def __init__(self):
        super().__init__("biologyBookList.txt")
        self.load_books()


class Economy(Library):
    """A Class representing the Economy Section in The library."""

    def __init__(self):
        super().__init__("economyBookList.txt")
        self.load_books()


class History(Library):
    """A Class representing the History Section in The Library."""

    def __init__(self):
        super().__init__("historyBookList.txt")
        self.load_books()
