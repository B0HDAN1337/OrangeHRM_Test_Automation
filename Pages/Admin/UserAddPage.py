from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class UserAddPage:
    def __init__(self, browser):
        self.browser = browser
    
        #locators
        self.user_role_click = (By.XPATH, "//label[text()='User Role']/../../div/div[@class='oxd-select-wrapper']")
        self.user_role = (By.XPATH, "(//div[@role='listbox']//span[text()='Admin'])")
        self.user_status_click = (By.XPATH, "//label[text()='Status']/../../div/div[@class='oxd-select-wrapper']")
        self.user_status = (By.XPATH, "(//div[@role='listbox']//div[@role='option']//span[text()='Enabled'])")
        self.hints = (By.CSS_SELECTOR, "input[placeholder='Type for hints...']")
        self.hint_click = (By.XPATH, "(//div[@role='listbox']//span[text()='manda akhil user'])")
        self.username = (By.XPATH, "//label[text()='Username']/../../div/input[@class='oxd-input oxd-input--active']")
        self.inputs_password = (By.CSS_SELECTOR, "input[type='password']")
        self.button_submit = (By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space")
    def click_new_role(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.user_role_click)).click()
    
    def select_new_role(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.user_role)).click()
        
    def click_new_status(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.user_status_click)).click()
        
    def select_new_status(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.user_status)).click()
    
    def input_hints(self, hint):
        self.browser.find_element(*self.hints).send_keys(hint)
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.hint_click)).click()
    
    def input_username(self, username):
        self.browser.find_element(*self.username).send_keys(username)

    def input_password(self, password):
        inputs = self.browser.find_elements(*self.inputs_password)
        for input in inputs:
            input.send_keys(password)
    
    def submit(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.button_submit)).click()