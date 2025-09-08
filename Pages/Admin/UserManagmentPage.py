from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserManagmentPage:
    def __init__(self, browser):
        self.browser = browser

        #locators
        self.input_username = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.button_search = (By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")
        self.button_reset = (By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--ghost")
        self.user_role_select_click = (By.XPATH, "(//div[@class='oxd-select-text-input'])[1]" )
        self.user_role = (By.XPATH, "(//div[@role='listbox']//span[text()='Admin'])")
        

    def search_user_by_username(self, username):
        WebDriverWait(self.browser, 5).until(
        EC.visibility_of_element_located(self.input_username)).send_keys(username)

    def click_button(self):
        self.browser.find_element(*self.button_search).click()
    
    def select_role(self):
        self.browser.find_element(*self.user_role_select_click).click()
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.user_role)).click()
