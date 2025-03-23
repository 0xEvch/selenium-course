from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "i.icon-signin")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group > a.btn")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    VIEW_BASKET = (By.CSS_SELECTOR, "p > a.btn-info:first-child")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    ADDED_BOOK_NAME = (By.CSS_SELECTOR, "div.alertinner > strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    ADDED_BOOK_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "div#content_inner > p")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "form.basket_summary")