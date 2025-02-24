import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import allure


@pytest.fixture(scope="session")
def web_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get('http://127.0.0.1:8000/')

    yield driver
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    driver.quit()
