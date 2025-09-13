from Pages.LoginPage import LoginPage

class AuthFacade:
    def __init__(self, browser):
        self.login_page = LoginPage(browser)
    
    def login_as(self, username, password):
        self.login_page.put_username(username)
        self.login_page.put_password(password)
        self.login_page.click_button()