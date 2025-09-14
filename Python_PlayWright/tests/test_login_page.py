import pytest

import re
from playwright.sync_api import expect
from pages.login_page.LoginPage import LoginPage

def test_login_valid(page, base_url):
    page.goto(base_url)
    login_page = LoginPage(page)
    login_page.login("Admin", "admin123")
    expect(page).to_have_url(re.compile(".*dashboard.*"))

def test_login_invalid(page, base_url):
    page.goto(base_url)
    login_page = LoginPage(page)
    login_page.login("Adm", "admin")
    alert = login_page.alert()
    expect(alert).to_have_text("Invalid credentials")
