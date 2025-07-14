# library_management.py

class Book:
    """
    Represents a book in the library with a title, author, and availability status.
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False # Private attribute to track availability

    def check_out(self):
        """
        Marks the book as checked out.
        Returns True if successful, False if already checked out.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Marks the book as available.
        Returns True if successful, False if already available.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """
        Checks if the book is currently available.
        Returns:
            bool: True if available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = [] # Private list to store Book instances

    def add_book(self, book: Book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        self._books.append(book)
        # print(f"Added '{book.title}' to the library.") # For internal testing

    def check_out_book(self, title: str):
        """
        Checks out a book by its title.

        Args:
            title (str): The title of the book to check out.
        """
        found = False
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                found = True
                break
        if not found:
            print(f"'{title}' not found in the library.")

    def return_book(self, title: str):
        """
        Returns a book by its title.

        Args:
            title (str): The title of the book to return.
        """
        found = False
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' is already available.")
                found = True
                break
        if not found:
            print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """
        Lists all books that are currently available in the library.
        """
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books currently available.")
        else:
            for book in available_books:
                print(book)

