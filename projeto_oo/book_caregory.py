# arquivo book_category.py

class BookCategory:
    def __init__(self, name: str):
        self.name = name
        self.subcategories = []
        self.books = []

    def add_subcategory(self, subcategory):
        self.subcategories.append(subcategory)

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

    def find_category(self, name: str):
        if self.name == name:
            return self
        for subcategory in self.subcategories:
            result = subcategory.find_category(name)
            if result:
                return result
        return None

    def __repr__(self):
        return f"BookCategory(name={self.name}, subcategories={self.subcategories}, books={self.books})"
