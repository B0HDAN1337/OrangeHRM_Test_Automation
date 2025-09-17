import pytest

import re
from playwright.sync_api import expect
from pages.login_page.LoginPage import LoginPage

def test_login_invalid_username_password(page, base_url):
    page.goto(base_url)
    login_page = LoginPage(page)
    login_page.login("Adm", "admin")
    alert = login_page.alert()
    expect(alert).to_be_visible
    expect(alert).to_have_text("Invalid credentials")

def test_login_invalid_username(page, base_url):
    page.goto(base_url)
    login_page = LoginPage(page)
    login_page.login("Adm", "admin123")
    alert = login_page.alert()
    expect(alert).to_be_visible
    expect(alert).to_have_text("Invalid credentials")

def test_login_invalid_password(page, base_url):
    page.goto(base_url)
    login_page = LoginPage(page)
    login_page.login("Admin", "adm")
    alert = login_page.alert()
    expect(alert).to_be_visible
    expect(alert).to_have_text("Invalid credentials")

def test_login_valid(page, base_url):
    page.goto(base_url)
    login_page = LoginPage(page)
    login_page.login("Admin", "admin123")
    expect(page).to_have_url(re.compile(".*dashboard.*"))
    page.context.storage_state(path="storage_state.json")


