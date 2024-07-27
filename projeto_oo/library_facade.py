from library_mediator import LibraryMediator
from library_user_mediator import LibraryUserMediator
import logging

LOGGER = logging.getLogger('sLogger')

class LibraryFacade:
    def __init__(self):
        self.library_mediator = LibraryMediator()
        self.user_library_mediator = LibraryUserMediator()
        self.inventory = [] #lista de livros (guarda objetos do tipo Book)
        self.users = [] #lista de usuarios (guarda objetos do tipo User)
        self.loan = [] #lista de alugueis (guarda objetos do tipo Loan)

    def register_book(self, book_id: int, title: str, author: str, category: str) -> None:
        book_model = self.library_mediator.insert_book(book_id=book_id, title=title, 
                                                       author=author, category=category)
        self.inventory.append(book_model)

        LOGGER.info(f"Livro cadastrado com sucesso")

    def delete_book(self, book_id: int) -> None:
        book_model = self.library_mediator.remove_book(actual_inventary=self.inventory,
                                                       book_id=book_id)
        self.inventory = book_model

        LOGGER.info(f"Livro removido com sucesso")

    def search_book(self, book_id) -> None:
        search_return = self.library_mediator.get_book(actual_inventary=self.inventory,
                                                       book_id=book_id)
        print(f"Livro com id correspondente: {search_return}")

        LOGGER.info(f"Busca concluida com sucesso")

    def search_for_all_books(self) -> None:
        search_return = self.library_mediator.get_books(actual_inventary=self.inventory)
        print(f"Livros cadastrados: {search_return}")

        LOGGER.info(f"Busca concluida com sucesso")

    def check_availability(self, book_id: int) -> None:
        availability = self.library_mediator.check_available(actual_inventary=self.inventory,
                                                             book_id=book_id)
        if availability:
            print(f"O livro com ID {book_id} está disponível")
        else:
            print(f"O livro com ID {book_id} não está disponível")

        LOGGER.info(f"Verificacao concluida com sucesso")

    def rent_book(self, ra: str, book_id: int) -> None:
        self.inventory, self.users, self.loan = self.user_library_mediator.process_to_rental_book(users_list=self.users,
                                                          actual_inventary = self.inventory,
                                                          rent=self.loan, ra=ra,
                                                          book_id=book_id)

    def return_rent_book(self, ra: str, book_id: int) -> None:
        self.inventory, self.users, self.loan = self.user_library_mediator.process_to_return_book(users_list=self.users,
                                                          actual_inventary = self.inventory,
                                                          rent=self.loan, ra=ra,
                                                          book_id=book_id)
