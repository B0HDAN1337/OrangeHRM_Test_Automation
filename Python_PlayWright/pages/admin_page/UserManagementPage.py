import pytest
from pages.admin_page.locators.LocatorAddUser import AddUserLocator


class UserManagementPage:
    def __init__(self, page):
        self.page = page

    def click_on_select(self, name_of_select):
       locator = AddUserLocator.select.format(name_of_select)
       self.page.wait_for_selector(locator)
       self.page.click(locator)
    
    def dropdown_select(self, name_of_dropdown):
        locator = AddUserLocator.dropdown.format(name_of_dropdown)
        self.page.wait_for_selector(locator)
        self.page.click(locator)

    def input_value(self, name_of_input, input_value):
        locator = AddUserLocator.input.format(name_of_input)
        self.page.wait_for_selector(locator)
        self.page.fill(locator, input_value)

    def click_on_EmployeeName(self):
        select_employee = AddUserLocator.click_EmployeeName
        self.page.wait_for_selector(select_employee).click()

    def click_button(self, button_name):
        locator = AddUserLocator.button.format(button_name)
        self.page.click(locator)
    
    def alert_success(self):
        locator = self.page.locator(AddUserLocator.alert_success)
        locator.wait_for(state="visible")
        return locator