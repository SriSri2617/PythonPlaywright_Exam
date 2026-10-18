from playwright.sync_api import expect
from src.features.pages.base_locators import BaseLocators, MyBooks


class MinaBocker:
    def __init__(self, page):
        self.page = page

    # Scenario : Add a favorite book

    def mina_bocker_btn(self):
        self.page.get_by_test_id(
            BaseLocators.My_Book
        ).click()

    def verify_favorites_page_visible(self):
        expect(self.page.locator(
            "div.favorites")
        ).to_be_visible()

    def verify_mina_bocker_page(self):
        expect(
            self.page.get_by_test_id(
                MyBooks.My_List)
        ).to_be_visible()

      # Scenario : Remove a book from favorite

    def verify_book_removed_mina_bocker_page(self):
        expect(
            self.page.get_by_test_id(MyBooks.My_List)
        ).to_be_empty()
