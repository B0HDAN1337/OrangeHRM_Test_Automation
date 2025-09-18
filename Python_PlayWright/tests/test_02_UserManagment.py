import pytest
from pages.admin_page.UserManagementPage import UserManagementPage
from playwright.sync_api import expect

def test_user_add_without_input(logged_in_user, base_url):
    logged_in_user.goto(f"{base_url}/web/index.php/admin/saveSystemUser")
    user_management = UserManagementPage(logged_in_user)
    user_management.click_button("Save")
    requires = user_management.required()
    count = requires.count()
    for i in range(count):
        require = requires.nth(i)
        expect(require).to_be_visible

def test_username_add_less_than_five_characters(logged_in_user, base_url):
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
    user_management.input_value("Username", "corf")
    # Set Password
    user_management.input_value("Password", "qwerty!21")
    user_management.input_value("Confirm Password", "qwerty!21")
    # Save User
    user_management.click_button("Save")
    #Assert on required
    alert = user_management.required()
    expect(alert).to_have_text("Should be at least 5 characters")

def test_password_add_less_than_seven_characters(logged_in_user, base_url):
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
    user_management.input_value("Username", "corffg")
    # Set Password
    user_management.input_value("Password", "1234567")
    user_management.input_value("Confirm Password", "1234567")
    # Save User
    user_management.click_button("Save")
    #Assert on required
    alert = user_management.required()
    expect(alert).to_have_text("Your password must contain minimum 1 lower-case letter")

def test_password_confirm_incorrect(logged_in_user, base_url):
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
    user_management.input_value("Username", "corfklio")
    # Set Password
    user_management.input_value("Password", "qwerty!21aa")
    user_management.input_value("Confirm Password", "qwerty!21s")
    # Save User
    user_management.click_button("Save")
    #Assert on required
    alert = user_management.required()
    expect(alert).to_have_text("Passwords do not match")

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
    user_management.input_value("Username", "USERTest2284")
    # Set Password
    user_management.input_value("Password", "qwerty!21")
    user_management.input_value("Confirm Password", "qwerty!21")
    # Save User
    user_management.click_button("Save")
    #Assert on alert
    alert = user_management.alert_success()
    expect(alert).to_be_visible()
