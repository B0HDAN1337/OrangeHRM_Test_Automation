import pytest
from pages.admin_page.UserManagementPage import UserManagementPage

def test_user_add(logged_in_user, base_url):
    logged_in_user.goto(f"{base_url}/web/index.php/admin/saveSystemUser")
    user_management = UserManagementPage(logged_in_user)
    user_management.click_on_select("User Role")
    user_management.dropdown_select("ESS")


