from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        #locators
        self.username_input = (By.CSS_SELECTOR, "input[name='username']")
        self.password_input = (By.CSS_SELECTOR, "input[name='password']")
        self.button = (By.CSS_SELECTOR, "button[type=submit]")
        self.error = (By.CSS_SELECTOR, "p.oxd-text.oxd-text--p.oxd-alert-content-text")

    def put_username(self, username):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.username_input)).send_keys(username)

    def put_password(self, password):
        self.browser.find_element(*self.password_input).send_keys(password)
    
    def click_button(self):
        self.browser.find_element(*self.button).click()
    
    def error_msg(self):
        element = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.error)
        )
        return element
    
    