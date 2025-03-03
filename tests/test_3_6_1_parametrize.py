from credentials import login, password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math

lessons = ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905']

def answer():
    return math.log(int(time.time()))

@pytest.fixture(scope="function")
def stepik_login(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://stepik.org/catalog")

    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="/catalog?auth=login"]')))
    login_btn.click()

    email_input = wait.until(EC.element_to_be_clickable((By.ID, 'id_login_email')))
    email_input.send_keys(login)

    password_input = driver.find_element(By.ID, 'id_login_password')
    password_input.send_keys(password)

    driver.find_element(By.CLASS_NAME, "sign-form__btn").click()

@pytest.mark.skip
@pytest.mark.parametrize('lesson', lessons)
def test_parametrize(stepik_login, driver, lesson):
    wait = WebDriverWait(driver, 10)

    link = f'https://stepik.org/lesson/{lesson}/step/1'

    driver.get(link)

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'navbar__profile-img')))

    driver.get(link)
    input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[spellcheck=false][autocorrect="off"]')))
    input.send_keys(answer)

    button = driver.find_element(By.CLASS_NAME, "submit-submission")
    button.click()

    check = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text

    assert check == "Correct!", "Wrong answer"

def test_parametrize_light(stepik_login, driver):
    wait = WebDriverWait(driver, 10)

    link = 'https://stepik.org/lesson/236896/step/1'

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'navbar__profile-img')))

    driver.get(link)
    input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[spellcheck=false][autocorrect="off"]')))
    input.send_keys(answer)

    button = driver.find_element(By.CLASS_NAME, "submit-submission")
    button.click()

    check = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text

    assert check == "Correct!", "Wrong answer"