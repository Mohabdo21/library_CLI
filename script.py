#!/usr/bin/env python3
"""
This script provides an interactive shell for managing different sections of a library.
It allows the user to add, lookup, and display books in
the Biology, Economy, and History sections.
"""

import cmd

from library.library import Biology, Economy, History


class LibraryShell(cmd.Cmd):
    """
    An interactive shell for managing different sections in the library.
    """

    intro = "Welcome to the library shell, Type help or ? to list commands.\n"
    prompt = "(library)  "

    def __init__(self):
        super().__init__()
        self.sections = {
            "biology": Biology(),
            "economy": Economy(),
            "history": History(),
        }

    def get_section(self, arg):
        """Get the library Section from the provided Argument."""
        if not arg:
            print("No Section Provided. Pleae Provide a Section.")
            return None

        section = self.sections.get(arg)
        if section is None:
            print(
                "Invalid Section. Please Choose from: 'biology', 'economy', or 'history'."
            )
        return section

    def do_add(self, arg):
        """Add a new Book to the Selected Section"""
        if not arg:
            print("No Section Provided. Please Provide a Section.")
            return

        section = self.get_section(arg)
        if section is None:
            return

        section.add_book()

    def do_lookup(self, arg):
        """Search for a Book in the Selected Section."""
        if not arg:
            print("No Section Provided. Please Provide a Section.")
            return

        section = self.get_section(arg)
        if section is None:
            return
        section.lookup_book()

    def do_display(self, arg):
        """Display all Books Available in the selected Section."""
        if not arg:
            print("No Section Provided. Please Provide a Section.")
            return

        section = self.get_section(arg)
        if section is None:
            return
        section.display_books()

    def do_exit(self, _):
        """Exit the Program."""
        print("Thank you For using library. Good Bye!")
        return True

    def help_add(self):
        """Print the help message for the add command."""
        print(
            "\n".join(
                [
                    "Add a new Book to the section.",
                    "Usage: add SECTION",
                    "Example: add biology",
                    "This will Prompt you to input Book Details to add it to Biology Section.",
                ]
            )
        )

    def help_lookup(self):
        """Print the help message for the lookup command."""
        print(
            "\n".join(
                [
                    "Search foor a Book in Selected Section.",
                    "Usage: lookup SECTION",
                    "Example: lookup history",
                    "This will Prompt you to Enter a Search Term to Search for a Book.",
                ]
            )
        )

    def help_display(self):
        """Print the help message for the display command."""
        print(
            "\n".join(
                [
                    "Display all Available Books in the Selected Section.",
                    "Usage: display SECTION",
                    "Example: display economy",
                    "Display all Available Books in the Selected Section.",
                ]
            )
        )

    def help_exit(self):
        """Print the help message for the exit command."""
        print(
            "\n".join(
                [
                    "Exit the Library Program.",
                    "Usage: exit",
                ]
            )
        )


if __name__ == "__main__":
    LibraryShell().cmdloop()
