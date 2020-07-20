import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(2)
    request.cls.driver = driver

    yield
    driver.quit()
