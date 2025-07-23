import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure

@pytest.fixture()
def get_driver(pytestconfig):
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    browser_name = pytestconfig.getini("browser_name")
    logging.info(f'Prepare {browser_name} browser...')
    logging.info(f'Browser {browser_name} has been started...')
    yield driver
    driver.quit()


@pytest.fixture
def go_to_url(page):
    @allure.step('Открытие страницы {url}')
    def callback(url):
        page.goto(url, wait_until='domcontentloaded')
    return callback

