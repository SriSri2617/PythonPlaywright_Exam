from playwright.sync_api import sync_playwright, expect
from src.features.pages.base_locators import BaseLocators
from src.features.pages.base_locators import Catalog


class CatalogPage:
    def __init__(self, page):
        self.page = page

    def verify_reading_list_heading(self):
        heading = self.page.get_by_role("heading", name="Läslistan")
        expect(heading).to_be_visible()
        

    def verify_heading_visible(self):
        heading = self.page.get_by_role("heading", name="Välkommen!")
        heading.is_visible()
        
        
    def verify_catalog_selected_by_default(self):
        catalog_btn = self.page.get_by_test_id(BaseLocators.Catalog)
        expect(catalog_btn).to_be_disabled()
        
        
    def verify_book_list(self):
        catalog_list = self.page.locator(Catalog.Book_List)
        expect(catalog_list).to_be_visible()
        expect(catalog_list).not_to_have_count(0)

     
    # favorite icon
    def mouse_hover(self):
        book = self.page.locator(Catalog.Book_List).first
        book.hover()
        
    def favorit_icon_display(self):
        icon = self.page.get_by_test_id(Catalog.Fav_Icon)
        expect(icon).to_be_visible()
