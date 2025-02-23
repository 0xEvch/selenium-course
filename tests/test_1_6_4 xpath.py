from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
try:
    driver.get("http://suninjuly.github.io/find_xpath_form")

    input1 = driver.find_element(By.NAME, "first_name")
    input1.send_keys("aboba")

    input2 = driver.find_element(By.NAME, "last_name")
    input2.send_keys("aboba")

    input3 = driver.find_element(By.CLASS_NAME, "city")
    input3.send_keys("aboba")

    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("aboba")

    button = driver.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
    button.click()

    time.sleep(30)
finally:
    driver.quit()