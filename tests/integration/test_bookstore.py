import pytest
from src.book_store import BookStore

@pytest.mark.integration
def test_add_multiple_books_and_manage_favorite():
    
    store = BookStore()
    
    # add books
    store.add_book(
        author = " Jory John",
        title = "The Good Egg",
    )
    store.add_book(
        author = " Jacqueline Woodson",
        title = "The Day You Begin"
    )
    
    # assert added books
    assert len(store.books) == 2
    assert store.books[0].book_id == 1
    assert store.books[1].book_id == 2
    
    # Toggle a favorite book using id
    store.toggle_Favorite(1)
    
    # verify the favorite book is added
    assert store.books[0].favorite is True
    
    # favorite book removed
    store.toggle_Favorite(1)
    assert store.books[0].favorite is False
    
    
@pytest.mark.integration
def test_toggle_non_existent_book():
    
    store = BookStore()
    
    store.add_book(
        author = "Russell Punter",
        title = "Goose on the loose"
    )
    
    with pytest.raises(ValueError):
        store.toggle_Favorite(35)
    assert store.books[0].favorite is False
    
    