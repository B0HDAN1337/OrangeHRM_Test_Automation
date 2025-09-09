from Pages.Admin.UserAddPage import UserAddPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser"

def test_add_user_role(logged_in_to_website):
    browser = logged_in_to_website
    browser.get(link)
    add_user = UserAddPage(browser)
    add_user.click_new_role()
    add_user.select_new_role()
    add_user.click_new_status()
    add_user.select_new_status()
    add_user.input_hints("manda akhil user")
    add_user.input_username("TestUserName2")
    add_user.input_password("Password12345pass")
    add_user.submit()
    assert WebDriverWait(browser, 5).until(EC.url_contains("viewSystemUsers")), "Url didn't changed"
    