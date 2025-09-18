import pytest
from pages.admin_page.UserManagementPage import UserManagementPage
from playwright.sync_api import expect

mapping = {
    2: "Username",
    3: "User_Role",
    4: "Employee_Name",
    5: "Status"
}

@pytest.mark.parametrize("search_data", [
    {"Username": "USERTest2284", "User_Role": "ESS", "Employee_Name": "James Butler", "Status": "Enabled"}
])
def test_search_user(logged_in_user, base_url, search_data):
    logged_in_user.goto(f"{base_url}/web/index.php/admin/viewSystemUsers")
    user_management = UserManagementPage(logged_in_user)
    # By Username
    user_management.input_value("Username", search_data["Username"])
    # By User Role 
    user_management.click_on_select("User Role")
    user_management.dropdown_select(search_data["User_Role"])
    # By Employee Name
    user_management.input_value("Employee Name", search_data["Employee_Name"])
    user_management.click_on_EmployeeName()
    # By Status
    user_management.click_on_select("Status")
    user_management.dropdown_select(search_data["Status"])
    # Search 
    user_management.click_button("Search")
    # Expect values
    values_in_table = user_management.table_result()
    for i, key in mapping.items():
        value = values_in_table.nth(i)
        expect(value).to_have_text(search_data[key])
    

