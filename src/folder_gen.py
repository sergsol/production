import datetime
import os


class Folder(object):

    def __init__(self):
        self.folder = self.create_folder()

    def create_folder(self):
        """Creating folder"""
        defaut = 'C:\\Users\\ssoloshchenko\\job_control\\' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')
        try:
            os.makedirs(defaut)
            return defaut
        except OSError:
            print('Error: Creating directory. ' + defaut)