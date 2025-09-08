import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Facades.AuthFacade import AuthFacade
import shutil
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture
def logged_in_to_website(browser):
    browser.get("https://opensource-demo.orangehrmlive.com/")
    auth = AuthFacade(browser)
    auth.login_as("Admin", "admin123")
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.oxd-topbar-header-title"))
        )
    return browser
