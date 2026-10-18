class BaseLocators:
    # page locators
    Catalog = "catalog"            # test-id
    Add_Book = "add-book"          # test-id
    My_Book = "favorites"          # test-id
    Statistics = "statistics"  # test-id


class AddBookLocators:
    # Lägg till bok page locators
    Title_Input = "add-input-title"     # test-id
    Author_Input = "add-input-author"   # test-id
    Submit_Button = "add-submit"        # test-id


class Catalog:
    # Katalog page locators
    Book_List = ".catalog"      # CSS class
    Fav_Icon = "star-The Pragmatic Procrastinator"      # test-id


class MyBooks:
    My_List = "book-list"      # test-id


class Statistics:
    Book_Count = "book-count"   # test-id
    Fav_Count = "stars-count"   # test-id
