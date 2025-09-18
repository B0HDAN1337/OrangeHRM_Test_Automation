import pytest
from pages.admin_page.UserManagementPage import UserManagementPage
from playwright.sync_api import expect

def test_user_add(logged_in_user, base_url):
    logged_in_user.goto(f"{base_url}/web/index.php/admin/saveSystemUser")
    user_management = UserManagementPage(logged_in_user)
    # Select Role
    user_management.click_on_select("User Role")
    user_management.dropdown_select("ESS")
    # Select Status
    user_management.click_on_select("Status")
    user_management.dropdown_select("Enabled")
    # Employee Name
    user_management.input_value("Employee Name", "James  Butler")
    user_management.click_on_EmployeeName()
    # Username
    user_management.input_value("Username", "Userq123344d")
    # Set Password
    user_management.input_value("Password", "qwerty!21")
    user_management.input_value("Confirm Password", "qwerty!21")
    # Save User
    user_management.click_button("Save")
    #Assert on alert
    alert = user_management.alert_success()
    expect(alert).to_be_visible()
