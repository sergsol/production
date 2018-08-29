import time
from selene.api import *
from pywinauto import Application
from selene.browser import set_driver
from selene.conditions import text
from selene.support import by
from selene.support.conditions import have
from selene.support.jquery_style_selectors import s, ss
from selene import config, browser
from selenium.webdriver.common.action_chains import ActionChains
from diffimg import diff
from src.pages import MainPage, LoginPage
from src.user import User

config.browser_name = "chrome"


# def test_login_admin():
#     admin = User('Admin', 'Password')
#     LoginPage().login_as(admin)


def test_login():
    MainPage().open()
    browser.should(have.title('Trotec Production Center'))
    MainPage().remove_all_jobs()
#
#
# def test_user_add_jos():
#     MainPage().add_job('destro').add_job('test').add_job('chine').add_job('giant').jobs_list.should(have.size(4))
#     MainPage().jobs_list.should(have.exact_texts('giant', 'chine', 'test', 'destro'))
#
#
# def test_remove_one_job():
#     MainPage().remove_job('test')
#     MainPage().jobs_list.should(have.exact_texts('giant', 'chine', 'destro'))
#
#
# def test_upload():
#     MainPage().test_upload_from_pc().jobs_list.should(have.texts('vector .pdf', 'giant', 'chine', 'destro'))
#
#
# def test_remove_all():
#     MainPage().remove_all_jobs().jobs_list.should(have.size(0))


def test_compare():
    MainPage().compare()
