from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart_button(driver):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    driver.get(link)

    add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn-add-to-basket")
    add_to_cart_button.click()

    elements = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.alert"))  
    )

    assert len(elements) == 3