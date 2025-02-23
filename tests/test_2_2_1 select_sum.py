from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def calc(x, y):
  return str(int(x) + int(y))

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
try:
  driver.get("http://suninjuly.github.io/selects2.html")

  x = driver.find_element(By.ID, "num1")
  x = x.text
  y = driver.find_element(By.ID, "num2")
  y = y.text

  select = Select(driver.find_element(By.TAG_NAME, "select"))
  select.select_by_value(calc(x,y)) 

  button = driver.find_element(By.CLASS_NAME, "btn")
  button.click()

  time.sleep(30)
finally:
  driver.quit()