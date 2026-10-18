import pytest
from src.book_store import BookStore

@pytest.mark.unit 
def test_add_book():
    
    store = BookStore()
    
    store.addBook(
        author = "Kent Beck",
        title = "TDD by Example"
    )

    assert len(store.books) == 1
    assert store.books[0].author == "Kent Beck"
    assert store.books[0].title == "TDD by Example"
    

@pytest.mark.unit 
def test_toggle_favorite():
    store = BookStore()

    store.addBook(
        author = "Kent Beck",
        title = "TDD by Example"
    )

    store.toggleFavorite(1)

    assert store.books[0].favorite is True
    

@pytest.mark.unit 
def test_get_book_by_id():
    store = BookStore()

    store.addBook(
        author="Kent Beck",
        title="TDD by Example"
    )

    book = store.get_book_by_Id(1)

    assert book is not None
    assert book.book_id == 1
    assert book.title == "TDD by Example"
    

@pytest.mark.unit 
def test_get_book_by_id_not_found():
    store = BookStore()

    book = store.get_book_by_Id(99)

    assert book is None 