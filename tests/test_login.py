import time
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


@allure.title("Login to Production as admin user")
def test_login_admin():
    admin = User('Admin', 'Password')
    LoginPage().open()
    LoginPage().login_as(admin)


@allure.title("Login to Production center, checking title")
def test_login():
    browser.should(have.title('Trotec Production Center'))
    MainPage().remove_all_jobs()


@allure.title("Used adds several jobs")
def test_user_add_jos():
    MainPage().add_job('destro').add_job('test').add_job('chine').add_job('giant').jobs_list.should(have.size(4))
    MainPage().jobs_list.should(have.exact_texts('giant', 'chine', 'test', 'destro'))


@allure.title("Removes job with particular name")
def test_remove_one_job():
    MainPage().remove_job('test')
    MainPage().jobs_list.should(have.exact_texts('giant', 'chine', 'destro'))


@allure.title("Uploading file from local drive")
def test_upload():
    MainPage().test_upload_from_pc().jobs_list.should(have.texts('vector .pdf', 'giant', 'chine', 'destro'))


@allure.title("Removes all jobs, check that job list has no items")
def test_remove_all():
    MainPage().remove_all_jobs().jobs_list.should(have.size(0))


@allure.title("Uase cant create")
def test_no_name_job():
    MainPage()._add_button.click()
    MainPage().allert.should(have.text('Job name cannot be empty'))
    MainPage().jobs_list.should(have.size(0))
    time.sleep(2)


@allure.title("Comparing 2 screenshots, with empty job list")
def test_compare_job_list():
    assert MainPage().compare(folder, 'No_jobs', NO_JOBS)


@allure.title("Selecting polish language")
def test_compare_language_selection():
    MainPage().pl.click()
    assert MainPage().compare(folder, 'PL', PL_LANGUAGE)


@allure.title("Selecting english language")
def test_compare_language():
    MainPage().en.click()
    assert MainPage().compare(folder, 'EN', EN_LANGUAGE)


@allure.title("Testing canvas displayed")
def test_screen():
    MainPage().canvas(folder, 'test', WORK_PLATE)