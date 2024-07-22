from models.book import Book
from user import User

class Loan:
    def __init__(self, start: str, end: str, book: Book, user: User):
        self.start = start
        self.end = end
        self.book = book
        self.user = user

    def make_rental(self, user: User, book: Book):
        print(f"Processing rental for {user.name} for book '{book.title}'.")
        if self.user.add_rented_book(book):
            print(f"Book '{book.title}' rented successfully by {user.name}.")
        else:
            print(f"Failed to rent book '{book.title}' for {user.name}.")

    def reversal_rental(self, user: User, book: Book):
        print(f"Processing reversal rental for {user.name} for book '{book.title}'.")
        if self.user.remove_rented_book(book):
            print(f"Reversal rental for book '{book.title}' by {user.name} successful.")
        else:
            print(f"Failed to reverse rental for book '{book.title}' by {user.name}.")
