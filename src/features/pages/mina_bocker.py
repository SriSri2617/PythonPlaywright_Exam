from playwright.sync_api import sync_playwright, expect



class MinaBocker:
    def __init__(self, page):
        self.page = page

        # Reusable locators
        # Katalog 
        self.catalog_list = page.get_by_test_id("catalog")
        # favorit icon (katalog page)
        self.icon = page.get_by_test_id("star-The Pragmatic Procrastinator")
        # mina_bocker
        self.my_book_btn = self.page.get_by_test_id("favorites")
        # favorit_book list (mina böcker page)
        self.favorit_list = self.page.get_by_test_id("book-list")
      
      
        
    def view_catalog_page(self):        
        expect(self.catalog_list).to_be_visible()
        
    def select_favorite_book(self):
        book = self.catalog_list
        book.hover()
        self.icon.click()
        
    def verify_favorit_book_icon(self):
        expect(self.icon).to_be_visible()
        
    def verify_mina_bocker_page(self):
        self.my_book_btn.click()
        expect(self.favorit_list).to_be_visible()
        
    def verify_favorit_icon_removed_katalog_page(self):
        expect(self.icon).not_to_have_class("start selected")
        
    def verify_book_removed_mina_bocker_page(self):
        expect(self.favorit_list).not_to_be_visible()