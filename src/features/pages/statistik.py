from playwright.sync_api import expect
from src.features.pages.base_locators import BaseLocators, Statistics
import re

class Statistic:
    def __init__(self, page):
        self.page = page
        
    def statistic_page(self):
        self.page.get_by_test_id(BaseLocators.Statistics).click()
        
        
    def verify_total_book_count(self):
        expect(
            self.page.get_by_test_id(
                Statistics.Book_Count)
        ).to_be_visible()
             
        
    def verify_fav_book_count(self):
        expect(self.page.get_by_test_id(
            Statistics.Fav_Count)
        ).to_be_visible()    
        

    def get_book_count_stats_page(self): 
        text = self.page.get_by_test_id(Statistics.Book_Count).inner_text()
        match = re.search(r"\d+", text)
        assert match, f"No number found in book count text: {text!r}" 
        return int(match.group())
    
    def get_fav_book_count_stats_page(self):
        fav_text = self.page.get_by_test_id(Statistics.Fav_Count).inner_text()
        match = re.search(r"\d+", fav_text) 
        assert match, f"No number found in favourite count text: {fav_text!r}" 
        return int(match.group())