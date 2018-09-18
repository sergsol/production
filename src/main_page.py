import cv2
import time
import numpy as np
import pywinauto
from allure_commons.types import AttachmentType
from pywinauto import Application
from selene import browser
from selene.support import by
from selene.api import *
from selene.support.jquery_style_selectors import s, ss
# config.browser_name = 'chrome'
from PIL import Image


class MainPage(object):

    def __init__(self):
        self._header = s('app-lbl[ng-reflect-key="Header_Toolbar_WelcomeTo"]')
        self.pl = s(by.xpath('//div[text()="PL"]'))
        self.en = s(by.xpath('//div[text()="EN"]'))
        ############################################################
        self._new_job_mane = s('#jobsListNewJobNameInput')
        self._add_button = s('#jobsListNewJobNameButton')
        self.jobs_list = ss(by.xpath(' //*[starts-with(@id,"jobsListJob")]//h3'))
        self.first_job = browser.element(by.xpath(' (//*[starts-with(@id,"jobsListJob")]//h3)[1]'))
        self.removes = browser.elements(by.xpath('//h3[@class="mat-line"]/../../button'))
        self._body = s('mat-toolbar.mat-primary > span:nth-child(1)')
        self.job = 'h3.mat-line'
        self.work_plate = '#canvasPanel'
        ############################################################
        self.allert = s(by.xpath('//snack-bar-container//span'))
        ############################################################
        self.work_tab = s(by.xpath('//app-lbl[text()="Work"]'))

    def job(self, name):
        return '//h3[contains(text(), "{}")]'.format(name)

    def open(self):
        browser.open_url("/")
        return self

    def add_job(self, name):
        self._new_job_mane.set(name)
        self._add_button.click()
        return self

    def test_upload_from_pc(self):

        s('#jobsListAttachJobButton').click()
        time.sleep(1)
        app = Application().connect(title_re="Open*")
        app.Open.Edit.set_edit_text('C:\\Users\\ssoloshchenko\\Desktop\\jobs\\vector .pdf')  # update path to local file
        while True:
            try:
                app.Open.Button.click()  # open button is getting focused
            except pywinauto.findbestmatch.MatchError:
                break
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

    def compare_screens(self, name_expected, path, image_folder, test):
        expected = cv2.imread(name_expected)
        actual = cv2.imread(path)
        difference = cv2.subtract(expected, actual)
        result = not np.any(difference)
        if result is True:
            print("Images are same")
            return True
        else:
            cv2.imwrite('{}\\{}.png'.format(image_folder, test), difference)
            print('Images are different')
            return False


    def compare(self, f, name, name_expected, test):
        image_folder = f
        time.sleep(2)
        #Will take a screenshot as png and will place it in newly created folder
        path = browser.take_screenshot(path=image_folder, filename='{}'.format(name))
        return self.compare_screens(name_expected, path, image_folder, test)


    def screenshot(self, f, name):
        image_folder = f
        time.sleep(2)
        # Will take a screenshot as png and will place it in newly created folder
        browser.take_screenshot(path=image_folder, filename='{}'.format(name))


    def compare_canvas(self, f, name, name_expected, test):
        #TODO add object as a paremeter
        image_folder = f
        element = s("#canvas123")
        location = element.location
        size = element.size
        path = browser.take_screenshot(path=image_folder, filename='{}'.format(name))
        x = location['x']
        y = location['y']
        width = location['x'] + size['width']
        height = location['y'] + size['height']
        im = Image.open(path)
        im = im.crop((int(x), int(y), int(width), int(height)))
        im.save(path)
        return self.compare_screens(name_expected, path, image_folder, test)

