from models.book import Book

class Inventory:
    def __init__(self):
        self.books = {}

    def add_book(self, book: Book) -> None:
        self.books[book.id] = book
    
    def remove_book(self, id: int) -> None:
        if id in self.books:
            del self.books[id]

    def get_books(self) -> dict:
        return self.books

    def get_book_by_id(self, id: int) -> Book:
        return self.books.get(id)

    def check_availability(self, id: int) -> bool:
        book = self.books.get(id)
        return book is not None and book.available

    def update_availability(self, id: int, available: bool) -> None:
        if id in self.books:
            self.books[id].available = available
