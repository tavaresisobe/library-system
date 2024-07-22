from inventory import Inventory
from models.book import Book

class LibraryMediator():
    """Mediator para as operacoes relacionadas ao inventario da biblioteca"""

    def __init__(self, books):
        self.books = books
        self.inventory = Inventory(self)

    def insert_book(self, book: Book) -> None:
        self.inventory.add_book(book=book)
    
    def get_book(self, book_id) -> Book:
        return self.inventory.get_book_by_id(id=book_id)
    
    def get_books(self) -> dict:
        return self.inventory.get_books()
    
    def remove_book(self, book_id: int) -> None:
        self.inventory.remove_book(book=book_id)
    
    def check_avaible(self, book: Book) -> bool:
        return self.inventory.check_availability(book=book)
