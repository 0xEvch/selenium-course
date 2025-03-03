import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action="store", default=None, help="Choose browser: Chrome or Firefox")

@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    driver = None
    if browser_name.lower() == "chrome":
        print("\start Chrome browser")
        driver = webdriver.Chrome()
    elif browser_name.lower() == "firefox":
        print("\start Firefox browser")
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be Chrome or Firefox")
    yield driver
    print("\quit browser")
    driver.quit()