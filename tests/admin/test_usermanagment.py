import pytest
from Pages.Admin.UserManagmentPage import UserManagmentPage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"

def test_search_user_by_name(logged_in_to_website):
    browser = logged_in_to_website
    browser.get(link)
    user_management = UserManagmentPage(browser)
    user_management.search_user_by_username("TestUserName2")
    user_management.click_button()
    check_username = user_management.check_username()
    assert "TestUserName2" in check_username

def test_search_user_by_role(logged_in_to_website):
    browser = logged_in_to_website
    browser.get(link)
    user_managment = UserManagmentPage(browser)
    user_managment.select_role()
    user_managment.click_button()
    time.sleep(1)
    check_role = user_managment.check_userrole()
    assert "Admin" in check_role
    