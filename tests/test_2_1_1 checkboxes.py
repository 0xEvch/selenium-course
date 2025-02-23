from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
try:
    driver.get("https://suninjuly.github.io/math.html")

    x = driver.find_element(By.ID, "input_value")
    x = x.text
    
    result = driver.find_element(By.ID, "answer")
    result.send_keys(calc(x))

    checkbot = driver.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbot.click()

    radiobot = driver.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radiobot.click()

    button = driver.find_element(By.CLASS_NAME, "btn")
    button.click()

    time.sleep(30)
finally:
    driver.quit()