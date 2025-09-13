from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

class UserManagmentPage:
    def __init__(self, browser):
        self.browser = browser

        #locators
        self.input_username = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.button_search = (By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")
        self.button_reset = (By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--ghost")
        self.user_role_select_click = (By.XPATH, "(//div[@class='oxd-select-text-input'])[1]" )
        self.user_role = (By.XPATH, "(//div[@role='listbox']//span[text()='Admin'])")
        self.check_user_name_in_record_found = (By.CSS_SELECTOR, "div.oxd-table-cell.oxd-padding-cell:nth-of-type(2)")
        self.check_user_role_in_record_found = (By.CSS_SELECTOR, "div.oxd-table-cell.oxd-padding-cell:nth-of-type(3)")
        self.click_button_delete = (By.XPATH, "//button[@class='oxd-icon-button oxd-table-cell-action-space']//i[@class='oxd-icon bi-trash']")
        self.check_elert_present = (By.CSS_SELECTOR, "div[role='document']")
        self.delete_user_button = (By. CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--label-danger.orangehrm-button-margin")
        self.success_message_alert = (By.CSS_SELECTOR, "p.oxd-text.oxd-text--p.oxd-text--toast-title.oxd-toast-content-text")
    def search_user_by_username(self, username):
        WebDriverWait(self.browser, 5).until(
        EC.visibility_of_element_located(self.input_username)).send_keys(username)

    def click_button(self):
        self.browser.find_element(*self.button_search).click()
    
    def select_role(self):
        time.sleep(1)
        self.browser.find_element(*self.user_role_select_click).click()
        time.sleep(1)
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.user_role)).click()
        time.sleep(1)

    def check_username(self):
        check = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.check_user_name_in_record_found))
        return check.text
    
    def check_userrole(self):
        check = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.check_user_role_in_record_found))
        return check.text

    def click_delete(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.click_button_delete)).click()
    
    def check_alert_delete(self):
        check = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.check_elert_present))
        return check
    
    def delete_user(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.delete_user_button)).click()
        
    def success_message(self):
        message = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.success_message_alert))
        return message.is_displayed()