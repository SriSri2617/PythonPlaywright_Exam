import pytest
from src.fav_books import FavoriteBooks
from src.book_store import Book

  
@pytest.mark.unit 
def test_add_books_to_favorite():
    
    favorite_books = FavoriteBooks()
        
    book = Book(
        title = "The Tomten",
        author = "Astrid Lindgren",
        book_id = 1, 
        favorite = False
    )
    
    favorite_books.add(book)
        
    assert len(favorite_books.books) == 1
    assert favorite_books.books[0] == book
   # assert favorite_books.books[0].title == "The Tomten"    
    
@pytest.mark.unit 
def test_remove_book_from_favorites():
    
    favorites = FavoriteBooks()

    book = Book(
        author = "Kent Beck",
        title = "TDD by Example",
        book_id = 1,
        favorite = False
    )

    favorites.add(book)
    favorites.remove(book)

    assert len(favorites.books) == 0

