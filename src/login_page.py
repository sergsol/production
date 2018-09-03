from src.main_page import MainPage


class LoginPage(object):
    def __init__(self):
        self.user_name = None
        self.password = None
        self.submit = None

    def login_as(self, user):
        self.user_name.set(user.name)
        self.password.set(user.password)
        self.submit.click()
        return MainPage()
