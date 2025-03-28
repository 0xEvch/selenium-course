from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

def test_guest_can_go_to_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()