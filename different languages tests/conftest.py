import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en-gb", help="choose language")

@pytest.fixture(scope="function")
def driver(request):
    lang= request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()