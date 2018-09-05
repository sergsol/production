import datetime
import os


class Folder(object):

    def create_folder(self):
        """Creating folder"""
        defaut = 'C:\\Users\\ssoloshchenko\\job_control\\' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')
        try:
            os.makedirs(defaut)
            return defaut
        except OSError:
            print('Error: Creating directory. ' + defaut)