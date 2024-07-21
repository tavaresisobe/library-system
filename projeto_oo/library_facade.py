from library_mediator import LibraryMediator
from models.book import Book
from user import User

class LibraryFacade:
    def __init__(self):
        self.mediator = LibraryMediator()

    def add_book(self, book_id, title):
        book = Book(book_id, title)
        self.mediator.inventory.add_book(book)

    def rent_book(self, ra, user_name, user_type, book_id):
        user = User(ra, user_name, user_type)
        self.mediator.process_rental(user, book_id)
    
    def remove_book(self, book_id) -> None:
        self.mediator.inventory.remove_book(book_id)
