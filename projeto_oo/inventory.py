from models.book import Book

class Inventory:
    def __init__(self, mediator):
        self.books = {}
        self.mediator = mediator

    def add_book(self, book: Book) -> None:
        self.books[book.book_id] = book
    
    def remove_book(self, book_id: int) -> None:
        if book_id in self.books:
            del self.books[book_id]

    def check_availability(self, book_id) -> bool:
        book = self.books.get(book_id)
        return book is not None and book.available

    def update_availability(self, book_id, available) -> None:
        if book_id in self.books:
            self.books[book_id].available = available
