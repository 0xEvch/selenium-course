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
  driver.get("http://suninjuly.github.io/execute_script.html")

  x = driver.find_element(By.ID, "input_value")
  x = x.text

  input = driver.find_element(By.ID, "answer")
  input.send_keys(calc(x))

  button = driver.find_element(By.CLASS_NAME, "btn")
  driver.execute_script("return arguments[0].scrollIntoView(true);", button)

  checkbot = driver.find_element(By.ID, "robotCheckbox")
  checkbot.click()

  radiobot = driver.find_element(By.ID, "robotsRule")
  radiobot.click()
  
  button.click()

  time.sleep(30)
finally:
  driver.quit()