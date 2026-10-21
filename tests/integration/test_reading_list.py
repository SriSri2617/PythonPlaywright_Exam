import pytest
from src.book_store import BookStore
from src.fav_books import FavoriteBooks


@pytest.mark.integration
def test_add_multiple_books_and_manage_favorite():

    store = BookStore()

    # add books
    store.addBook(
        author=" Jory John",
        title="The Good Egg"
    )
    store.addBook(
        author=" Jacqueline Woodson",
        title="The Day You Begin"
    )

    # assert added books
    assert len(store.books) == 2
    assert store.books[0].book_id == 1
    assert store.books[1].book_id == 2

    # Toggle a favorite book using id
    store.toggleFavorite(1)

    # verify the favorite book is added
    assert store.books[0].favorite is True

    # favorite book removed
    store.toggleFavorite(1)
    assert store.books[0].favorite is False


@pytest.mark.integration
def test_toggle_non_existent_book():

    store = BookStore()

    store.addBook(
        author="Russell Punter",
        title="Goose on the loose"
    )

    with pytest.raises(ValueError):
        store.toggleFavorite(35)
    assert store.books[0].favorite is False


@pytest.mark.integration
def test_add_book_to_fav_and_remove():

    store = BookStore()
    fav = FavoriteBooks()

    # add book to store
    store.addBook(
        author="Kent Beck",
        title="TDD by Example"
    )

    # Retrive the book
    book = store.get_book_by_Id(1)

    # add to favorite
    fav.add(book)

    # Assert
    assert len(store.books) == 1
    assert len(fav.books) == 1
    assert fav.books[0].author == "Kent Beck"
    assert fav.books[0].title == "TDD by Example"

    # Remove the book
    fav.remove(book)

    # Assert
    assert len(store.books) == 1
