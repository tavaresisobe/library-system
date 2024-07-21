from inventory import Inventory
from user import User
from loan import Loan

class LibraryMediator():
    def __init__(self, books, users):
        self.books = books
        self.users = users
        self.inventory = Inventory(self)
        self.rental = Loan(self)

    def process_rental(self, user: User, book_id: int) -> None:
        if self.inventory.check_availability(book_id):
            book = self.inventory.books[book_id]
            if user.can_rent_more_books():
                self.rental.process_rental(user, book)
                self.inventory.update_availability(book_id, False)
                user.add_rented_book(book)
            else:
                print(f"{user.name} has reached the limit of rented books for {user.user_type.name.lower()}s.")
        else:
            print(f"Book with ID {book_id} is not available for rent.")

    def reversal_rental(self, user: User, book_id: int) -> None:
        if self.inventory.check_availability(book_id):
            book = self.inventory.books[book_id]
            self.rental.reversal_rental(user, book)
            self.inventory.update_availability(book_id, True)
        else:
            print(f"Book with ID {book_id} is not available for rent.")
