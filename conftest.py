import time

import pytest
from locators.main_page_locators import *
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from pages.main_page import MainPage

@pytest.fixture()
def browser_setup():
    time.sleep(10)
    option = webdriver.FirefoxOptions()
    #option.add_argument('--headless')
    option.add_argument("--disable-notifications")
    option.add_argument("--enable-automation")
    option.add_argument("--disable-infobars")
    option.add_argument("--disable-extensions")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-gpu")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--incognito")

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=option)
    driver.set_window_size(1920, 1080)
    driver.get(MainPageLocators.main_link)

    MainPage(driver).click_confirm_cookie_button()
    yield driver
    driver.quit()