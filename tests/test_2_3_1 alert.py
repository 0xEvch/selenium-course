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
  driver.get("https://suninjuly.github.io/alert_accept.html")

  start = driver.find_element(By.CLASS_NAME, "btn")
  start.click()

  alert = driver.switch_to.alert
  alert.accept()

  x = driver.find_element(By.ID, "input_value")
  x = x.text
  
  result = driver.find_element(By.ID, "answer")
  result.send_keys(calc(x))

  button = driver.find_element(By.CLASS_NAME, "btn")
  button.click()

  time.sleep(30)
finally:
  driver.quit()