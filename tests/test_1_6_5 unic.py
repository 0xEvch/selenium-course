from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
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

    # Отправляем заполненную форму
    btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()