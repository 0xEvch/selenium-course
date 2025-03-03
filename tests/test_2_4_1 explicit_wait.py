from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)

try:
  driver.get("https://suninjuly.github.io/explicit_wait2.html")

  WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

  book = driver.find_element(By.ID, "book")
  book.click()

  x = driver.find_element(By.ID, "input_value")
  x = x.text
  
  result = driver.find_element(By.ID, "answer")
  result.send_keys(calc(x))

  button = driver.find_element(By.ID, "solve")
  button.click()

  time.sleep(10)
finally:
  driver.quit()