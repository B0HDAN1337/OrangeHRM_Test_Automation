import pytest
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
import time

link = "https://opensource-demo.orangehrmlive.com/"


def test_login(browser):
    browser.get(link)
    login_page = LoginPage(browser)
    login_page.put_username("Admin")
    login_page.put_password("admin123")
    login_page.click_button()
    time.sleep(2)
    assert "index" in browser.current_url

def test_login_invalid(browser):
    browser.get(link)
    login_page = LoginPage(browser)
    login_page.put_username("test_invalid")
    login_page.put_password("password")
    login_page.click_button()
    error_message = login_page.error_msg()
    assert "Invalid credentials" in error_message.text

