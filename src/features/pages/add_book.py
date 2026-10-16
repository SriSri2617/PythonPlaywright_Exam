import re

class AddBookPage:
    def __init__(self, page):
        self.page = page
       
    # Add_book page    
    def add_book(self):
        add_book_btn = self.page.get_by_test_id("add-book")
        add_book_btn.click()
       
    # enter title
    def enter_title(self, title):
        title_input = self.page.get_by_test_id("add-input-title")
        title_input.fill(title)
        
    def enter_author(self, author):
        author_input = self.page.get_by_test_id("add-input-author")
        author_input.fill(author)
        
    def click_add_book(self):
        add_new_book_btn = self.page.get_by_role("button", name = re.compile("Lägg till ny bok"))
        add_new_book_btn.click()
        
    def open_katalog_page(self):
        katalog_page = self.page.get_by_test_id("catalog")
        katalog_page.click()
   