import pytest
from pages.admin_page.locators.LocatorAddUser import AddUserLocator


class UserManagementPage:
    def __init__(self, page):
        self.page = page

    def click_on_select_role(self, name_of_select):
       locator = AddUserLocator.select.format(name_of_select)
       self.page.wait_for_selector(locator)
       self.page.click(locator)
    
    def dropdown_select_role(self, name):
        locator = AddUserLocator.dropdown.format(name)
        self.page.wait_for_selector(locator)
        self.page.click(locator)