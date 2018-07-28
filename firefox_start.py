# -*- coding: utf-8 -*-


import subprocess

firefox_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'

proc = subprocess.Popen(firefox_path, shell=True, stdout=subprocess.PIPE)
out = proc.communicate()
