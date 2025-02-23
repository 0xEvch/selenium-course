from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 

try:
  driver.get("https://suninjuly.github.io/file_input.html")

  fName = driver.find_element(By.CSS_SELECTOR, "[name='firstname']")
  fName.send_keys("aboba")

  lName = driver.find_element(By.CSS_SELECTOR, "[name='lastname']")
  lName.send_keys("aboba")

  email = driver.find_element(By.CSS_SELECTOR, "[name='email']")
  email.send_keys("aboba@aboba.com")

  file = driver.find_element(By.ID, "file")
  file.send_keys(file_path)

  button = driver.find_element(By.CLASS_NAME, "btn")
  button.click()

  time.sleep(10)
finally:
  driver.quit()