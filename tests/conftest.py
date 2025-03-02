import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# import sys
# import os
#
# # Get the project root directory
# ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
#
# # Add the root directory to sys.path
# sys.path.insert(0, ROOT_DIR)
from pages.login_page import LoginPage


@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.wait = WebDriverWait(driver, 10)
    yield driver
    driver.quit()


@pytest.fixture()
def login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login_button()
    assert "dashboard" in driver.current_url.lower(), "Login failed!"
    return driver
