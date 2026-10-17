from playwright.sync_api import sync_playwright, expect
from src.features.pages.base_locators import BaseLocators, MyBooks, Catalog

class MinaBocker:
    def __init__(self, page):
        self.page = page
        
        
    # Scenario : Add a favorite book
    
    def view_catalog_page(self):        
        expect(
            self.page.get_by_test_id(
                BaseLocators.Catalog)
        ).to_be_visible()
        
    def click_favorite_icon(self):
        book = self.page.locator(Catalog.Book_List)
        book.hover()
        fav_icon = self.page.get_by_test_id(Catalog.Fav_Icon)
        fav_icon.click()
        
    def verify_favorit_book_icon(self):
        expect(
            self.page.get_by_test_id(
                Catalog.Fav_Icon)
        ).to_be_visible()
        
    def verify_mina_bocker_page(self):
        my_book_page = self.page.get_by_test_id(BaseLocators.My_Book)
        my_book_page.click()
        expect(
            self.page.get_by_test_id(
                MyBooks.My_List)
        ).to_be_visible()
        
      
      # Scenario : Remove a book from favorite  
        
    def verify_favorit_icon_removed_katalog_page(self):
       expect(self.page.get_by_test_id(
            Catalog.Fav_Icon)
        ).not_to_have_class("start selected")
        
    def verify_book_removed_mina_bocker_page(self):
        my_book_page = self.page.get_by_test_id(BaseLocators.My_Book)
        my_book_page.click()
        expect(
            self.page.get_by_test_id(MyBooks.My_List)
        ).to_be_empty()