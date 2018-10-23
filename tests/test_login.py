import time
import pytest
from allure_commons.types import AttachmentType
from selene.api import *
from selene.support.conditions import have
from selene import config, browser
from images import *
from src.folder_gen import Folder
from src.login_page import LoginPage
from src.main_page import MainPage
from src.user import User
import allure


folder = Folder().create_folder()


@allure.title("Login button is disabled")
def test_try_login():
    LoginPage().open()
    LoginPage().user_name.should(be.blank)
    LoginPage().password.should(be.blank)
    LoginPage().submit.should_not(be.clickable)


@allure.title("Login to Production as admin user")
def test_login_admin():
    admin = User('Admin', 'Password')
    LoginPage().login_as(admin)
    LoginPage().submit.should_not(be.clickable)


@allure.title("Login to Production center, checking title")
def test_login():
    browser.should(have.title('Trotec Production Center'))
    MainPage().remove_all_jobs()


@allure.title("User adds several jobs")
def test_user_add_jos():
    MainPage().add_job('destro').add_job('test').add_job('chine').add_job('giant').jobs_list.should(have.size(4))
    MainPage().jobs_list.should(have.exact_texts('giant', 'chine', 'test', 'destro'))


@allure.title("Removes job with particular name")
def test_remove_one_job():
    MainPage().remove_job('test')
    MainPage().jobs_list.should(have.exact_texts('giant', 'chine', 'destro'))
    time.sleep(1)


# @allure.title("Uploading file from local drive")
# def test_upload():
#     MainPage().test_upload_from_pc().jobs_list.should(have.texts('vector .pdf', 'giant', 'chine', 'destro'))


@allure.title("Removes all jobs, check that job list has no items")
def test_remove_all():
    MainPage().remove_all_jobs().jobs_list.should(have.size(0))


@allure.title("User can't create job without name")
def test_no_name_job():
    MainPage()._add_button.click()
    MainPage().allert.should(have.text('Job name cannot be empty'))
    MainPage().jobs_list.should(have.size(0))
    time.sleep(2)


# @allure.title("Comparing 2 screenshots, with empty job list")
# def test_compare_job_list():
#     assert MainPage().compare(folder, 'No_jobs', NO_JOBS, 'Jobs list has items')


@allure.title("Selecting polish language")
def test_compare_language_selection():
    MainPage().pl.click()
    assert MainPage().compare(folder, 'PL', PL_LANGUAGE, 'Polish not selected')


@allure.title("Welcome is in polish language")
def test_pl_header():
    MainPage()._header.should(have.exact_text('Witamy w'))


@allure.title("Selecting english language")
def test_compare_language():
    MainPage().en.click()
    assert MainPage().compare(folder, 'EN', EN_LANGUAGE, 'English not selected')


@allure.title("Welcome is in english language")
def test_pl_header():
    MainPage()._header.should(have.exact_text('Welcome to'))


@allure.title("Testing canvas displayed")
def test_screen():
    MainPage().work_tab.click()
    assert MainPage().compare_canvas(folder, 'Canvas', WORK_PLATE, 'Canvas_error')