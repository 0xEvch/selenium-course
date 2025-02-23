from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://suninjuly.github.io/huge_form.html")

    for i in range(0,100):
        input = driver.find_elements(By.TAG_NAME, "input")
        input[i].send_keys("fdd")

    button = driver.find_element(By.CLASS_NAME, "btn")
    button.click()

    time.sleep(30)
finally:
    driver.quit()