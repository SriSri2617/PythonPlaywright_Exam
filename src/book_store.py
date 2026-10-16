from src.book import Book

class BookStore:
    def __init__(self):
        self.books = []
        
    def add_book(self, author, title):
        book_id = len(self.books)+1
        books = Book(title, author, book_id, favorite = False)
        self.books.append(books)
        
    def toggle_Favorite(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.favorite = not book.favorite
                return
        raise ValueError(f"Book with ID {book_id} not found.")

    def get_book_by_Id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None
