from models.book import Book
from user import User

class Loan:
    def __init__(self, start: str, end: str, book: Book, user: User):
        self.start = start
        self.end = end
        self.book = book
        self.user = user
    
    def process_rental(self, user: User, book: Book):
        print(f"Processing rental for {user.name} for book '{book.title}'.")

    def reversal_rental(self, user: User, book: Book):
        print(f"Processing reversal rental for {user.name} for book '{book.title}'.")
