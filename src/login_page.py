from selene.support.jquery_style_selectors import s
from selene import browser
from src.main_page import MainPage


class LoginPage(object):
    def __init__(self):
        self.user_name = s('input[formcontrolname="userName"]')
        self.password = s('input[formcontrolname="password"]')
        self.submit = s('button[type="submit"]')

    def open(self):
        browser.open_url("/")
        return self

    def login_as(self, user):
        self.user_name.set(user.name)
        self.password.set(user.password)
        self.submit.click()
        return MainPage()
