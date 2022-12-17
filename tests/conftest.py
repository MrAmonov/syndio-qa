import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# The following method allows to run the tests under different browsers, but the default browser is set as chrome


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

# This file is for the parameters under which the tests are run


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        # Directories below needs to be switched according to the location of the driver
        service_obj = Service("/opt/homebrew/bin/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service("/opt/homebrew/bin/geckodriver")
        driver = webdriver.Firefox(service=service_obj)
    driver.implicitly_wait(15)
    driver.set_window_size(1920, 1080)
    driver.get("http://localhost:3000/")
    request.cls.driver = driver
    yield
    driver.quit()
