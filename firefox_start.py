# -*- coding: utf-8 -*-

import subprocess

firefox_path = 'firefox'

proc = subprocess.Popen(firefox_path, shell=True, stdout=subprocess.PIPE)
out = proc.communicate()
