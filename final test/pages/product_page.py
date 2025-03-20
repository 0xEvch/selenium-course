from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()
    
    def should_match_book_name_and_price(self):
        self.should_match_book_name()
        self.should_match_book_price()
        
    
    def should_match_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        added_book_name = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_NAME).text
        
        assert book_name == added_book_name, "Book name not match"

    def should_match_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        added_book_price = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_PRICE).text

        assert book_price == added_book_price, "Book price not match"

    def should_not_show_element(self):
        result = self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
        
        assert result, "Element showed"

    def should_be_disappeared(self):
        result = self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
        
        assert result, "Element appeared"
    
