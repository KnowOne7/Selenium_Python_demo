import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    #browser = request.config.getoption("--browser")
    browser = request.param
    print(f"\nCreating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox' but got {browser}")
        # my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # my_driver.implicitly_wait(10)
    yield my_driver
    print(f"\nClosing {browser} Driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browsers to execute tests (chrome or firefox)"
    )

