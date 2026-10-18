from playwright.sync_api import sync_playwright, expect
from src.features.pages.base_locators import BaseLocators, MyBooks, Catalog

class MinaBocker:
    def __init__(self, page):
        self.page = page
        
        
    # Scenario : Add a favorite book
       
    def verify_mina_bocker_page(self):
        my_book_page = self.page.get_by_test_id(BaseLocators.My_Book)
        my_book_page.click()
        expect(
            self.page.get_by_test_id(
                MyBooks.My_List)
        ).to_be_visible()
        
      
      # Scenario : Remove a book from favorite      
            
    def verify_book_removed_mina_bocker_page(self):
        my_book_page = self.page.get_by_test_id(BaseLocators.My_Book)
        my_book_page.click()
        expect(
            self.page.get_by_test_id(MyBooks.My_List)
        ).to_be_empty()