from models.user_type import UserType
from library_mediator import LibraryMediator

class User:
    def __init__(self, ra: str, name: str, user_type: int):
        self.ra = ra
        self.name = name
        self.user_type = user_type
        self.rented_books = []

    def can_rent_more_books(self) -> int:
        if self.user_type == UserType.STUDENT:
            return len(self.rented_books) < 3
        elif self.user_type == UserType.TEACHER:
            return len(self.rented_books) < 10
        return False

    def add_rented_book(self, book):
        self.rented_books.append(book)
