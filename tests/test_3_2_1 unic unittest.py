from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestAbs(unittest.TestCase): 
    def test_1st(self):
        try: 
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)
            browser.implicitly_wait(5)

            name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
            name.send_keys("Antonio")

            lastname = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
            lastname.send_keys("Hoffman")
            
            email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
            email.send_keys("email@gmail.com")

            phone = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
            phone.send_keys("+7999999")

            address = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
            address.send_keys("addr")
            btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
            btn.click()

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

            welcome_text = welcome_text_elt.text

            expected_text = "Congratulations! You have successfully registered!"
            self.assertEqual(welcome_text, expected_text, f"Expected success message, but displayed {welcome_text}")
        finally:
            browser.quit()

    def test_2nd(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)
            browser.implicitly_wait(5)

            name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
            name.send_keys("Antonio")

            lastname = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
            lastname.send_keys("Hoffman")
            
            email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
            email.send_keys("email@gmail.com")

            phone = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
            phone.send_keys("+7999999")

            address = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
            address.send_keys("addr")
            btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
            btn.click()

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

            welcome_text = welcome_text_elt.text

            expected_text = "Congratulations! You have successfully registered!"
            self.assertEqual(welcome_text, expected_text, f"Expected success message, but displayed {welcome_text}")
        finally:
            browser.quit()

if __name__ == "__main__":
    unittest.main()
