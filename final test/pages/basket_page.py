from .base_page import BasePage
from .locators import BasketPageLocators
import pytest

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_not_have_items_in_basket()
        self.should_show_empty_basket_message()

    def should_not_have_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), "Basket is not empty"
    
    def should_show_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "No message about empty basket"