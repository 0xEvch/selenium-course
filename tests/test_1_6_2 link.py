from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import math
import time

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

link = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    driver.get("https://suninjuly.github.io/find_link_text")
    
    foundLink = driver.find_element(By.LINK_TEXT, link)
    foundLink.click()

    input1 = driver.find_element(By.NAME, "first_name")
    input1.send_keys("aboba")

    input2 = driver.find_element(By.NAME, "last_name")
    input2.send_keys("aboba")

    input3 = driver.find_element(By.CLASS_NAME, "city")
    input3.send_keys("aboba")

    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("aboba")

    button = driver.find_element(By.CLASS_NAME, "btn")
    button.click()

    time.sleep(60)
finally:
    driver.quit()