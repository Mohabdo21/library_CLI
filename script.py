#!/usr/bin/env python3
"""
This script provides an interactive shell for managing different sections of a library.
It allows the user to add, lookup, and display books in the Biology, Economy, and History sections.
"""

import cmd
import sys

from library.library import Biology, Economy, History


class LibraryShell(cmd.Cmd):
    """
    An interactive shell for managing different sections in the library.
    """

    intro = "Welcome to the library shell. Type help or ? to list commands.\n"
    prompt = "(library) "

    def __init__(self):
        super().__init__()
        self.sections = {
            "biology": Biology(),
            "economy": Economy(),
            "history": History(),
        }

    def get_section(self, section_name):
        """Retrieve the library section from the provided name."""
        section = self.sections.get(section_name.lower())
        if section is None:
            print(
                "Invalid section. Please choose from: 'biology', 'economy', or 'history'."
            )
        return section

    def do_add(self, section_name):
        """Add a new book to the selected section."""
        section = self.get_section(section_name)
        if section:
            section.add_book()

    def do_lookup(self, section_name):
        """Search for a book in the selected section."""
        section = self.get_section(section_name)
        if section:
            section.lookup_book()

    def do_display(self, section_name):
        """Display all books available in the selected section."""
        section = self.get_section(section_name)
        if section:
            section.display_books()

    def do_display_all(self, _):
        """Display all books in the library."""
        for section in self.sections.values():
            section.display_books()

    def do_exit(self, _):
        """Exit the program."""
        print("Thank you for using the library. Goodbye!")
        return True

    def help_add(self):
        """Print the help message for the add command."""
        print(
            "\n".join(
                [
                    "Add a new book to the section.",
                    "Usage: add SECTION",
                    "Example: add biology",
                    "This will prompt you to input book details to add it to the Biology section.",
                ]
            )
        )

    def help_lookup(self):
        """Print the help message for the lookup command."""
        print(
            "\n".join(
                [
                    "Search for a book in the selected section.",
                    "Usage: lookup SECTION",
                    "Example: lookup history",
                    "This will prompt you to enter a search term to search for a book.",
                ]
            )
        )

    def help_display(self):
        """Print the help message for the display command."""
        print(
            "\n".join(
                [
                    "Display all available books in the selected section.",
                    "Usage: display SECTION",
                    "Example: display economy",
                    "Display all available books in the selected section.",
                ]
            )
        )

    def help_display_all(self):
        """Print the help message for the display_all command."""
        print(
            "\n".join(
                ["Display all available books in the library.", "Usage: display_all"]
            )
        )

    def help_exit(self):
        """Print the help message for the exit command."""
        print("\n".join(["Exit the library program.", "Usage: exit"]))


if __name__ == "__main__":
    shell = LibraryShell()
    if len(sys.argv) < 2:  # Interactive mode
        shell.cmdloop()
    else:  # Non-interactive mode
        shell.onecmd(" ".join(sys.argv[1:]))
