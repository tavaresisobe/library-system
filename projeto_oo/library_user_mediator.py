from inventory import Inventory
from models.book import Book
from user import User
from loan import Loan

class LibraryUserMediator():
    """Mediator para as operacoes do usuario com a biblioteca"""

    def __init__(self, books, users):
        self.books = books
        self.users = users
        self.inventory = Inventory(self)
        self.rental = Loan(self)

    def process_to_rental_book(self, user: User, book_id: int) -> None:
        """Processo para alugar livro"""

        if self.inventory.check_availability(book_id):
            book: Book = self.inventory.books[book_id]
            if user.can_rent_more_books():
                self.rental.make_rental(user, book)
                self.inventory.update_availability(id=book_id, available=False)
            else:
                print(f"{user.name} has reached the limit of rented books for {user.user_type.name.lower()}s.")
        else:
            print(f"Book with ID {book_id} is not available for rent.")

    def process_to_return_book(self, user: User, book_id: int) -> None:
        """Processo para devolver livro"""

        book : Book = self.inventory.books[book_id]
        if user.already_rented_book:
            self.rental.reversal_rental(user, book)
            self.inventory.update_availability(book_id, True)
        else:
            print(f"{user.name} has not rented the currently book.")
