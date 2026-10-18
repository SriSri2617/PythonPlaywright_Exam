import re
from playwright.sync_api import expect
from src.features.pages.base_locators import AddBookLocators, BaseLocators


class AddBookPage:
    def __init__(self, page):
        self.page = page
       
    # Add_book page    
    def add_book(self):
        self.page.get_by_test_id(
            BaseLocators.Add_Book
        ).click() 
        
    def add_book_page(self):       
        expect(self.page.locator(
            "div.form")
        ).to_be_visible()
       
    # enter title
    def enter_title(self, title):
        self.page.get_by_test_id(
            AddBookLocators.Title_Input
        ).fill(title)
       
        
    def enter_author(self, author):
        self.page.get_by_test_id(
            AddBookLocators.Author_Input
        ).fill(author)
       
        
    def click_add_book(self):
        self.page.get_by_test_id(
            AddBookLocators.Submit_Button
        ).click()
        
    def add_btn_disabled(self):
        expect(self.page.get_by_test_id(
            AddBookLocators.Submit_Button)
        ).to_be_disabled()