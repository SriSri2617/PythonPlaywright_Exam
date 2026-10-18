from playwright.sync_api import sync_playwright, expect
from src.features.pages.base_locators import BaseLocators
from src.features.pages.base_locators import Catalog


class CatalogPage:
    def __init__(self, page):
        self.page = page
        
    def click_catalog_btn(self):
        catalog_btn = self.page.get_by_test_id(BaseLocators.Catalog)
        catalog_btn.click()
        
    def view_catalog_page(self):  
        expect(
            self.page.get_by_test_id(
                BaseLocators.Catalog)
        ).to_be_visible()

    def verify_reading_list_heading(self):
       expect(self.page.get_by_role(
           "heading", name="Läslistan")
       ).to_be_visible()
        

    def verify_heading_visible(self):
        expect(self.page.get_by_role(
            "heading", name="Välkommen!")
        ).to_be_visible()
        
        
    def verify_catalog_selected_by_default(self):
        expect(self.page.get_by_test_id(
            BaseLocators.Catalog)
        ).to_be_disabled()
        
        
    def verify_book_list(self):
        catalog_list = self.page.locator(Catalog.Book_List)
        expect(catalog_list).to_be_visible()
        expect(catalog_list).not_to_have_count(0)

     
    # favorite icon
    def mouse_hover(self):
        book = self.page.locator(Catalog.Book_List).first
        book.hover()

    def click_favorite_icon(self):
        self.page.get_by_test_id(
            Catalog.Fav_Icon
        ).click()
      
           
    def favorit_icon_display(self):
        expect(self.page.get_by_test_id(
            Catalog.Fav_Icon)
        ).to_be_visible()
        
    def verify_favorit_icon_removed(self):
       expect(self.page.get_by_test_id(
            Catalog.Fav_Icon)
        ).not_to_have_class("start selected")
        
    def get_book_count(self):
        return self.page.locator(".catalog .book").count()    
    
    def get_fav_book_count(self):
        return self.page.locator(".star.selected").count()