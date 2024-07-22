from models.user_type import UserType
from models.book import Book

class User:
    def __init__(self, ra: str, name: str, user_type: UserType):
        self.ra = ra
        self.name = name
        self.user_type = user_type
        self.rented_books = []

    def can_rent_more_books(self) -> bool:
        if self.user_type == UserType.STUDENT:
            return len(self.rented_books) < 3
        elif self.user_type == UserType.TEACHER:
            return len(self.rented_books) < 10
        return False

    def already_rented_book(self, book: Book)-> bool:
        return isinstance (book, self.rented_books)

    def add_rented_book(self, book: Book) -> bool:
        try:
            self.rented_books.append(book)
            return True
        except:
            return False

    def remove_rented_book(self, book: Book) -> bool:
        try:
            self.rented_books.remove(book)
            return True
        except:
            return False
