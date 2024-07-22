from library_user_mediator import LibraryUserMediator
from library_meditor import LibraryMediator
from models.book import Book
from user import User

class LibraryFacade:
    def __init__(self):
        self.library_mediator = LibraryMediator()
        self.user_library_mediator = LibraryUserMediator()

    def add_book(self, book_id: int, title: str, author: str, category: str) -> None:
        new_book = Book(id=book_id, title=title, author=author, category=category)
        self.library_mediator.insert_book(book=new_book)

    def search_book(self, book_id) -> Book:
        print(f'result of searching by id: {self.library_mediator.get_book(book_id=book_id)}')

    def list_books(self) -> None:
        print(f'result of searching: {self.library_mediator.get_books()}')

    def remove_book(self, book_id: int) -> None:
        self.library_mediator.remove_book(id=book_id)

    def check_availability(self, book_id: int) -> bool:
        if self.library_mediator.check_avaible(id=book_id):
            print (f'the book with id {book_id} is avaible')
        else:
            print (f'the book with id {book_id} is not avaible')

    def rent_book(self, ra: str, user_name: str, user_type: int, book_id: int) -> None:
        user = User(ra=ra, user_name=user_name, user_type=user_type)
        self.user_library_mediator.process_to_rental_book(user=user, book_id=book_id)

    def return_rent_book(self, ra: str, user_name: str, user_type: int, book_id: int) -> None:
        user = User(ra=ra, user_name=user_name, user_type=user_type)
        self.user_library_mediator.process_to_return_book(user=user, book_id=book_id)
