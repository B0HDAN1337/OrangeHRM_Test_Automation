import pytest
from selenium import webdriver
from Facades.AuthFacade import AuthFacade
import shutil

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
    return browser
