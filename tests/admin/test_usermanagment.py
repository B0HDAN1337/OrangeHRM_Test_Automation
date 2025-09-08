import pytest
from Pages.Admin.UserManagmentPage import UserManagmentPage
import time

link = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"

def test_search_user(logged_in_to_website):
    browser = logged_in_to_website
    browser.get(link)
    user_management = UserManagmentPage(browser)
    user_management.search_user_by_username("Admin")
    user_management.click_button()
    user_management.select_role()
    time.sleep(2)
    