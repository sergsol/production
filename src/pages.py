import cv2
import datetime
import os
import time
import numpy as np
import pywinauto
from pywinauto import Application
from selene import browser
from selene.support import by
from selene.api import *
from selene.support.jquery_style_selectors import s, ss
config.browser_name = 'chrome'

class MainPage(object):

    def __init__(self):
        self._new_job_mane = s('#jobsListNewJobNameInput')
        self._add_button = s('#jobsListNewJobNameButton')
        self.jobs_list = ss(by.xpath(' //*[starts-with(@id,"jobsListJob")]//h3'))
        self.first_job = browser.element(by.xpath(' (//*[starts-with(@id,"jobsListJob")]//h3)[1]'))
        self.removes = browser.elements(by.xpath('//h3[@class="mat-line"]/../../button'))
        self._body = s('mat-toolbar.mat-primary > span:nth-child(1)')
        self.job = 'h3.mat-line'
        self.work_plate = '#canvasPanel'

    def job(self, name):
        return '//h3[contains(text(), "{}")]'.format(name)


    def open(self):
        browser.open_url("http://localhost:4200/")
        return self

    # def open(self):
    #     browser.open_url("https://html5demos.com/drag/")
    #     return self

    def add_job(self, name):
        self._new_job_mane.set(name)
        self._add_button.click()
        return self

    def test_upload_from_pc(self):

        s('#dropZone').click()
        time.sleep(1)
        app = Application().connect(title_re="Open*")
        app.Open.Edit.set_edit_text('C:\\Users\\ssoloshchenko\\Desktop\\jobs\\vector .pdf')  # update path to local file
        while True:
            try:
                app.Open.Button.click()  # open button is getting focused
            except pywinauto.findbestmatch.MatchError:
                break
        browser.element(by.xpath('//button[text() = "Upload"]')).click()
        time.sleep(1)
        return self


    def remove_job(self, job_name):
        s(by.xpath('//h3[contains(text(), "{}")]/../..//button[starts-with(@id,"jobsListJobDeleteButton")]'.format(job_name))).click()
        return self

    # def remove_jobs(self, *jobs):
    #     for job in jobs:
    #         s(by.xpath('//h3[contains(text(), "{}")]/../../button'.format(job))).click()
    #     return self

    def remove_all_jobs(self):
        time.sleep(1)
        jobs = ss(by.xpath('//button[starts-with(@id,"jobsListJobDeleteButton")]'))
        count = len(jobs)
        while count >= 1:
                jobs[count - 1].click()
                time.sleep(0.1)
                count -= 1
        return self

    def create_folder(self):
        """Creating folder"""
        defaut = 'C:\\Users\\ssoloshchenko\\job_control\\' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')
        try:
            os.makedirs(defaut)
            return defaut
        except OSError:
            print('Error: Creating directory. ' + defaut)

    def compare(self):
        image_folder = self.create_folder()
        time.sleep(2)
        #Will take a screenshot as png and will place it in newly created folder
        path = browser.take_screenshot(path=image_folder, filename='Actual_result')

        expected = cv2.imread('C:\\Users\\ssoloshchenko\\job_control\\Expected_result.png')
        actual = cv2.imread(path)
        difference = cv2.subtract(expected, actual)
        result = not np.any(difference)
        if result is True:
            print("Images are same")
        else:
            cv2.imwrite('{}\\result.png'.format(image_folder), difference)
            print('Images are different')


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
