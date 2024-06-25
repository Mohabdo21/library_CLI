"""
This module defines a Library class and several subclasses for different sections of a library.
Each class provides methods for managing books in that section.
"""

import datetime

from file_man.file_man import FileManager


class Library:
    """A Class representing a library."""

    def __init__(self, filename, section_code):
        """Initialize an empty library."""
        self.file_manager = FileManager(filename)
        self.books = self.file_manager.load_data()
        self.counter = len(self.books)
        self.section_code = section_code

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
        current_time = datetime.datetime.now()
        book_id = (
            f"{self.section_code}-"
            f"{current_time.strftime('%d%m%y')}-"
            f"{current_time.strftime('%H%M')}"
        )
        self.books.append(
            {
                "id": book_id,
                "name": book_name,
                "author": author_name,
                "pages": number_of_pages,
            }
        )
        print(
            f"The Book '{book_name}' was added to Section {self.__class__.__name__}\n"
        )
        self.counter += 1
        self.file_manager.save_data(self.books)

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
                f"The Search Term: '{keyword}' is Not Found in The "
                f"{self.__class__.__name__} Section.\n"
            )

    def display_books(self):
        """Display all Books in The library"""
        if not self.books:
            print(f"No Books in The {self.__class__.__name__} Section.\n")
            return

        print(
            f"    *** Displaying All Books in The {self.__class__.__name__} Section ***    "
        )
        for i, book in enumerate(self.books, start=1):
            print(f"Book no ({i}):")
            print(f"Book ID {book['id']}")
            print(f"Book Name: {book['name']}")
            print(f"Author Name: {book['author']}")
            print(f"Number of Pages: {book['pages']}\n")


class Biology(Library):
    """A Class representing the Biology Section in The library."""

    def __init__(self):
        super().__init__("biologyBookList.txt", "0400")


class Economy(Library):
    """A Class representing the Economy Section in The library."""

    def __init__(self):
        super().__init__("economyBookList.txt", "0500")


class History(Library):
    """A Class representing the History Section in The Library."""

    def __init__(self):
        super().__init__("historyBookList.txt", "0600")
