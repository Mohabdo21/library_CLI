# Library Management System

This project provides a simple and interactive shell for managing different sections of a library. It allows users to add, lookup, and display books in the Biology, Economy, and History sections.

## Files

The project consists of two main Python files:

1. `library.py`: This module defines a `Library` class and several subclasses for different sections of a library. Each class provides methods for managing books in that section.

2. `script.py`: This script provides an interactive shell for managing different sections of a library. It allows the user to add, lookup, and display books in the Biology, Economy, and History sections.

## Classes

### Library

The `Library` class represents a library. It provides the following methods:

- `load_books()`: Load books from a file.
- `save_books()`: Save books to a file.
- `add_book()`: Add a book to the library.
- `lookup_book()`: Search for a book in the library.
- `display_books()`: Display all books in the library.

### Biology, Economy, History

These classes represent the Biology, Economy, and History sections in the library. They are subclasses of the `Library` class and inherit all its methods.

## LibraryShell

The `LibraryShell` class provides an interactive shell for managing different sections in the library. It provides the following commands:

- `add SECTION`: Add a new book to the selected section.
- `lookup SECTION`: Search for a book in the selected section.
- `display SECTION`: Display all books available in the selected section.
- `exit`: Exit the program.

## Usage

To start the interactive shell, run the `script.py` script:

```
bash
./script.py
```


```
$ ./script.py
Welcome to the library shell, Type help or ? to list commands.

(library)  help

Documented commands (type help <topic>):
========================================
add  display  exit  help  lookup

(library)  add biology
Adding a Book to the Section Biology
Enter The name of The Book: Guns, Germs, and Steel
Enter The name of The Author: Book by Jared Diamond
Enter The Number of The Pages: 480
(library)  exit
Thank you For using library. Good Bye!
```
