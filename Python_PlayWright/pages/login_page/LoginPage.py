from pages.login_page.locator import LoginLocator


class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.fill(LoginLocator.input_login, username)
        self.page.fill(LoginLocator.input_password, password)
        self.page.click(LoginLocator.button_login)

    def alert(self):
        return self.page.locator(LoginLocator.alert_element)
    

        